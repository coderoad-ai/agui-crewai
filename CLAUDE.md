# Project guidelines

Python code lives in `ag-ui-restaurant-agent/` (CrewAI backend), the frontend in `ag-ui-restaurant-frontend/`.

## Python rules (flag violations in code review)

- Never use a mutable default argument (`def f(x, cache={})`). Use `None` and create the object inside the function.
- Never use a bare `except:`. Catch the specific exception type.
- Do not use `print()` in library or agent code. Use the `logging` module with lazy formatting: `logger.debug("x: %s", x)`.
- All new functions must have type hints on parameters and return values.
- Do not add unused functions or dead code.
- New helper functions must come with a test.

## Review guidance

- Treat the rules above as required, not optional. Report each violation as an issue.
