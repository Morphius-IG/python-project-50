import argparse
from gendiff.scripts.parser import parse_files


PATH_FOLD = 'gendiff/files/'
def generate_diff(data1, data2):
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff = {}
    
    for key in keys:
        if key not in data1:
            diff[f"+ {key}"] = data2[key]
        elif key not in data2:
            diff[f"- {key}"] = data1[key]
        elif data1[key] != data2[key]:
            diff[f"- {key}"] = data1[key]
            diff[f"+ {key}"] = data2[key]
        else:
            diff[key] = data1[key]
    lines = []
    for key, value in diff.items():
        lines.append(f"{key}: {value}")
    return '\n'.join(lines)
    

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


    file1_data, file2_data = parse_files(PATH_FOLD + args.first_file, PATH_FOLD + args.second_file)
    diff = generate_diff(file1_data, file2_data)
    return diff


if __name__ == "__main__":
    main()
