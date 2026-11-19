# california-drought-scrapers

Scrapers and processing notebooks that feed the Los Angeles Times' [California drought tracker](https://www.latimes.com/projects/california-drought-status-maps-water-usage/) ([datadesk/drought-tracker](https://github.com/datadesk/drought-tracker)). Each one runs on a schedule in GitHub Actions and commits its output back to `main`.

## Setup

Install the Python dependencies:

```bash
pipenv sync
```

`pipenv sync` installs exactly the versions pinned in `Pipfile.lock`, which is what the GitHub Actions workflows run. Avoid `pipenv install` with no arguments for setup, since it can re-lock and quietly upgrade packages.

To add or upgrade a package, use `pipenv install <package>` (or edit the `Pipfile` and run `pipenv lock`), then commit both `Pipfile` and `Pipfile.lock`. The workflows only ever install from the lock file, so a change to the `Pipfile` without a matching lock won't reach them.

## Running the scrapers

Each dataset has a Makefile target, the same one its workflow calls:

| Target | Workflow |
|---|---|
| `make reservoirsdata` | `daily-reservoirs.yml` |
| `make snowpackdata` | `snowpack.yml` |
| `make precipitationdata` | `precip.yml` |
| `make droughtmonitordata` | `us-drought-monitor.yml` |
| `make urbanwaterusedata` | `monthly-reports.yml` (after `urban-water-use/scrape.py`) |
