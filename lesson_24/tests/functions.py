def assert_sorted(items, key):
    values = [item[key] for item in items]
    assert values == sorted(values), f"Response is not sorted by '{key}'. Values: {values}"
