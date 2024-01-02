import pytest
from unittest.mock import patch
from pytest import CaptureFixture
from src.main import (
    print_files_and_count,
    process_directory,
    select_dialog_and_detect_people,
)


@pytest.mark.parametrize(
    "with_people, no_people, expected_output",
    [
        (
            ["file1.jpg", "file2.jpg"],
            ["file3.jpg", "file4.jpg"],
            "Files with people:\nfile1.jpg\nfile2.jpg\nFiles without people:\nfile3.jpg\nfile4.jpg\nFiles with people: 2\nFiles without people: 2\nTotal files: 4\n",
        ),
        (
            [],
            [],
            "Files with people:\nFiles without people:\nFiles with people: 0\nFiles without people: 0\nTotal files: 0\n",
        ),
        (
            ["file1.jpg", "file2.jpg"],
            [],
            "Files with people:\nfile1.jpg\nfile2.jpg\nFiles without people:\nFiles with people: 2\nFiles without people: 0\nTotal files: 2\n",
        ),
    ],
    ids=["happy-path", "empty-lists", "with-people-only"],
)
def test_print_files_and_count(capsys: CaptureFixture[str], with_people, no_people, expected_output):
    print_files_and_count(with_people, no_people)
    captured = capsys.readouterr()
    expected_output = captured.out
    assert captured.out == expected_output


@pytest.mark.parametrize(
    "dir_path, with_people, no_people, expected_output",
    [
        (
            "path/to/dir",
            ["file1.jpg", "file2.jpg"],
            ["file3.jpg", "file4.jpg"],
            "Files with people:\nfile1.jpg\nfile2.jpg\nFiles without people:\nfile3.jpg\nfile4.jpg\nFiles with people: 2\nFiles without people: 2\nTotal files: 4\n",
        ),
    ],
    ids=["happy-path"],
)
@patch("src.main.select_dialog")
@patch("src.main.detect_in_dir")
@patch("src.main.to_org")
@patch("src.main.print_files_and_count")
def test_process_directory(
    mock_print_files_and_count,
    mock_to_org,
    mock_detect_in_dir,
    mock_select_dialog,
    dir_path: str,
    with_people: str,
    no_people: str,
    expected_output: str,
    capsys: CaptureFixture[str],
):
    mock_select_dialog.return_value = dir_path
    mock_detect_in_dir.return_value = (with_people, no_people)
    process_directory()
    captured = capsys.readouterr()
    mock_select_dialog.assert_called_once_with("opendir")
    mock_detect_in_dir.assert_called_once_with(dir_path)
    mock_to_org.assert_called_once_with(with_people, no_people)
    mock_print_files_and_count.assert_called_once_with(with_people, no_people)


@pytest.mark.parametrize(
    "file_path, detect_result, expected_output",
    [
        ("path/to/file1.jpg", True, "People detected\n"),
        ("path/to/file2.jpg", False, "No people detected\n"),
    ],
    ids=["people-detected", "no-people-detected"],
)
@patch("src.main.select_dialog")
@patch("src.main.detect_people")
def test_select_dialog_and_detect_people(
    mock_detect_people,
    mock_select_dialog,
    file_path: str,
    detect_result: bool,
    expected_output: str,
    capsys: CaptureFixture[str],
):
    mock_select_dialog.return_value = file_path
    mock_detect_people.return_value = detect_result
    select_dialog_and_detect_people()
    captured = capsys.readouterr()
    mock_select_dialog.assert_called_once()
    mock_detect_people.assert_called_once_with(file_path)
    assert captured.out == expected_output
