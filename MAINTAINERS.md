# Yamlify-Me Maintainer's Guide

This document provides instructions for maintainers of the Yamlify-Me package, including how to publish new versions to PyPI.

## Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/JensKlimke/yamlify.git
   cd yamlify
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install the package in development mode with development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

## Release Process

### 1. Update Version

1. Edit `pyproject.toml` and update the version number in the `[project]` section:
   ```toml
   [project]
   name = "yamlify-me"
   version = "x.y.z"  # Update this line
   ```

   Follow semantic versioning:
   - Increment the major version (x) for incompatible API changes
   - Increment the minor version (y) for added functionality in a backward-compatible manner
   - Increment the patch version (z) for backward-compatible bug fixes

2. Commit the version change:
   ```bash
   git add pyproject.toml
   git commit -m "Bump version to x.y.z"
   ```

### 2. Run Tests

Ensure all tests pass before releasing:

```bash
python -m unittest discover tests
```

### 3. Build the Package

Build both the source distribution and wheel:

```bash
python -m pip install --upgrade build
python -m build
```

This will create the distribution files in the `dist/` directory.

### 4. Publish to PyPI

1. Install Twine if not already installed:
   ```bash
   pip install --upgrade twine
   ```

2. Upload to TestPyPI first to verify everything works:
   ```bash
   twine upload --repository-url https://test.pypi.org/legacy/ dist/*
   ```

3. Install from TestPyPI to verify the package works:
   ```bash
   pip install --index-url https://test.pypi.org/simple/ --no-deps yamlify-me
   ```

4. Upload to the real PyPI:
   ```bash
   twine upload dist/*
   ```

### 5. Create a Git Tag

1. Create a tag for the new version:
   ```bash
   git tag -a vx.y.z -m "Version x.y.z"
   ```

2. Push the tag to GitHub:
   ```bash
   git push origin vx.y.z
   ```

### 6. Create a GitHub Release

1. Go to the [GitHub releases page](https://github.com/JensKlimke/yamlify/releases)
2. Click "Draft a new release"
3. Select the tag you just created
4. Add release notes describing the changes in this version
5. Publish the release

## Continuous Integration (Future Enhancement)

Setting up GitHub Actions for automated testing and publishing is recommended:

1. Create a `.github/workflows/python-package.yml` file for testing:
   ```yaml
   name: Python Package

   on:
     push:
       branches: [ main ]
     pull_request:
       branches: [ main ]

   jobs:
     test:
       runs-on: ubuntu-latest
       strategy:
         matrix:
           python-version: [3.7, 3.8, 3.9, "3.10"]

       steps:
       - uses: actions/checkout@v2
       - name: Set up Python ${{ matrix.python-version }}
         uses: actions/setup-python@v2
         with:
           python-version: ${{ matrix.python-version }}
       - name: Install dependencies
         run: |
           python -m pip install --upgrade pip
           pip install -e ".[dev]"
       - name: Run tests
         run: |
           python -m unittest discover tests
   ```

2. Create a `.github/workflows/python-publish.yml` file for publishing:
   ```yaml
   name: Upload Python Package

   on:
     release:
       types: [created]

   jobs:
     deploy:
       runs-on: ubuntu-latest
       steps:
       - uses: actions/checkout@v2
       - name: Set up Python
         uses: actions/setup-python@v2
         with:
           python-version: '3.x'
       - name: Install dependencies
         run: |
           python -m pip install --upgrade pip
           pip install build twine
       - name: Build and publish
         env:
           TWINE_USERNAME: ${{ secrets.PYPI_USERNAME }}
           TWINE_PASSWORD: ${{ secrets.PYPI_PASSWORD }}
         run: |
           python -m build
           twine upload dist/*
   ```

## Recommended Improvements

1. Update the license year in LICENSE file to the current year
2. Simplify the license-files field in pyproject.toml to just "LICENSE"
3. Add more classifiers to pyproject.toml to better describe the package
4. Set up GitHub Actions for automated testing and publishing
5. Add a CHANGELOG.md file to track changes between versions
6. Consider adding type hints and using a tool like mypy for static type checking
7. Consider adding code coverage reporting with a tool like coverage.py