from gendiff.scripts.formatters.json import to_json
from gendiff.scripts.formatters.plain import to_plain
from gendiff.scripts.formatters.stylish import to_stylish

from .makediff import make_diff


def generate_diff(file1, file2, format='stylish'):
    diff = make_diff(file1, file2)
    if format == 'stylish':
        return to_stylish(diff)
    
    elif format == 'plain':
        return to_plain(diff)
    
    elif format == 'json':
        return to_json(diff)