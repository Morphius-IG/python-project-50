from gendiff.scripts.formatters.json import to_json


def test_simple_added():

    
    data = {"key": {"status": "added", "value": "value"}}
    expected = (
        '{\n    "key": {\n        "status": "added",\n'
        '        "value": "value"\n    }\n}'
    )
    assert to_json(data) == expected


def test_simple_deleted():

    
    data = {"key": {"status": "deleted", "value": "value"}}
    expected = (
        '{\n    "key": {\n        "status": "deleted",\n'
        '        "value": "value"\n    }\n}'
    )
    assert to_json(data) == expected


def test_simple_changed():

    
    data = {"key": {"status": "changed", "old": "old", "new": "new"}}
    expected = (
        '{\n    "key": {\n        "status": "changed",\n'
        '        "old": "old",\n        "new": "new"\n    }\n}'
    )
    assert to_json(data) == expected


def test_not_changed():

    
    data = {"key": {"status": "not changed", "value": "value"}}
    expected = (
        '{\n    "key": {\n        "status": "not changed",\n'
        '        "value": "value"\n    }\n}'
    )
    assert to_json(data) == expected


def test_nested_structure():

    
    data = {
        "nested": {
            "status": "nested",
            "value": {
                "child": {"status": "added", "value": "value"}
            }
        }
    }
    expected = (
        '{\n    "nested": {\n        "status": "nested",\n'
        '        "value": {\n            "child": {\n'
        '                "status": "added",\n'
        '                "value": "value"\n            }\n'
        '        }\n    }\n}'
    )
    assert to_json(data, depth=1) == expected


def test_multiple_properties():

    
    data = {
        "added": {"status": "added", "value": "new"},
        "deleted": {"status": "deleted", "value": "old"},
    }
    expected = (
        '{\n    "added": {\n        "status": "added",\n'
        '        "value": "new"\n    },\n    "deleted": {\n'
        '        "status": "deleted",\n        "value": "old"\n    }\n}'
    )
    assert to_json(data) == expected


def test_boolean_and_none():

    
    data = {
        "bool_true": {"status": "added", "value": True},
        "bool_false": {"status": "added", "value": False},
        "none_val": {"status": "added", "value": None}
    }
    expected = (
        '{\n    "bool_true": {\n        "status": "added",\n'
        '        "value": true\n    },\n    "bool_false": {\n'
        '        "status": "added",\n        "value": false\n    },\n'
        '    "none_val": {\n        "status": "added",\n'
        '        "value": null\n    }\n}'
    )
    assert to_json(data) == expected


def test_complex_value():

    
    data = {"nested": {"status": "added", "value": {"inner": "value"}}}
    expected = (
        '{\n    "nested": {\n        "status": "added",\n'
        '        "value": {\n            "inner": "value"\n'
        '        }\n    }\n}'
    )
    assert to_json(data) == expected


def test_root_level():

    
    data = {"key": "value"}
    expected = '{\n    "key": "value"\n}'
    assert to_json(data) == expected