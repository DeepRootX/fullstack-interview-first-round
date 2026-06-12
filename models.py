"""
Data types for the Round 1 interview.

These NamedTuples describe the shape of each record returned by the loaders in
data.py. Use them as the input types for the functions you implement in
solution.py.
"""

from datetime import datetime
from typing import NamedTuple


class Household(NamedTuple):
    household_id: str
    zip_code: int


class ViewershipEvent(NamedTuple):
    household_id: str
    network: str
    start_time: datetime
    end_time: datetime
