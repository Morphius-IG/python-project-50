from gendiff.formatters.json import to_json
from gendiff.formatters.plain import to_plain
from gendiff.formatters.stylish import to_stylish
from gendiff.scripts.parser import parse_files

from .makediff import make_diff


def generate_diff(file_path1, file_path2, format='stylish'):
    file1, file2 = parse_files(file_path1, file_path2)
    
    diff = make_diff(file1, file2)
    if format == 'stylish':
        return to_stylish(diff)
    
    elif format == 'plain':
        return to_plain(diff)
    
    elif format == 'json':
        return to_json(diff)