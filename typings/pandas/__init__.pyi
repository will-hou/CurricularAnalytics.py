from typing import (
    Generic,
    Hashable,
    Iterable,
    Literal,
    Sequence,
    Tuple,
    TypeVar,
)

from pandas._libs import lib
from pandas._typing import (
    FilePath,
)

__all__ = ["DataFrame", "Series", "read_csv"]

T = TypeVar("T")

class DataFrame(Generic[T]):
    columns: Sequence[Hashable]
    shape: Tuple[int, int]

    def iterrows(self) -> Iterable[tuple[Hashable, Series[T]]]: ...
    def nunique(self) -> Series[Hashable]: ...

class Series(Generic[T]):
    def __getitem__(self, key: str) -> T: ...

# default case -> DataFrame
def read_csv(
    filepath_or_buffer: FilePath,
    *,
    delimiter: str | None | lib.NoDefault = ...,
    header: int | Sequence[int] | None | Literal["infer"] = ...,
    nrows: int | None = ...,
) -> DataFrame[Hashable]: ...
def concat(
    objs: Iterable[DataFrame[T]],
    *,
    axis: Literal[0, 1, "index", "columns"] = 0,
) -> DataFrame[T]: ...
