from gendiff.scripts.gendiff import generate_diff
import json


def test_generate_diff():
  file1, file2 = json.load(open('gendiff/files/tree1.json')), json.load(open('gendiff/files/tree2.json'))
  assert generate_diff(file1, file2) == '''- follow: False
host: hexlet.io
- proxy: 123.234.53.22
- timeout: 50
+ timeout: 20
+ verbose: True'''
  assert generate_diff(file1, file1) == '''follow: False
host: hexlet.io
proxy: 123.234.53.22
timeout: 50'''