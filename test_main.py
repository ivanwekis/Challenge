import pytest
from main import main
from validations import ValidationError
from data_io import FormatError

"""This file was created for the purpose of testing the script. 6 different entries will be checked, 
    2 of them are correct and 4 of them are incorrect."""


@pytest.mark.parametrize(
    "input_file,output_file",
    [
        ("test_files/customers2.csv", "output_files/encrypted2.csv"),  # Correct File
        ("test_files/customers3.csv", "output_files/encrypted3.csv"),  # Correct File
    ],
)
def test_valid_inputs(input_file, output_file):
    assert main(input_file, output_file) is None


@pytest.mark.parametrize(
    "input_file,output_file",
    [
        (
            "test_files/customers1.csv",
            "output_files/encrypted1.csv",
        ),  # Bad file, with incorrect header
    ],
)
def test_validation_error(input_file, output_file):
    with pytest.raises(FormatError) as exception:
        main(input_file, output_file)
    assert str(exception.value) == "The file does not have a correct header."


@pytest.mark.parametrize(
    "input_file,output_file",
    [
        (
            "test_files/customers5.csv",
            "output_files/encrypted5.csv",
        ),  # Bad file, with incorrect email format
    ],
)
def test_validation_error(input_file, output_file):
    with pytest.raises(ValidationError) as exception:
        main(input_file, output_file)
    assert str(exception.value) == "ERROR while validating email."


@pytest.mark.parametrize(
    "input_file,output_file",
    [
        (
            "test_files/customers3.csv",
            "output_files/encrypted3.csv",
        ),  # Bad file, with incorrect billing field
    ],
)
def test_validation_error(input_file, output_file):
    with pytest.raises(ValidationError) as exception:
        main(input_file, output_file)
    assert str(exception.value) == "ERROR while validating the billing field."


@pytest.mark.parametrize(
    "input_file,output_file",
    [
        ("test_files/customers7.csv", "output_files/encrypted7.csv"),  # Bad file path
    ],
)
def test_validation_error(input_file, output_file):
    with pytest.raises(FileNotFoundError) as exception:
        main(input_file, output_file)
    assert str(exception.value) == "The path of the file is incorrect."
