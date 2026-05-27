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

## Contributing

If you notice any mistakes or have suggestions, I’m all ears. Feel free to [open an Issue
on GitHub](https://github.com/pablocru/ticket-tracker/issues) or submit a `Pull Request`.

### Contribution guidelines

1. `Fork` the repository and create a `new branch`.
1. Document your additions.
1. Use [Conventional Commits](https://www.conventionalcommits.org).
1. Submit a `Pull Request` with a clear description of your changes.

Thanks for helping improve this project.
