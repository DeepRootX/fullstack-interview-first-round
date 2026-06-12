"""
Your solution goes here.
"""

from data import load_households, load_viewership
from models import Household, ViewershipEvent

# Part 1
def compute_reach(households: list[Household], viewership: list[ViewershipEvent]) -> float:
    # TODO: Implement me!
    return 0.0


if __name__ == "__main__":
    households = load_households()
    viewership = load_viewership()

    # Part 1 Output
    print(f"Weekly reach: {compute_reach(households, viewership):.1%}")

    # Part 2 and beyond...
    # TODO: add calls here