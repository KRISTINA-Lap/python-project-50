import json
import yaml


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


def format_value(value):
    """Format value for display"""
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return value


def generate_diff(file1_path, file2_path, format_name='stylish'):
    """Generate difference between two files"""
    data1 = parse_file(file1_path)
    data2 = parse_file(file2_path)
    
    return build_diff(data1, data2)


def build_diff(data1, data2):
    """Build diff between two dictionaries"""
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))
    
    diff_lines = ["{"]
    
    for key in all_keys:
        value1 = data1.get(key)
        value2 = data2.get(key)
        
        if key not in data2:
            # Ключ только в первом файле
            diff_lines.append(f"  - {key}: {format_value(value1)}")
        elif key not in data1:
            # Ключ только во втором файле  
            diff_lines.append(f"  + {key}: {format_value(value2)}")
        elif value1 == value2:
            # Ключ в обоих файлах с одинаковым значением
            diff_lines.append(f"    {key}: {format_value(value1)}")
        else:
            # Ключ в обоих файлах с разными значениями
            diff_lines.append(f"  - {key}: {format_value(value1)}")
            diff_lines.append(f"  + {key}: {format_value(value2)}")
    
    diff_lines.append("}")
    return "\n".join(diff_lines)
