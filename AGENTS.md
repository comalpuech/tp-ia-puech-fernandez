# Bac à sable — OpenCode

## Project structure

- **Single module**: `toolbox.py` — three functions: `is_palindrome`, `word_frequency`, `celsius_to_fahrenheit`
- **Tests**: `test_toolbox.py` — pytest, imports from `toolbox` directly
- **Two venvs**: `.venv` and `.venv-1` (both ignored). Use `python -m venv .venv` to create.

## Commands

```bash
python -m venv .venv && source .venv/bin/activate          # Linux/macOS
python -m venv .venv && .venv\Scripts\activate              # Windows
pip install pytest
pytest
```

## Gotchas

- `is_palindrome` strips case but **not spaces** — `test_is_palindrome_with_spaces` fails intentionally.
- `word_frequency` and `celsius_to_fahrenheit` raise `NotImplementedError` — stubs to be implemented.
- This is a learning exercise, not a production repo. Keep changes minimal.
