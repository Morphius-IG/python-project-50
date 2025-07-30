from gendiff.scripts.formatters.stylish import to_stylish


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




