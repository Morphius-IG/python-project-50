import yaml
from gendiff.makediff import make_diff


def test_make_diff_flat_json():
    file1 = {"a": 1, "b": 2, "c": 3}
    file2 = {"a": 1, "b": 20, "d": 4}
    expected = {
        'a': {'status': 'not changed', 'value': 1},
        'b': {'status': 'changed', 'old': 2, 'new': 20},
        'c': {'status': 'deleted', 'value': 3},
        'd': {'status': 'added', 'value': 4},
    }
    assert make_diff(file1, file2) == expected


def test_make_diff_nested_json():
    file1 = {
        "common": {
            "setting1": "Value 1",
            "setting2": 200,
        },
        "group1": {
            "baz": "bas",
        }
    }
    file2 = {
        "common": {
            "setting1": "Value 1",
            "setting3": None,
        },
        "group2": {
            "abc": 12345,
        }
    }
    expected = {
        'common': {
            'status': 'nested',
            'value': {
                'setting1': {'status': 'not changed', 'value': 'Value 1'},
                'setting2': {'status': 'deleted', 'value': 200},
                'setting3': {'status': 'added', 'value': None},
            }
        },
        'group1': {
            'status': 'deleted',
            'value': {'baz': 'bas'},
        },
        'group2': {
            'status': 'added',
            'value': {'abc': 12345},
        }
    }
    assert make_diff(file1, file2) == expected


def test_make_diff_flat_yaml():
    file1 = yaml.safe_load("""
        a: 1
        b: 2
        c: 3
    """)
    file2 = yaml.safe_load("""
        a: 1
        b: 20
        d: 4
    """)
    expected = {
        'a': {'status': 'not changed', 'value': 1},
        'b': {'status': 'changed', 'old': 2, 'new': 20},
        'c': {'status': 'deleted', 'value': 3},
        'd': {'status': 'added', 'value': 4},
    }
    assert make_diff(file1, file2) == expected