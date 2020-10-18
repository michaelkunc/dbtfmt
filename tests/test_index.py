import pytest

from dbtfmt import index


def test_reader_simple():
    output = index.reader("tests/sql_files/simple_string.sql")
    assert output == ["here", "is", "a", "simple", "string"]


def test_reader_simple_newlines():
    output = index.reader("tests/sql_files/string_newlines.sql")
    assert output == ["stuff", "things", "foo", "bar"]


def test_simple():
    output = index.reader("tests/sql_files/simple.sql")
    assert output[0] == "{{"
    assert output[1] == "config("
    assert output[-1] == "t"


def test_scan_file():
    file_contents = index.reader("tests/sql_files/simple.sql")
    output = index.scan_file(file_contents)
    assert output["select"] == [8, 17, 26, 35, 46]
    assert output["from"] == [49]
    assert output["config("] == [48]
