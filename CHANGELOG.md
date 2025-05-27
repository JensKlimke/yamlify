# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- GitHub Actions workflows for automated testing and publishing
- MAINTAINERS.md with instructions for publishing new versions
- CHANGELOG.md to track changes between versions

### Changed
- Updated pyproject.toml with more classifiers and simplified license-files field
- Changed version from development (0.1.1-dev02) to release (0.1.1)
- Updated LICENSE file with correct copyright year

## [0.1.1] - 2023-05-27

### Changed
- First official release version
- Improved main.py to work both as a library and as a command-line tool
- Added comprehensive documentation in README.md

## [0.1.1-dev02] - 2023-04-17

### Added
- Initial development release
- Basic functionality for converting YAML files to rendered output using Jinja2 templates
- Command-line interface
- Support for recursive loading of YAML files
- Support for custom processors