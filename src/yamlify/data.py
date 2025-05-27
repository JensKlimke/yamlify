import yaml
import os
import logging
from pathlib import Path
from typing import List, Dict, Any, Optional

# Set up logging
logger = logging.getLogger(__name__)

def read_folder(directory: str, path: str, data: List[Any], index: Dict[str, Any]) -> Optional[List[str]]:
    """
    Reads all YAML files from a specified directory and loads their content into data structures.

    Args: 
        directory (str): The base directory path.
        path (str): The relative path from the base directory to search for YAML files.
        data (list): A list to append the loaded YAML content to.
        index (dict): A dictionary to store the loaded YAML content with filenames as keys.

    Returns:
        Optional[List[str]]: List of errors encountered during processing, or None if no errors occurred.

    Raises:
        ValueError: If any of the input parameters are invalid.
        FileNotFoundError: If the specified directory does not exist.
    """
    # Validate input parameters
    if not directory or not isinstance(directory, str):
        raise ValueError("Directory must be a non-empty string")
    if not isinstance(path, str):
        raise ValueError("Path must be a string")
    if not isinstance(data, list):
        raise ValueError("Data must be a list")
    if not isinstance(index, dict):
        raise ValueError("Index must be a dictionary")

    # Construct the full directory path
    full_path = os.path.join(directory, path)

    # Check if the directory exists
    if not os.path.isdir(full_path):
        raise FileNotFoundError(f"Directory not found: {full_path}")

    # Use pathlib for more robust path handling
    search_path = Path(full_path)

    # Get all YAML files in the directory
    yaml_files = list(search_path.glob("*.yaml"))

    # Check if the directory is empty
    if not yaml_files:
        logger.warning(f"No YAML files found in {full_path}")
        return None

    errors = []

    # Process each YAML file
    for file_path in yaml_files:
        logger.info(f"Reading file: {file_path}")

        # Get name without extension using pathlib
        name = str(file_path.with_suffix(''))

        try:
            # Open and parse the YAML file
            with open(file_path, 'r', encoding='utf-8') as stream:
                try:
                    yaml_content = yaml.safe_load(stream)
                    index[name] = yaml_content
                    data.append(yaml_content)
                except yaml.YAMLError as exc:
                    error_msg = f"YAML parsing error in {file_path}: {exc}"
                    logger.error(error_msg)
                    errors.append(error_msg)
        except (IOError, PermissionError) as exc:
            error_msg = f"Error opening file {file_path}: {exc}"
            logger.error(error_msg)
            errors.append(error_msg)

    return errors if errors else None
