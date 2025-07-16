from gendiff.scripts.gendiff import generate_diff
import yaml


def test_generate_diff():
  file1, file2 = yaml.safe_load(open('gendiff/files/file1.yml')), yaml.safe_load(open('gendiff/files/file2.yml'))
  assert generate_diff(file1, file2) == '''
- follow: False
host: hexlet.io
- proxy: 123.234.53.22
- timeout: 50
+ timeout: 20
+ verbose: True'''
  assert generate_diff(file1, file1) == '''
follow: False
host: hexlet.io
proxy: 123.234.53.22
timeout: 50'''