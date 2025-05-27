"""
Yamlify Package - Software Detailed Design

This package provides functionality for converting YAML files to rendered output
using Jinja2 templates. It serves as a tool for generating documents from YAML data.

The package is organized into several modules:
- convert: Main conversion functionality
- yaml_loader: YAML file loading
- template_renderer: Template rendering
- utils: Utility functions
- data: Data processing (legacy)
- main: Command-line interface

Public API:
- convert: Main function for converting YAML files to rendered output
- read_folder: Function for reading YAML files from a directory
- main: Entry point for the command-line interface
"""

from .main import main
from .convert import convert
from .data import read_folder

# Also expose the new module functions for direct access
from .yaml_loader import load_yaml_files, load_yaml_files_recursively
from .template_renderer import render_template, markdown_to_html, to_json
from .utils import show_structure
