import json
import yaml


def parse_files(file_path1, file_path2):
    parsed_file1 = json.load(open(file_path1)) if '.json' in file_path1 else yaml.safe_load(open(file_path1))
    parsed_file2 = json.load(open(file_path2)) if '.json' in file_path2 else yaml.safe_load(open(file_path2))
    return parsed_file1, parsed_file2