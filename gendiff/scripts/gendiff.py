import argparse
import json

def main():
    parser = argparse.ArgumentParser(
    prog='gendiff',
    usage='gendiff [-h] [-f FORMAT] first_file second_file',
    description='''Compares two configuration files and shows a difference.''')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output', metavar='FORMAT')
    first_file = json.load(open('gendiff/files/file1.json'))
    second_file = json.load(open('gendiff/files/file2.json'))
    args = parser.parse_args() 
    #parser.print_help()



# …




if __name__ == "__main__":
    main()
