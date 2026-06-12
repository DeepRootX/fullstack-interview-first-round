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

Tunnl has just received a new feed of **Household TV Viewership** data, and we'd
like your help turning it into insights about what NY households are watching —
the kind of insight we use to advise clients on where and when to run their ads.

You'll be working with two data sets:

- **The household universe** (`households.csv`) — every NY household we measure,
  each with its zip code.
  Columns: 
- **A week of viewership** (`viewership.csv`) — one row per continuous tune-in
  event for the week of **2024-01-15 through 2024-01-21**: which household
  watched which network, and the start/end time of each session.

Both files are already parsed for you (see "The data" under Part 1 below) — you
won't need to write any CSV parsing.

This is a **multi-part exercise** that starts simple and builds from there. Each
part is revealed once you finish the one before it, so focus on the part in front
of you rather than designing for what might come later. Let's start with **Part 1**.

# Part 1

We want you to calculate our weekly **reach** — what percentage of the total NY households
watched any amount of TV during this time period?

You're given two input files:

- `households.csv` — the universe of NY households we measure. Columns:
  `household_id`, `zip_code`.
- `viewership.csv` — one row per continuous tune-in event for the week of
  **2024-01-15 through 2024-01-21**. Columns: `household_id`, `network`,
  `start_time`, `end_time`.

The data is parsed for you. Use `load_households()` and `load_viewership()`
from `data.py` to get back `list[Household]` and `list[ViewershipEvent]`
(both defined in `models.py`). You don't need to write any CSV-parsing code.
Feel free to look through the csv files to view the raw data.

**Your task:** implement `compute_reach()` in `solution.py` so it returns
the reach as a `float` between `0.0` and `1.0`.

You can run `solution.py` to see your result against the real data. The `__main__`
block has already been defined to run your Part 1 function passing in the CSV data
for households and viewership.

If you'd like, you can write extra tests in `tests/` against `compute_reach()` 
directly, using hand-built lists of `Household` and `ViewershipEvent` records — that lets
you cover edge cases without depending on the real CSVs.

# Part 2 and beyond...
Your interviewer will reveal the next steps once we are finished with Part 1!

## How we'll evaluate this

We're looking at **both your implementation and your tests**. Specifically:

- **Correctness** — does your solution actually work, including on edge cases?
- **How you work** — talking through your decisions, asking clarifying
  questions, and reasoning out loud are all encouraged.
- **Code clarity** — would someone else on the team be able to read and modify
  this in six months?


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

## Running tests

From the repo root:

```bash
pytest                       # run everything
pytest -v                    # verbose
pytest tests/test_foo.py     # one file
pytest -k "name_substring"   # filter by test name
```