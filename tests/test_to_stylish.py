from gendiff.scripts.formatters.stylish import to_stylish
from gendiff.gendiff import generate_diff
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


def test_simple_added():
    data = {"key": {"status": "added", "value": "value"}}
    expected = "{\n  + key: value\n}"
    assert to_stylish(data) == expected

def test_simple_deleted():
    data = {"key": {"status": "deleted", "value": "value"}}
    expected = "{\n  - key: value\n}"
    assert to_stylish(data) == expected

def test_simple_changed():
    data = {"key": {"status": "changed", "old": "old", "new": "new"}}
    expected = "{\n  - key: old\n  + key: new\n}"
    assert to_stylish(data) == expected

def test_not_changed():
    data = {"key": {"status": "not changed", "value": "value"}}
    expected = "{\n    key: value\n}"
    assert to_stylish(data) == expected

def test_nested_structure():
    data = {
        "nested": {
            "status": "nested",
            "value": {
                "child": {"status": "added", "value": "value"}
            }
        }
    }
    expected = "{\n    nested: {\n      + child: value\n    }\n}"
    assert to_stylish(data, depth=1) == expected

def test_multiple_properties():
    data = {
        "added": {"status": "added", "value": "new"},
        "deleted": {"status": "deleted", "value": "old"},
        "changed": {"status": "changed", "old": "old", "new": "new"}
    }
    expected = ("{\n"
                "  + added: new\n"
                "  - deleted: old\n"
                "  - changed: old\n"
                "  + changed: new\n"
                "}")
    assert to_stylish(data) == expected

def test_boolean_and_none():
    data = {
        "bool_true": {"status": "added", "value": True},
        "bool_false": {"status": "added", "value": False},
        "none_val": {"status": "added", "value": None}
    }
    expected = ("{\n"
                "  + bool_true: true\n"
                "  + bool_false: false\n"
                "  + none_val: null\n"
                "}")
    assert to_stylish(data) == expected

def test_complex_value():
    data = {"nested": {"status": "added", "value": {"inner": "value"}}}
    expected = "{\n  + nested: {\n        inner: value\n    }\n}"
    assert to_stylish(data) == expected

def test_deeply_nested():
    data = {
        "level1": {
            "status": "nested",
            "value": {
                "level2": {
                    "status": "nested",
                    "value": {
                        "level3": {"status": "added", "value": "deep"}
                    }
                }
            }
        }
    }
    expected = ("{\n"
                "    level1: {\n"
                "        level2: {\n"
                "          + level3: deep\n"
                "        }\n"
                "    }\n"
                "}")
    assert to_stylish(data, depth=1) == expected

def test_root_level():
    data = {"key": "value"}
    expected = "{\n    key: value\n}"
    assert to_stylish(data) == expected




