from gendiff.scripts.formatter import to_stylish
from gendiff.scripts.gendiff import generate_diff
import json


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


def test_to_stylish_flat_dict():
    data = {
        "key1": {"status": "added", "value": "value1"},
        "key2": {"status": "deleted", "value": "value2"},
    }
    expected = (
        "{\n"
        "  + key1: value1\n"
        "  - key2: value2\n"
        "}"
    )
    assert to_stylish(data) == expected


def test_to_stylish_nested_dict():
    data = {
        "parent": {
            "status": "parent",
            "value": {
                "child": {"status": "added", "value": "child_value"}
            }
        }
    }
    expected = (
        "{\n"
        "    parent: {\n"
        "      + child: child_value\n"
        "    }\n"
        "}"
    )
    assert to_stylish(data) == expected


def test_to_stylish_changed_value():
    data = {
        "key": {
            "status": "changed",
            "old": "old_value",
            "new": "new_value"
        }
    }
    expected = (
        "{\n"
        "  - key: old_value\n"
        "  + key: new_value\n"
        "}"
    )
    assert to_stylish(data) == expected


def test_to_stylish_not_changed_value():
    data = {
        "key": {"status": "not changed", "value": "same_value"}
    }
    expected = (
        "{\n"
        "    key: same_value\n"
        "}"
    )
    assert to_stylish(data) == expected





