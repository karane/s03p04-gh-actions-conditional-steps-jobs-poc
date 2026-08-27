# s03p04-gh-actions-conditional-steps-jobs-poc

`if:` conditions on jobs/steps using `success()`, `failure()`, `always()`, `cancelled()`, and skipping jobs based on `github.event_name`/`github.ref`.

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run tests

```bash
python3 -m pytest tests/ -v
```

## Run the workflow

Push to `main` or open a PR — `.github/workflows/conditional-steps-jobs.yml`'s `build` job runs tests, then a step for each of `success()`/`failure()`/`always()`/`cancelled()`, plus one gated on `github.event_name`/`github.ref`. The `deploy` job only runs at all for direct pushes to `main`.

See [BLOG.md](./BLOG.md) for a full walkthrough.
