# Fullstack Engineer Interview — Round 1

Welcome! This is a ~45 minute coding exercise. Don't worry about finishing
everything — we're more interested in how you think than in a perfect solution.

## The environment

This repo is designed to be opened as a **GitHub Codespace**. When you open it,
the devcontainer will:
- Boot a Python 3.12 environment
- Install `pytest` (see `requirements.txt`)

You should not need to install anything yourself. If `pytest` isn't on your
path when the Codespace finishes building, run `pip install -r requirements.txt`.

## The problem

Tunnl has just received a new feed of Household TV Viewership data. We would like 
you to help us parse this data so we can gain insights into what households are 
watching. This will help us advise our clients where they should be running their
ads. 

# Part 1

We want to know our weekly **reach** — what fraction of the panel watched
any TV at all over the past week.

You're given two input files:

- `households.csv` — the universe of NY households we measure. Columns:
  `household_id`, `dma_id`.
- `viewership.csv` — one row per continuous tune-in event for the week of
  **2024-01-15 through 2024-01-21**. Columns: `household_id`, `network`,
  `start_time`, `end_time`.

The data is parsed for you. Use `load_households()` and `load_viewership()`
from `data.py` to get back `list[Household]` and `list[ViewershipEvent]`
(both defined in `models.py`). You don't need to write any CSV-parsing code.

**Your task:** implement `compute_reach()` in `solution.py` so it returns
the reach as a `float` between `0.0` and `1.0`.

You can run `solution.py` to see your result against the real data:

```python
# add at the bottom of solution.py
if __name__ == "__main__":
    from data import load_households, load_viewership
    households = load_households()
    viewership = load_viewership()
    print(f"Weekly reach: {compute_reach(households, viewership):.1%}")
```

Write your tests in `tests/` against `compute_reach()` directly, using
hand-built lists of `Household` and `ViewershipEvent` records — that lets
you cover edge cases without depending on the real CSVs.

# Part 2 and beyond...
Your interviewer will reveal the next steps once we are finished with Part 1!

You'll implement your solution in `solution.py` (and any additional files you
want to create).

## How we'll evaluate this

We're looking at **both your implementation and your tests**. Specifically:

- **Correctness** — does your solution actually work, including on edge cases?
- **Test design** — what cases did you choose to cover, and what does that say
  about how you think about correctness? A good test suite often reveals more
  about an engineer's thinking than the implementation does.
- **Code clarity** — would someone else on the team be able to read and modify
  this in six months?
- **How you work** — talking through your decisions, asking clarifying
  questions, and reasoning out loud are all encouraged.

You don't need to write tests first — but we would like you to write
tests.

## Running tests

From the repo root:

```bash
pytest                       # run everything
pytest -v                    # verbose
pytest tests/test_foo.py     # one file
pytest -k "name_substring"   # filter by test name
```

A sanity-check test in `tests/test_example.py` confirms pytest is wired up.
You can delete it or replace it once you start writing real tests.

## Ground rules

- **No AI assistants.** Copilot and other AI extensions are disabled in this
  devcontainer. Please don't use ChatGPT, Claude, or similar tools in another
  tab — we want to see your thinking, not a model's.
- Anything in the Python standard library is fair game.
- You can search the web for language/library documentation. Looking up the
  exact signature of `itertools.groupby` is fine; pasting a solution from
  Stack Overflow is not.
- Ask us anything! Clarifying questions are encouraged and aren't held against
  you.

Good luck!
