from gendiff.scripts.formatter import to_stylish
from gendiff.scripts.gendiff import generate_diff
import json
import yaml

def test_to_stylish():
  file1 = (json.load(open('gendiff/files//tree1.json')))
  file2 = (json.load(open('gendiff/files//tree2.json')))
  diff = generate_diff(file1, file2) 

  expected = '''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}'''
  assert to_stylish(diff) == expected
