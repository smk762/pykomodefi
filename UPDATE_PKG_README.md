# Package Update and PyPI Publishing Guide

This guide outlines the steps to update and publish the pykomodefi package to PyPI.

## Prerequisites

- Poetry installed and configured
- PyPI account with credentials or API token
- All tests passing
- Updated version number in `pyproject.toml`

## Authentication Setup

### Option 1: API Tokens (Recommended)

**For PyPI:**
1. Go to [pypi.org](https://pypi.org) and log in to your account
2. Navigate to Account Settings → API Tokens
3. Click "Add API token"
4. Choose scope: "Entire account" or "Project: pykomodefi" (if it exists)
5. Copy the generated token (starts with `pypi-`)
6. Configure Poetry with the token:

```bash
poetry config pypi-token.pypi pypi-AgEIcHlwaS5vcmcCJGYourTokenHere
```

**For TestPyPI:**
1. Go to [test.pypi.org](https://test.pypi.org) and log in
2. Follow the same steps as above
3. Configure Poetry for TestPyPI:

```bash
poetry config pypi-token.testpypi pypi-AgEIcHlwaS5vcmcCJGYourTestTokenHere
```

### Verify Authentication

Test your authentication setup:

```bash
# Test with a dry run (doesn't actually publish)
poetry publish --dry-run

# For TestPyPI
poetry publish -r testpypi --dry-run
```

## Step-by-Step Publishing Process

### 1. Build the Package

```bash
poetry build
```

This creates distribution files in the `dist/` directory (both `.tar.gz` and `.whl` files).

### 2. Test on TestPyPI First (Recommended)

Before publishing to the real PyPI, test on TestPyPI:

```bash
# Configure TestPyPI (one-time setup)
poetry config repositories.testpypi https://test.pypi.org/legacy/

# Publish to TestPyPI
poetry publish -r testpypi
```

### 3. Test Installation from TestPyPI

```bash
# Test install from TestPyPI
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ pykomodefi==0.2.5
```

Replace `0.2.5` with your current version number.

### 4. Publish to Real PyPI

Once testing looks good:

```bash
poetry publish
```

Ensure you have authentication set up (see "Authentication Setup" section above).

### 7. Verify the Upload

- Check [pypi.org/project/pykomodefi/](https://pypi.org/project/pykomodefi/)
- Test installation: `pip install pykomodefi==0.2.5`
- Verify the new version appears correctly

### 8. Tag the Release in Git

```bash
git add .
git commit -m "Release v0.2.5: Update to Python 3.12, latest dependencies"
git tag v0.2.5
git push origin main --tags
```

### 9. Clean Up (Optional)

```bash
# Remove build artifacts if desired
rm -rf dist/ build/ *.egg-info/
```

## Pre-Publishing Checklist

Before publishing, ensure:

- ✅ Version number updated in `pyproject.toml`
- ✅ All dependencies updated to latest compatible versions
- ✅ Code formatted with Black: `poetry run black pykomodefi/`
- ✅ Tests passing: `poetry run pytest tests/ -v`
- ✅ README.md updated with any new features or changes
- ✅ CHANGELOG or release notes prepared (if applicable)

## Common Issues and Solutions

### Authentication Issues
- Ensure you have valid PyPI credentials
- Use API tokens instead of username/password for better security
- Check that your token has the correct permissions

### Version Conflicts
- Make sure the version number in `pyproject.toml` is higher than the current PyPI version
- Follow semantic versioning (MAJOR.MINOR.PATCH)

### Build Issues
- Run `poetry install` to ensure all dependencies are up to date
- Clear any previous build artifacts: `rm -rf dist/ build/`

### Test Failures
- Ensure all tests pass locally before publishing
- Set up proper test configuration (`.env` file in `tests/` directory)
- Remember that connection errors are expected when MM2 is not running

## Version History

- `0.2.5`: Updated to Python 3.12, latest dependencies, improved test setup
- `0.2.4`: Previous stable version

## Security Notes

- Use API tokens instead of passwords when possible
- Never commit API tokens to version control
- Consider using environment variables for sensitive configuration
