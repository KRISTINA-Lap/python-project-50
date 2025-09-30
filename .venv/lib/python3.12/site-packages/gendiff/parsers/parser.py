import json
import yaml


def parse_file(file_path):
    """Parse configuration file (JSON or YAML)"""
    with open(file_path, 'r') as file:
        content = file.read()
    
    if file_path.endswith('.json'):
        return json.loads(content)
    elif file_path.endswith(('.yaml', '.yml')):
        return yaml.safe_load(content)
    else:
        raise ValueError(f"Unsupported file format: {file_path}")
