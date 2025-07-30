import sys
import argparse
import os

from gendiff.gendiff import generate_diff


#def get_full_path(filename):
#    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#    return os.path.join(base_dir, 'files', filename)


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
    try:
        args = parser.parse_args() 
        file_path1 = args.first_file
        file_path2 = args.second_file
        output_format = args.format

        result = generate_diff(file_path1, file_path2, output_format)
        print(result)
        sys.exit(0)

    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
        
    except ValueError as e:
        print(f"Error: Invalid file format - {e}", file=sys.stderr)
        sys.exit(1)
        
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)
        

if __name__ == "__main__":
    main()
