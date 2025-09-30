#!/usr/bin/env python3
import argparse
import json
import yaml
from gendiff.diff.core import generate_diff


def parse_file(file_path):
    """Parse configuration file (JSON or YAML)"""
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        
        if file_path.endswith('.json'):
            return json.loads(content)
        elif file_path.endswith(('.yaml', '.yml')):
            return yaml.safe_load(content)
        else:
            raise ValueError(f"Unsupported file format: {file_path}")
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except (json.JSONDecodeError, yaml.YAMLError) as e:
        raise ValueError(f"Error parsing {file_path}: {e}")


def generate_diff(file1_path, file2_path, format_name='stylish'):
    """Generate difference between two files"""
    data1 = parse_file(file1_path)
    data2 = parse_file(file2_path)
    
    # вывод данных
    result = [
        f"Comparison in {format_name} format:",
        f"File 1 ({file1_path}):",
        f"  {data1}",
        f"File 2 ({file2_path}):", 
        f"  {data2}",
        "Differences to be implemented..."
    ]
    return "\n".join(result)


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        default='stylish',
        help='set format of output'
    )
    
    args = parser.parse_args()
    
    try:
        diff = generate_diff(args.first_file, args.second_file, args.format)
        print(diff)
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
        return 1


if __name__ == '__main__':
    main()
