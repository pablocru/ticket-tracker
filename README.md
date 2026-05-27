# Ticket Tracker

I take exported tickets from systems like ServiceNow and transform them into Excel
spreadsheets that my team can actually work with.

## Philosophy

This is not a product. It's how I work.

You can use it too. Or just take ideas. That's why it's public.

## Usage

### Development setup

Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install `pip-tools`:

```bash
pip install pip-tools
```

Install development dependencies:

```bash
pip-compile requirements-dev.in
pip-sync requirements-dev.txt
```

> `requirements-dev.in` includes development tools and project dependencies:
>
> ```txt
> -r requirements.in
>
> pip-tools
> ```

Install production dependencies:

```bash
pip-compile requirements.in
pip-sync requirements.txt
```

### Code quality

This project uses [Ruff](https://docs.astral.sh/ruff/), a fast Python linter and
formatter, to keep the codebase consistent and clean.

#### Useful commands

Check for linting issues:

```bash
ruff check .
```

Automatically fix issues when possible:

```bash
ruff check . --fix
```

Format code:

```bash
ruff format .
```

Run both linting and formatting:

```bash
ruff check . --fix && ruff format .
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
python -m app
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
