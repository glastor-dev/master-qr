# Contributing to GLASTOR README Generator

Thank you for considering contributing to GLASTOR README Generator! 🎉

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Your environment (Python version, OS)

### Suggesting Features

Feature suggestions are welcome! Please create an issue with:
- Clear description of the feature
- Use cases and benefits
- Potential implementation approach

### Pull Requests

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```

3. **Make your changes**
   - Follow the existing code style
   - Add tests for new functionality
   - Update documentation as needed

4. **Run tests**
   ```bash
   python -m pytest tests/ -v
   ```

   On Windows you may need:
   ```bash
   py -m pytest tests/ -v
   ```

5. **Run lint/format (recommended)**
   ```bash
   ruff check .
   ruff format .
   ```

   Or run everything via pre-commit:
   ```bash
   pre-commit run --all-files
   ```

6. **Commit your changes**
   ```bash
   git commit -m "feat: add amazing feature"
   ```

   Use conventional commits:
   - `feat:` - New feature
   - `fix:` - Bug fix
   - `docs:` - Documentation changes
   - `test:` - Test additions/changes
   - `refactor:` - Code refactoring

7. **Push to your fork**
   ```bash
   git push origin feature/amazing-feature
   ```

8. **Create a Pull Request**

PR tips:
- Keep PRs small and focused (one change-set per PR)
- Include a short description of what changed and how to test it

Note: DCO sign-off is NOT required for this repository.

## Development Setup

1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies (includes dev tools like pytest/ruff/black/pre-commit):
   ```bash
   pip install -r requirements.txt
   ```

Optional (recommended): enable pre-commit hooks
```bash
pre-commit install
```

## Code Style

- Follow PEP 8
- Use type hints where appropriate
- Document functions with docstrings
- Keep functions focused and small

## Testing

- Write tests for new features
- Maintain test coverage above 80% when practical
- Run tests before submitting PR

## Documentation

- Update README.md for user-facing changes
- Add docstrings for new functions/classes
- Update CHANGELOG.md with your changes

## Questions?

Feel free to reach out via:
- GitHub Issues
- Email: glastor.info@gmail.com
- Telegram: @zerhocool

Thank you for contributing! 🚀
