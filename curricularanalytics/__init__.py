__version__ = "1.4.0"

from .data_handler import read_csv, write_csv
from .degree_plan_creation import bin_filling, create_degree_plan
from .graph_algs import (
    all_paths,
    dfs,
    gad,
    longest_path,
    longest_paths,
    reach,
    reach_subgraph,
    reachable_from,
    reachable_from_subgraph,
    reachable_to,
    reachable_to_subgraph,
    topological_sort,
)
from .types.course import AbstractCourse, Course, CourseCollection, course_id
from .types.course_catalog import CourseCatalog
from .types.curriculum import BasicMetrics, Curriculum, basic_statistics, homology
from .types.data_types import (
    EdgeClass,
    Requisite,
    System,
    back_edge,
    co,
    cross_edge,
    forward_edge,
    pre,
    quarter,
    semester,
    strict_co,
    tree_edge,
)
from .types.degree_plan import DegreePlan, Term, TermMetrics
from .types.degree_requirements import (
    AbstractRequirement,
    CourseSet,
    Grade,
    RequirementSet,
    from_grade,
    grade,
)
from .types.learning_outcome import LearningOutcome
from .types.simulation import Simulation
from .types.student import Student, simple_students
from .types.student_record import CourseRecord, StudentRecord
from .types.transfer_articulation import TransferArticulation

__all__ = [  # "AA",
    # "AAS",
    # "AS",
    "AbstractCourse",
    "AbstractRequirement",
    # "BA",
    # "BS",
    "Course",
    "CourseCollection",
    "CourseCatalog",
    "CourseRecord",
    "CourseSet",
    "Curriculum",
    "DegreePlan",
    "EdgeClass",
    # "Enrollment",
    "Grade",
    "LearningOutcome",
    # "PassRate",
    "RequirementSet",
    "Requisite",
    "Student",
    "StudentRecord",
    "Simulation",
    "System",
    "Term",
    "TransferArticulation",
    "all_paths",
    "back_edge",
    "basic_statistics",
    "bin_filling",
    "co",
    "course_id",
    "create_degree_plan",
    "cross_edge",
    "dfs",
    "forward_edge",
    "gad",
    "grade",
    "homology",
    "longest_path",
    "longest_paths",
    # "pass_table",
    # "passrate_table",
    "pre",
    "quarter",
    "reach",
    "reach_subgraph",
    "reachable_from",
    "reachable_from_subgraph",
    "reachable_to",
    "reachable_to_subgraph",
    "read_csv",
    "semester",
    # "set_passrates",
    # "set_passrate_for_course",
    # "set_passrates_from_csv",
    "simple_students",
    # "simulation_report",
    "strict_co",
    "topological_sort",
    "tree_edge",
    "write_csv",
    # "csv_stream",
    "from_grade",
    "TermMetrics",
    "BasicMetrics",
]
