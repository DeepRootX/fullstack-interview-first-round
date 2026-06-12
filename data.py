"""
Loaders for the interview input CSVs. Call these to get parsed, ready-to-use
lists of records — you do not need to write any CSV-parsing code yourself.

    from data import load_households, load_viewership

    households = load_households()       # list[Household]
    viewership = load_viewership()       # list[ViewershipEvent]
"""

import csv
from datetime import datetime
from pathlib import Path

from models import Household, ViewershipEvent

_DATA_DIR = Path(__file__).parent


def load_households() -> list[Household]:
    """Load the NY panel from households.csv."""
    households = []
    with open(_DATA_DIR / "households.csv") as f:
        for row in csv.DictReader(f):
            households.append(
                Household(
                    household_id=row["household_id"],
                    zip_code=row["zip_code"],
                )
            )
    return households


def load_viewership() -> list[ViewershipEvent]:
    """Load this week's viewership events from viewership.csv."""
    events = []
    with open(_DATA_DIR / "viewership.csv") as f:
        for row in csv.DictReader(f):
            events.append(
                ViewershipEvent(
                    household_id=row["household_id"],
                    network=row["network"],
                    start_time=datetime.fromisoformat(row["start_time"]),
                    end_time=datetime.fromisoformat(row["end_time"]),
                )
            )
    return events
