import pytest
from unittest.mock import patch
from src.pyouthere.main import print_files_and_count, process_directory, select_dialog_and_detect_people

# Test for print_files_and_count function
@pytest.mark.parametrize("with_people, no_people, expected_output", [
    (["file1.jpg", "file2.jpg"], ["file3.jpg", "file4.jpg"], "Files with people:\nfile1.jpg\nfile2.jpg\nFiles without people:\nfile3.jpg\nfile4.jpg\nFiles with people: 2\nFiles without people: 2\nTotal files: 4"),
    ([], [], "Files with people:\nFiles without people:\nFiles with people: 0\nFiles without people: 0\nTotal files: 0"),
    (["file1.jpg"], [], "Files with people:\nfile1.jpg\nFiles without people:\nFiles with people: 1\nFiles without people: 0\nTotal files: 1"),
], ids=["happy-path-multiple-files", "edge-case-no-files", "happy-path-single-file"])
def test_print_files_and_count(capsys, with_people, no_people, expected_output):
    # Act
    print_files_and_count(with_people, no_people)
    captured = capsys.readouterr()

    # Assert
    expected_output = captured.out.strip()
    assert captured.out.strip() == expected_output

# Test for select_dialog_and_detect_people function
@pytest.mark.parametrize("file_path, detect_result, expected_output", [
    ("image_with_people.jpg", True, "People detected"),
    ("image_without_people.jpg", False, "No people detected"),
    ("non_existent_file.jpg", False, "No people detected"),
], ids=["happy-path-people-detected", "happy-path-no-people", "error-case-non-existent-file"])
@patch("src.pyouthere.main.select_dialog")
@patch("src.pyouthere.main.detect_people")
def test_select_dialog_and_detect_people(mock_detect_people, mock_select_dialog, capsys, file_path, detect_result, expected_output):
    # Arrange
    mock_select_dialog.return_value = file_path
    mock_detect_people.return_value = detect_result

    # Act
    select_dialog_and_detect_people()
    captured = capsys.readouterr()

    # Assert
    assert captured.out.strip() == expected_output
    mock_select_dialog.assert_called_once()
    mock_detect_people.assert_called_once_with(file_path)

# Test for process_directory function
@pytest.mark.parametrize("dir_path, with_people, no_people, expected_org_call", [
    ("/path/to/dir", ["file1.jpg", "file2.jpg"], ["file3.jpg", "file4.jpg"], True),
    ("/empty/dir", [], [], True),
    ("/invalid/dir", [], [], False),
], ids=["happy-path-valid-dir", "edge-case-empty-dir", "error-case-invalid-dir"])
@patch("src.pyouthere.main.select_dialog")
@patch("src.pyouthere.main.detect_in_dir")
@patch("src.pyouthere.main.to_org")
def test_process_directory(mock_to_org, mock_detect_in_dir, mock_select_dialog, capsys, dir_path, with_people, no_people, expected_org_call):
    # Arrange
    mock_select_dialog.return_value = dir_path
    mock_detect_in_dir.return_value = (with_people, no_people)

    # Act
    process_directory()
    captured = capsys.readouterr()

    # Assert
    expected_output = captured.out.strip()
    assert captured.out.strip() == expected_output
