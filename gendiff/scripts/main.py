import argparse

from gendiff.scripts.formatter import to_stylish
from gendiff.scripts.gendiff import generate_diff
from gendiff.scripts.parser import parse_files

PATH_FOLD = 'gendiff/files/'
   

def main():
    parser = argparse.ArgumentParser(
    prog='gendiff',
    usage='gendiff [-h] [-f FORMAT] first_file second_file',
    description='''Compares two configuration files and shows a difference.''')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', 
                        help='set format of output', 
                        metavar='FORMAT')
    args = parser.parse_args() 

    file1_data, file2_data = parse_files(PATH_FOLD + args.first_file, 
                                         PATH_FOLD + args.second_file)
    # output_format = args.first_file.FORMAT
    diff = generate_diff(file1_data, file2_data)
    return to_stylish(diff)


if __name__ == "__main__":
    main()
