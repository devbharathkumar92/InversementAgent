# CI Workflow (activation template)

`ci.yml.example` is the GitHub Actions CI workflow for this repository.

It is stored **outside** `.github/workflows/` because the personal access token
used for the initial bootstrap does not have the `workflow` scope, so GitHub
rejects pushes that create/update files under `.github/workflows/`.

## Activating CI

Two options:

1. **Activate via the GitHub web UI** (no token scope needed):
   - Go to the repository → *Actions* → enable workflows (if prompted).
   - Create `.github/workflows/ci.yml` from the template via the GitHub UI.

2. **Use a token with `workflow` scope**:
   ```bash
   mkdir -p .github/workflows
   cp ci/workflows/ci.yml.example .github/workflows/ci.yml
   git add .github/workflows/ci.yml
   git commit -m "ci: activate CI workflow"
   git push
   ```

## What it runs

- Python 3.11 and 3.12
- `ruff check` and `ruff format --check` (src, tests, scripts)
- `mypy` (strict)
- `pytest -m unit` with coverage
- A secrets scan for common token patterns