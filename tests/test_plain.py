from gendiff.scripts.formatters.plain import to_plain


def test_added_simple_value():
    data = {"key": {"status": "added", "value": "first"}}
    expected = "Property 'key' was added with value: 'first'"
    assert to_plain(data) == expected

def test_added_boolean():
    data = {"flag": {"status": "added", "value": True}}
    expected = "Property 'flag' was added with value: true"
    assert to_plain(data) == expected

def test_added_none():
    data = {"none_val": {"status": "added", "value": None}}
    expected = "Property 'none_val' was added with value: null"
    assert to_plain(data) == expected

def test_added_complex_value():
    data = {"nested": {"status": "added", "value": {"inner": "value"}}}
    expected = "Property 'nested' was added with value: [complex value]"
    assert to_plain(data) == expected

def test_deleted():
    data = {"old_key": {"status": "deleted"}}
    expected = "Property 'old_key' was removed"
    assert to_plain(data) == expected

def test_changed():
    data = {"key": {"status": "changed", "old": "old", "new": "new"}}
    expected = "Property 'key' was updated. From 'old' to 'new'"
    assert to_plain(data) == expected


def test_nested_properties():
    data = {
        "common": {
            "status": "nested",
            "value": {
                "setting": {"status": "changed", "old": "old", "new": "new"}
            }
        }
    }
    expected = "Property 'common.setting' was updated. From 'old' to 'new'"
    assert to_plain(data) == expected

def test_multiple_properties():
    data = {
        "key1": {"status": "added", "value": "value1"},
        "key2": {"status": "deleted"},
        "key3": {"status": "changed", "old": "old", "new": "new"}
    }
    expected = "\n".join([
        "Property 'key1' was added with value: 'value1'",
        "Property 'key2' was removed",
        "Property 'key3' was updated. From 'old' to 'new'"
    ])
    assert to_plain(data) == expected

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
    expected = "Property 'level1.level2.level3' was added with value: 'deep'"
    assert to_plain(data) == expected

def test_complex_value_directly():
    data = {"config": {"key": "value"}}
    expected = "Property 'config' was added with value: [complex value]"
    assert to_plain(data) == expected