from pathlib import Path

import pytest

from gendiff import gendiff

DIR_FILE = Path(__file__).parent / 'fixtures'


def read_file(file_name):
    file_path = DIR_FILE / file_name
    with open(file_path, 'r') as file:
        return file.read().strip()
    

@pytest.mark.parametrize(
('file1', 'file2', 'expected_file'),
[
    (
        "file1.json",
        "file2.json",
        "test_flat.txt",
    )
]
)
def test_flat(file1, file2, expected_file):
    file1_path = DIR_FILE / file1
    file2_path = DIR_FILE / file2
    expected_result = read_file(expected_file)
    result = gendiff(file1_path, file2_path)
    assert result == expected_result