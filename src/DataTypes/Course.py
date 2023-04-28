from abc import ABC
from typing import Any, Dict, List, TypedDict

from src.DataTypes.DataTypes import Requisite
from src.DataTypes.LearningOutcome import LearningOutcome

CourseMetrics = TypedDict(
    "CurriculumMetrics",
    {
        "blocking factor": int,
        "delay factor": int,
        "centrality": int,
        "complexity": float,
        "requisite distance": int,
    },
)


# Course-related data types:
#
#                               AbstractCourse
#                                /          \
#                          Course       CourseCollection
#
# A requirement may involve a set of courses (CourseSet), or a set of requirements (RequirementSet), but not both.
class AbstractCourse(ABC):
    """
    The `AbstractCourse` data type is used to represent the notion of an abstract course that may appear in a curriculum
    or degree plan. That is, this abstract type serves as a placeholder for a course in a curriculum or degree plan,
    where the abstract course may correspond to a single course, or a set of courses, where only one of the courses in the
    set should be taken at that particular point in the curriculum or degree plan. This allows a user to specify a course
    or a collection of courses as a part part of a curriculum or degree plans. The two possible concrete subtypes of
    an `AbstractCourse` are:
    - `Course` : a specific course.
    - `CourseCollection` : a set of courses, any of which can serve as the required course in a curriculum or degree plan.
    """

    id: int
    "Unique course id"
    vertex_id: Dict[int, int]
    "The vertex id of the course w/in a curriculum graph, stored as (curriculum_id, vertex_id)"

    name: str
    "Name of the course, e.g., Introduction to Psychology"
    credit_hours: float
    'Number of credit hours associated with course or a "typcial" course in the collection. For the purpose of analytics, variable credits are not supported'

    institution: str
    "Institution offering the course"
    college: str
    "College or school (within the institution) offering the course"
    department: str
    "Department (within the school or college) offering the course"
    canonical_name: str
    "Standard name used to denote the course in the discipline, e.g., Psychology I, or course collection, e.g., math genearl education"

    requisites: Dict[int, Requisite]
    "List of requisites, in (requisite_course id, requisite_type) format"
    learning_outcomes: List[LearningOutcome]
    "A list of learning outcomes associated with the course"
    metrics: CourseMetrics
    "Course-related metrics"
    metadata: Dict[str, Any]
    "Course-related metadata"


##############################################################
# Course data type
class Course(AbstractCourse):
    """
    The `Course` data type is used to represent a single course consisting of a given number
    of credit hours.  To instantiate a `Course` use:

        Course(name, credit_hours; <keyword arguments>)

    # Arguments
    Required:
    - `name:AbstractString` : the name of the course.
    - `credit_hours:int` : the number of credit hours associated with the course.
    Keyword:
    - `prefix:AbstractString` : the prefix associated with the course.
    - `num:AbstractString` : the number associated with the course.
    - `institution:AbstractString` : the name of the institution offering the course.
    - `canonical_name:AbstractString` : the common name used for the course.

    # Examples:
    ```julia-repl
    julia> Course("Calculus with Applications", 4, prefix="MA", num="112", canonical_name="Calculus I")
    ```
    """

    prefix: str
    "Typcially a department prefix, e.g., PSY"
    num: str
    "Course number, e.g., 101, or 302L"
    cross_listed: List["Course"]
    'courses that are cross-listed with the course (same as "also offered as")'

    passrate: float
    "Percentage of students that pass the course"

    # Constructor
    def __init__(
        self,
        name: str,
        credit_hours: float,
        prefix: str = "",
        learning_outcomes: List[LearningOutcome] = [],
        num: str = "",
        institution: str = "",
        college: str = "",
        department: str = "",
        cross_listed: List["Course"] = [],
        canonical_name: str = "",
        id: int = 0,
        passrate: float = 0.5,
    ) -> None:
        self.name = name
        self.credit_hours = credit_hours
        self.prefix = prefix
        self.num = num
        self.institution = institution
        if id == 0:
            self.id = hash(self.name + self.prefix + self.num + self.institution)
        else:
            self.id = id
        self.college = college
        self.department = department
        self.cross_listed = cross_listed
        self.canonical_name = canonical_name
        self.requisites = {}
        # self.requisite_formula
        self.metrics = {
            "blocking factor": -1,
            "centrality": -1,
            "complexity": -1,
            "delay factor": -1,
            "requisite distance": -1,
        }
        self.metadata = {}
        self.learning_outcomes = learning_outcomes
        # curriculum id -> vertex id, note: course may be in multiple curricula
        self.vertex_id = {}

        self.passrate = passrate


class CourseCollection(AbstractCourse):
    courses: List[Course]
    "Courses associated with the collection                                   "

    # Constructor
    def __init__(
        self,
        name: str,
        credit_hours: float,
        courses: List[Course],
        institution: str = "",
        college: str = "",
        department: str = "",
        canonical_name: str = "",
        id: int = 0,
    ) -> None:
        self.name = name
        self.credit_hours = credit_hours
        self.courses = courses
        self.institution = institution
        if id == 0:
            self.id = hash(self.name + self.institution + str(len(courses)))
        else:
            self.id = id
        self.college = college
        self.department = department
        self.canonical_name = canonical_name
        self.requisites = {}
        # self.requisite_formula
        self.metrics = {
            "blocking factor": -1,
            "centrality": -1,
            "complexity": -1,
            "delay factor": -1,
            "requisite distance": -1,
        }
        self.metadata = {}
        self.vertex_id = {}  # curriculum id -> vertex id


def course_id(prefix: str, num: str, name: str, institution: str) -> int:
    return hash(name + prefix + num + institution)


def add_requisite(
    requisite_course: AbstractCourse, course: AbstractCourse, requisite_type: Requisite
) -> None:
    """
        add_requisite!(rc, tc, requisite_type)

    Add course rc as a requisite, of type requisite_type, for target course tc.

    # Arguments
    Required:
    - `rc::AbstractCourse` : requisite course.
    - `tc::AbstractCourse` : target course, i.e., course for which `rc` is a requisite.
    - `requisite_type::Requisite` : requisite type.

    # Requisite types
    One of the following requisite types must be specified for the `requisite_type`:
    - `pre` : a prerequisite course that must be passed before `tc` can be attempted.
    - `co`  : a co-requisite course that may be taken before or at the same time as `tc`.
    - `strict_co` : a strict co-requisite course that must be taken at the same time as `tc`.
    """

    course.requisites[requisite_course.id] = requisite_type


def add_requisites(
    requisite_courses: List[AbstractCourse],
    course: AbstractCourse,
    requisite_types: List[Requisite],
) -> None:
    """
        add_requisite!([rc1, rc2, ...], tc, [requisite_type1, requisite_type2, ...])

    Add a collection of requisites to target course tc.

    # Arguments
    Required:
    - `rc::Array{AbstractCourse}` : and array of requisite courses.
    - `tc::AbstractCourse` : target course, i.e., course for which `rc` is a requisite.
    - `requisite_type::Array{Requisite}` : an array of requisite types.

    # Requisite types
    The following requisite types may be specified for the `requisite_type`:
    - `pre` : a prerequisite course that must be passed before `tc` can be attempted.
    - `co`  : a co-requisite course that may be taken before or at the same time as `tc`.
    - `strict_co` : a strict co-requisite course that must be taken at the same time as `tc`.
    """

    assert len(requisite_courses) == len(requisite_types)
    for i in range(len(requisite_courses)):
        course.requisites[requisite_courses[i].id] = requisite_types[i]


def delete_requisite(requisite_course: Course, course: Course) -> None:
    """
        delete_requisite!(rc, tc)

    Remove course rc as a requisite for target course tc.  If rc is not an existing requisite for tc, an
    error is thrown.

    # Arguments
    Required:
    - `rc::AbstractCourse` : requisite course.
    - `tc::AbstractCourse` : target course, i.e., course for which `rc` is a requisite.

    """
    # if !haskey(course.requisites, requisite_course.id)
    #    error("The requisite you are trying to delete does not exist")
    # end
    del course.requisites[requisite_course.id]
