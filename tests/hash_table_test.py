from hash_table.hash_table import EMPTY, HashTable


def test_hash_table_create():
    assert HashTable(size=100) is not None


def test_return_hash_table_size():
    assert len(HashTable(size=100)) == 100


def test_new_hash_table_creates_empty_spaces():
    expected_values = [EMPTY, EMPTY, EMPTY]
    hash_table = HashTable(size=3)

    actual_values = hash_table.values

    assert actual_values == expected_values


def test_insert_key_value_pairs():
    hash_table = HashTable(size=100)
    hash_table["key"] = "value"
    hash_table[99.9] = 42
    hash_table[False] = True

    assert "value" in hash_table.values
    assert 42 in hash_table.values
    assert True in hash_table.values

    assert len(hash_table) == 100


def test_not_contain_none_values_created():
    assert None not in HashTable(size=100).values
