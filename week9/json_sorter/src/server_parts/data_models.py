from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum


class SortFuncs(str, Enum):
    merge_sort = "merge_sort"
    quick_sort = "quick_sort"
    shaking_sort = "shaking_sort"
    insertion_sort="insertion_sort"


class InputData(BaseModel):
    sequence: list[int]
    sorting_selected: Optional[SortFuncs] = Field(default="shaking_sort")

    class Config:
        use_enum_values = True


class OutputData(BaseModel):
    sorted_sequence: list[int]
    time_taken: Optional[datetime.time]
