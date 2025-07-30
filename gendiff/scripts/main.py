import argparse
import os

from gendiff.gendiff import generate_diff

# from gendiff.scripts.parser import parse_files


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
#    file1, file2 = parse_files(file_path1, file_path2)

    return generate_diff(file_path1, file_path2, output_format)


if __name__ == "__main__":
    main()
