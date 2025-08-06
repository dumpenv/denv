# denv
A Tool To Store Environment Variables

## Prerequisites

- Python 3.13.0 or higher
- [uv](https://docs.astral.sh/uv/) - A fast Python package installer and resolver

### Installing uv

If you don't have uv installed, you can install it using one of the following methods:

**macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**
```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Using pip:**
```bash
pip install uv
```

## Local Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd denv
```

<!-- ### 2. Install Dependencies

The project uses uv for dependency management. Install all dependencies using:

```bash
uv sync
``` 

This will:
- Create a virtual environment automatically
- Install Python 3.13.0 (as specified in [.python-version](.python-version))
- Install all dependencies from [pyproject.toml](pyproject.toml)

### 3. Activate the Virtual Environment

```bash
uv shell
```

Alternatively, you can run commands directly with uv without activating the shell:

```bash
uv run python main.py
``` -->

### 4. Run the Application

Start the FastAPI development server:

```bash
uv run uvicorn main:app --reload
```

The application will be available at:
- **API**: http://localhost:8000
- **Interactive API docs**: http://localhost:8000/docs
- **Alternative docs**: http://localhost:8000/redoc



## Development

### Adding New Dependencies

To add new dependencies to the project:

```bash
uv add <package-name>
```

For development dependencies:

```bash
uv add --dev <package-name>
```

### Running Commands

You can run any Python command using uv:

```bash
uv run python <script.py>
uv run pytest  # if you add pytest later
uv run black .  # if you add black for formatting
```


## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.