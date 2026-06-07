# Ticket Tracker

I take exported tickets from systems like ServiceNow and transform them into Excel
spreadsheets that my team can actually work with.

## Philosophy

This is not a product. It's how I work.

You can use it too. Or just take ideas. That's why it's public.

## Usage

### Development setup

This project uses `uv` for dependency and environment management.

Python version is defined in `pyproject.toml` (see `requires-python`) and will be
automatically handled by `uv` when syncing the project.

Please refer to the installation guide for `uv`:
<https://docs.astral.sh/uv/getting-started/installation/>

Install dependencies:

```bash
uv sync
```

This command automatically creates a `virtual environment` (if needed) and installs all
project and development dependencies.

You can optionally activate the environment manually:

```bash
source .venv/bin/activate
```

> Useful if you prefer not to use `uv run` for every command (e.g. running ruff or the
> application).

Managing dependencies with `uv`:

```bash
uv add <package>
uv remove <package>
```

> Use `--dev` for development dependencies

### Code quality

This project uses [Ruff](https://docs.astral.sh/ruff/), a fast Python linter and
formatter, to keep the codebase consistent and clean.

#### Useful commands

Check for linting issues:

```bash
uv run ruff check .
```

> Use `--fix` to automatically fix issues when possible.

Format code:

```bash
uv run ruff format .
```

### Run application

#### CSV input

The application reads the latest CSV file from:

```txt
data/input/
```

File naming convention:

```txt
tickets_YYYYMMDD_HHMMSS.csv
```

Example:

```txt
tickets_20260527_120000.csv
```

#### Run command

This project uses Python module execution as the entrypoint defined in:

```txt
./app/__main__.py
```

Run the application:

```bash
uv run python -m app
```

#### Logging

Logs are written to:

```txt
data/logs/application.log
```

## Contributing

If you notice any mistakes or have suggestions, I’m all ears. Feel free to [open an Issue
on GitHub](https://github.com/pablocru/ticket-tracker/issues) or submit a `Pull Request`.

### Contribution guidelines

1. `Fork` the repository and create a `new branch`.
1. Document your additions.
1. Use [Conventional Commits](https://www.conventionalcommits.org).
1. Submit a `Pull Request` with a clear description of your changes.

Thanks for helping improve this project.
