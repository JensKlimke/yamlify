# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2025-05-28

### Added
- GitHub Actions workflows for automated testing and publishing
- MAINTAINERS.md with instructions for publishing new versions
- CHANGELOG.md to track changes between versions

### Changed
- Updated pyproject.toml with more classifiers and simplified license-files field
- Changed version from development (0.1.1-dev02) to release (0.1.1)
- Updated LICENSE file with correct copyright year
- Added --version flag to command-line interface

## [0.1.1]

- First official release version
- Basic functionality for converting YAML files to rendered output using Jinja2 templates
- Command-line interface
- Support for recursive loading of YAML files
- Support for custom processors
