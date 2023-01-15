import pathlib
import datetime

import pytest

import tomte


@pytest.fixture
def test_file():
    return pathlib.Path('data/img/chocolate.jpg')


def test_calc_checksum(test_file):
    expected_checksum = '9c12b09015e8fe1bdd3c9aa765d08c5cdd60a485'

    calculated_checksum = tomte._calc_checksum(test_file)

    assert expected_checksum == calculated_checksum


def test_extract_date(test_file):
    expected_date = datetime.datetime(2021, 6, 28, 9, 31, 21)

    extracted_date = tomte._extract_date(test_file)

    assert expected_date == extracted_date


def test_process_file(test_file, tmp_path):
    expected_file = pathlib.Path(tmp_path).joinpath('2021/6')

    tomte._process_file(test_file, tmp_path)

    assert expected_file.exists()