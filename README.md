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

> _The problem statement goes here. The interviewer will share it with you at
> the start of the session._

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

You don't need to write tests first (TDD-style) — but you do need to write
tests. Treat them as a first-class deliverable, not an afterthought.

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
