# 🤝 Contributing to GLASTOR README Generator

First off, **thank you** for considering contributing to GLASTOR README Generator! It's people like you that make the open source community such an amazing place to learn, inspire, and create. 🎉

This document provides guidelines and instructions for contributing. Following these guidelines helps communicate that you respect the time of the developers managing and developing this open source project. In return, they should reciprocate that respect in addressing your issue, assessing changes, and helping you finalize your pull requests.

## 📑 Table of Contents

- [Code of Conduct](#-code-of-conduct)
- [Quick Start](#-quick-start-for-first-time-contributors)
- [Ways to Contribute](#-ways-to-contribute)
- [Development Setup](#️-development-setup)
- [Contribution Workflow](#-contribution-workflow)
- [Code Standards](#-code-standards)
- [Testing Guidelines](#-testing-guidelines)
- [Documentation](#-documentation)
- [Commit Conventions](#-commit-conventions)
- [Pull Request Process](#-pull-request-process)
- [Getting Help](#-getting-help)

---

## 📜 Code of Conduct

This project adheres to a Code of Conduct that all contributors are expected to follow. By participating, you are expected to uphold this code. Please read [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) before contributing.

**TL;DR**: Be respectful, inclusive, and professional. No harassment, discrimination, or toxic behavior will be tolerated.

---

## 🚀 Quick Start for First-Time Contributors

**Never contributed to open source before?** No problem! Here's a quick guide:

1. **🔍 Find an issue** labeled `good first issue` or `help wanted`
2. **💬 Comment** on the issue expressing your interest
3. **🍴 Fork** the repository
4. **🔧 Make** your changes
5. **✅ Test** everything works
6. **📤 Submit** a Pull Request

**Not sure where to start?** Check our [good first issues](https://github.com/glastor-dev/glastor-dev/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22).

---

## 💡 Ways to Contribute

There are many ways to contribute beyond writing code:

### 🐛 Report Bugs

Found a bug? Help us fix it by creating a detailed issue.

**Before submitting:**
- Search [existing issues](https://github.com/glastor-dev/glastor-dev/issues) to avoid duplicates
- Check if you're using the latest version

**When reporting, include:**
- **Clear title**: Brief description of the problem
- **Description**: Detailed explanation of the issue
- **Steps to reproduce**: Numbered steps that lead to the bug
- **Expected behavior**: What should happen
- **Actual behavior**: What actually happens
- **Environment**:
  - Python version: `python --version`
  - OS: Windows/Linux/macOS + version
  - Package version: `pip show glastor-readme-generator`
- **Screenshots**: If applicable
- **Error messages**: Full traceback/logs

**Example template:**
```markdown
**Bug**: Template rendering fails with custom variables

**Steps to reproduce:**
1. Create config with custom variable `author_email`
2. Run `glastor-readme generate`
3. Error occurs

**Expected**: README generated with custom variable
**Actual**: TypeError: 'NoneType' object is not subscriptable

**Environment:**
- Python 3.11.5
- Windows 11
- glastor-readme-generator 1.0.0

**Error log:**
```
Traceback (most recent call last):
  ...
```
```

### ✨ Suggest Features

Have an idea to make GLASTOR better? We'd love to hear it!

**Feature requests should include:**
- **Clear description**: What is the feature?
- **Use case**: Why is it needed? What problem does it solve?
- **Proposed solution**: How could it work?
- **Alternatives considered**: Other approaches you've thought about
- **Additional context**: Screenshots, examples, mockups

**Example:**
```markdown
**Feature**: Multi-language support for README templates

**Use case**: International projects need READMEs in multiple languages

**Proposed solution**: 
- Add `language` parameter to config
- Create language-specific template folders
- Auto-detect system language as default

**Alternatives**: 
- Manual translation (current workaround)
- Use external translation services

**Benefits**:
- Wider adoption
- Better accessibility
- Community templates in native languages
```

### 📝 Improve Documentation

Documentation is crucial! You can help by:

- Fixing typos or unclear explanations
- Adding examples and use cases
- Translating documentation
- Creating video tutorials
- Writing blog posts about the project

### 💬 Help Others

- Answer questions in [Issues](https://github.com/glastor-dev/glastor-dev/issues)
- Participate in [Discussions](https://github.com/glastor-dev/glastor-dev/discussions)
- Help review Pull Requests
- Share the project on social media

### 🎨 Design Contributions

- Create logos or graphics
- Design better template layouts
- Improve UI/UX of generated READMEs
- Suggest color schemes and styling

---

## 🛠️ Development Setup

### Prerequisites

- **Python**: 3.10 or higher
- **Git**: Latest version
- **Code editor**: VS Code, PyCharm, or your favorite editor

### Step-by-Step Setup

1. **Fork and Clone**

   ```bash
   # Fork on GitHub, then clone your fork
   git clone https://github.com/YOUR_USERNAME/glastor-dev.git
   cd glastor-dev
   ```

2. **Add Upstream Remote**

   ```bash
   # Keep your fork synced with the original repo
   git remote add upstream https://github.com/glastor-dev/glastor-dev.git
   git fetch upstream
   ```

3. **Create Virtual Environment**

   **Linux/macOS:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

   **Windows:**
   ```cmd
   python -m venv venv
   venv\Scripts\activate
   ```

   **Windows (PowerShell):**
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

4. **Install Dependencies**

   ```bash
   # Install project + dev dependencies
   pip install -r requirements.txt
   
   # Or if using pyproject.toml
   pip install -e ".[dev]"
   ```

5. **Install Pre-commit Hooks** (Recommended)

   ```bash
   pre-commit install
   ```

   This automatically runs linters/formatters before each commit.

6. **Verify Installation**

   ```bash
   # Run tests to ensure everything works
   pytest tests/ -v
   
   # Try running the tool
   glastor-readme --version
   ```

### Troubleshooting Setup

**Issue**: `python: command not found`
- **Solution**: Use `python3` on Linux/macOS or `py` on Windows

**Issue**: Permission errors on Linux/macOS
- **Solution**: Don't use `sudo`! Use virtual environments instead

**Issue**: Pre-commit hooks fail
- **Solution**: 
  ```bash
  pre-commit clean
  pre-commit install --install-hooks
  ```

**Issue**: Dependencies conflict
- **Solution**: Create fresh virtual environment
  ```bash
  deactivate
  rm -rf venv  # or rd /s venv on Windows
  python -m venv venv
  # Activate and reinstall
  ```

---

## 🔄 Contribution Workflow

### 1. Sync Your Fork

Before starting new work, sync with upstream:

```bash
git checkout main
git fetch upstream
git merge upstream/main
git push origin main
```

### 2. Create Feature Branch

Use descriptive branch names:

```bash
# Good branch names
git checkout -b feature/add-markdown-linter
git checkout -b fix/template-rendering-bug
git checkout -b docs/improve-installation-guide

# Bad branch names (too vague)
git checkout -b update
git checkout -b fix
git checkout -b changes
```

### 3. Make Your Changes

**Best practices:**
- **Make small, focused commits**: One logical change per commit
- **Write clear commit messages**: See [Commit Conventions](#-commit-conventions)
- **Test as you go**: Don't wait until the end to test
- **Follow code style**: Run linters frequently

### 4. Run Quality Checks

```bash
# Format code
ruff format .

# Check code style
ruff check .

# Run tests
pytest tests/ -v

# Check test coverage
pytest tests/ --cov=src --cov-report=html

# Run ALL checks (if pre-commit is configured)
pre-commit run --all-files
```

### 5. Commit Changes

```bash
# Stage changes
git add .

# Commit with conventional commit message
git commit -m "feat: add support for custom templates"
```

See [Commit Conventions](#-commit-conventions) for message format.

### 6. Push to Your Fork

```bash
git push origin feature/your-feature-name
```

### 7. Create Pull Request

Go to GitHub and create a PR from your fork to the main repository.

---

## 📏 Code Standards

### Python Style Guide

We follow [PEP 8](https://pep8.org/) with these additional conventions:

**Formatting**
- **Indentation**: 4 spaces (no tabs)
- **Line length**: 88 characters (Black default)
- **Quotes**: Double quotes for strings (`"text"`)
- **Imports**: Organized with `isort`

**Naming Conventions**
```python
# Variables and functions: snake_case
user_name = "John"
def calculate_total(): pass

# Classes: PascalCase
class TemplateRenderer: pass

# Constants: UPPER_SNAKE_CASE
MAX_RETRIES = 3
DEFAULT_ENCODING = "utf-8"

# Private members: _leading_underscore
def _internal_helper(): pass
```

**Type Hints**
```python
# Always use type hints for public functions
def generate_readme(
    config: dict[str, Any],
    output_path: Path | None = None
) -> str:
    """Generate README from configuration.
    
    Args:
        config: Configuration dictionary
        output_path: Optional output file path
        
    Returns:
        Generated README content
        
    Raises:
        ValueError: If config is invalid
    """
    pass
```

**Docstrings**
```python
# Use Google-style docstrings
def process_template(template: str, variables: dict) -> str:
    """Process Jinja2 template with variables.
    
    Renders the template string using provided variables and
    returns the processed output. Handles missing variables
    gracefully with defaults.
    
    Args:
        template: Jinja2 template string
        variables: Dictionary of template variables
        
    Returns:
        Processed template as string
        
    Raises:
        TemplateError: If template syntax is invalid
        
    Example:
        >>> process_template("Hello {{ name }}", {"name": "World"})
        'Hello World'
    """
    pass
```

### Code Organization

```
src/glastor_readme/
├── __init__.py          # Package initialization
├── cli.py               # Command-line interface
├── config.py            # Configuration handling
├── generator.py         # Core generation logic
├── templates/           # Built-in templates
│   ├── __init__.py
│   ├── basic.md
│   └── professional.md
└── utils/               # Helper functions
    ├── __init__.py
    ├── validators.py
    └── formatters.py
```

**Best practices:**
- One class per file for large classes
- Group related functions in modules
- Use `__init__.py` to expose public API
- Keep imports at the top, organized by:
  1. Standard library
  2. Third-party packages
  3. Local imports

### Error Handling

```python
# Use specific exceptions
from typing import Optional

class ConfigError(Exception):
    """Raised when configuration is invalid."""
    pass

def load_config(path: Path) -> dict:
    """Load configuration from file.
    
    Raises:
        ConfigError: If file doesn't exist or is invalid JSON
    """
    if not path.exists():
        raise ConfigError(f"Config file not found: {path}")
    
    try:
        return json.loads(path.read_text())
    except json.JSONDecodeError as e:
        raise ConfigError(f"Invalid JSON in config: {e}") from e
```

---

## 🧪 Testing Guidelines

### Writing Tests

**Test file structure:**
```
tests/
├── __init__.py
├── conftest.py          # Shared fixtures
├── test_cli.py          # CLI tests
├── test_generator.py    # Core logic tests
├── test_templates.py    # Template tests
└── fixtures/            # Test data
    ├── config.json
    └── sample_readme.md
```

**Test naming:**
```python
# Use descriptive test names
def test_generate_readme_with_valid_config():
    """Should generate README when config is valid."""
    pass

def test_generate_readme_raises_error_when_template_missing():
    """Should raise TemplateNotFoundError when template doesn't exist."""
    pass

# Group related tests in classes
class TestTemplateRenderer:
    def test_render_with_all_variables(self):
        pass
    
    def test_render_with_missing_variables_uses_defaults(self):
        pass
    
    def test_render_raises_error_on_invalid_syntax(self):
        pass
```

**Test structure (AAA pattern):**
```python
def test_config_loader():
    # Arrange: Set up test data
    config_data = {"project_name": "Test", "author": "John"}
    config_file = tmp_path / "config.json"
    config_file.write_text(json.dumps(config_data))
    
    # Act: Execute the code under test
    result = load_config(config_file)
    
    # Assert: Verify the results
    assert result["project_name"] == "Test"
    assert result["author"] == "John"
```

### Running Tests

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_generator.py

# Run specific test
pytest tests/test_generator.py::test_generate_readme

# Run with coverage
pytest --cov=src --cov-report=html
# Open htmlcov/index.html to see coverage report

# Run only fast tests (skip slow integration tests)
pytest -m "not slow"

# Run in parallel (faster)
pytest -n auto
```

### Test Coverage Goals

- **Minimum**: 80% coverage for new code
- **Target**: 90% coverage overall
- **Critical paths**: 100% coverage (core generation logic)

**What to test:**
- ✅ Public functions and methods
- ✅ Error handling and edge cases
- ✅ Different input combinations
- ✅ Integration between modules

**What NOT to test:**
- ❌ Third-party library internals
- ❌ Trivial getters/setters
- ❌ Configuration files (validate them instead)

---

## 📚 Documentation

### Documentation Types

1. **Code Documentation** (Docstrings)
   - Every public function/class
   - Google-style format
   - Include examples

2. **User Documentation** (README.md)
   - Installation instructions
   - Usage examples
   - FAQ section

3. **API Documentation** (Auto-generated)
   - Sphinx or MkDocs
   - Generated from docstrings

4. **Contributing Guide** (This file)
   - How to contribute
   - Development setup
   - Standards and conventions

### Documentation Standards

**Good docstring:**
```python
def merge_configs(base: dict, override: dict) -> dict:
    """Merge two configuration dictionaries.
    
    Performs deep merge where override values take precedence.
    Lists are concatenated, nested dicts are merged recursively.
    
    Args:
        base: Base configuration dictionary
        override: Override configuration dictionary
        
    Returns:
        Merged configuration dictionary
        
    Example:
        >>> base = {"colors": ["red"], "size": 10}
        >>> override = {"colors": ["blue"], "name": "Test"}
        >>> merge_configs(base, override)
        {'colors': ['red', 'blue'], 'size': 10, 'name': 'Test'}
    """
```

**Update documentation when:**
- Adding new features
- Changing behavior
- Deprecating functionality
- Fixing bugs that affect usage

---

## 📝 Commit Conventions

We use [Conventional Commits](https://www.conventionalcommits.org/) for clear and semantic commit messages.

### Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- **feat**: New feature for the user
- **fix**: Bug fix for the user
- **docs**: Documentation changes
- **style**: Code formatting (no logic change)
- **refactor**: Code refactoring (no behavior change)
- **perf**: Performance improvements
- **test**: Adding or updating tests
- **build**: Build system or dependencies
- **ci**: CI/CD configuration changes
- **chore**: Other changes (tooling, etc.)

### Examples

**Good commits:**
```bash
feat(templates): add professional README template

- New template with sections for features, installation, usage
- Includes badges and table of contents
- Supports customization via config

Closes #42

---

fix(generator): handle missing template variables gracefully

Previously crashed with KeyError when variable was missing.
Now uses empty string as default value.

Fixes #156

---

docs: update installation instructions for Windows

Added PowerShell instructions and troubleshooting section.

---

refactor(config): extract validation into separate module

No behavior change. Improves code organization and testability.
```

**Bad commits (don't do this):**
```bash
update stuff
fix bug
WIP
asdfasdf
Final commit (for real this time)
```

### Commit Message Tips

- **Subject line**:
  - Max 50 characters
  - Start with lowercase
  - No period at end
  - Imperative mood ("add" not "added" or "adds")

- **Body** (optional):
  - Wrap at 72 characters
  - Explain what and why, not how
  - Separate from subject with blank line

- **Footer** (optional):
  - Reference issues: `Closes #123`, `Fixes #456`
  - Breaking changes: `BREAKING CHANGE: description`

---

## 🔀 Pull Request Process

### Before Submitting

- [ ] **Tests pass**: `pytest tests/ -v`
- [ ] **Code formatted**: `ruff format .`
- [ ] **Linting clean**: `ruff check .`
- [ ] **Documentation updated**: If adding features
- [ ] **CHANGELOG updated**: Add entry for your change
- [ ] **Commits are clean**: Follow commit conventions

### PR Template

When creating a PR, include:

```markdown
## Description
Brief description of what this PR does.

## Type of Change
- [ ] Bug fix (non-breaking change that fixes an issue)
- [ ] New feature (non-breaking change that adds functionality)
- [ ] Breaking change (fix or feature that breaks existing functionality)
- [ ] Documentation update

## Related Issues
Closes #issue_number

## How Has This Been Tested?
Describe the tests you ran and how to reproduce.

## Checklist
- [ ] Tests pass locally
- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] No new warnings
- [ ] Added tests for new functionality

## Screenshots (if applicable)
```

### Review Process

1. **Automated Checks**: CI runs tests automatically
2. **Code Review**: Maintainer reviews your code
3. **Revisions**: Address feedback if requested
4. **Approval**: Once approved, PR will be merged
5. **Recognition**: You'll be added to contributors list!

### PR Guidelines

**Do:**
- ✅ Keep PRs focused (one feature/fix per PR)
- ✅ Write clear descriptions
- ✅ Respond to feedback promptly
- ✅ Be patient and respectful

**Don't:**
- ❌ Submit huge PRs (>500 lines)
- ❌ Mix multiple changes in one PR
- ❌ Force push after review starts
- ❌ Take criticism personally

### After PR is Merged

```bash
# Sync your fork with upstream
git checkout main
git pull upstream main
git push origin main

# Delete your feature branch (optional)
git branch -d feature/your-feature
git push origin --delete feature/your-feature
```

---

## 🆘 Getting Help

### Where to Ask

- **💬 GitHub Discussions**: General questions, ideas, show & tell
- **🐛 GitHub Issues**: Bug reports, feature requests
- **📧 Email**: glastor.info@gmail.com (for private matters)
- **💬 Telegram**: [@zerhocool](https://t.me/zerhocool) (quick questions)

### Getting Better Answers

**Good question:**
```markdown
I'm trying to use custom templates but getting "Template not found" error.

**What I tried:**
1. Created `templates/custom.md` in project root
2. Set `template: custom.md` in config.json
3. Ran `glastor-readme generate`

**Error:**
```
TemplateNotFoundError: custom.md not found in search paths
```

**Environment:**
- Python 3.11
- glastor-readme-generator 1.0.0
- Windows 11

**Question:** Where should I place custom templates?
```

**Bad question:**
```
It doesn't work. Help!
```

---

## 🎉 Recognition

Contributors are recognized in several ways:

- **README.md**: Listed in Contributors section
- **CHANGELOG.md**: Credited in release notes
- **GitHub**: Automatic contributor badge
- **Social Media**: Major contributions are announced

### Hall of Fame

Special thanks to our top contributors! 🌟

Want to see your name here? Start contributing today!

---

## 📜 License

By contributing to GLASTOR README Generator, you agree that your contributions will be licensed under the project's [GPL v3.0 License](LICENSE).

---

## 🙏 Final Words

Thank you for taking the time to contribute! Every contribution, no matter how small, makes a difference. You're helping make documentation better for developers everywhere.

**Questions about this guide?** Open an issue or reach out directly.

**Ready to start?** Check out the [good first issues](https://github.com/glastor-dev/glastor-dev/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)!

Happy coding! 🚀

---

**Maintained with ❤️ by [@glastor-dev](https://github.com/glastor-dev)**  
**Last updated**: 2025-12-28