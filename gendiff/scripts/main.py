import argparse
import os

from gendiff.gendiff import generate_diff
from gendiff.scripts.formatters.json import to_json
from gendiff.scripts.formatters.plain import to_plain
from gendiff.scripts.formatters.stylish import to_stylish


def get_full_path(filename):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_dir, 'files', filename)


def main():
    parser = argparse.ArgumentParser(
    prog='gendiff',
    usage='gendiff [-h] [-f FORMAT] first_file second_file',
    description='''Compares two configuration files and shows a difference.''')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        choices=['stylish', 'plain', 'json'],
                        default='stylish',
                        help='set format of output', 
                        metavar='FORMAT')
    args = parser.parse_args() 

    file_path1 = get_full_path(args.first_file)
    file_path2 = get_full_path(args.second_file)
    output_format = args.format

    diff = generate_diff(file_path1, file_path2)

    if output_format == 'stylish':
        return to_stylish(diff)
    
    elif output_format == 'plain':
        return to_plain(diff)

    elif output_format == 'json':
        return to_json(diff)
    
    
if __name__ == "__main__":
    main()
