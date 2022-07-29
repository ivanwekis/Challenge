#!/usr/bin python3
import argparse
import data_io
import stats


def main(input_file_path, output_file_path):
    """This is the main part of the code. The inputs are the paths of the input and output file.
    here we execute in order the different instructions"""
    header_expected_list = {"Name", "Email", "Billing"}
    data = data_io.read_file(input_file_path)
    customers, header = data_io.get_customers_dictionary(data, header_expected_list)
    data_io.write_header_and_encrypted_data(header, customers, output_file_path)

    stats.billing_stats(customers)
    stats.name_stats(customers)


if __name__ == "__main__":
    """The inputs are captured with the argparse function. One of the reasons is to be able to make a test file."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input_file",
        type=str,
        default="test_files/customers2.csv",
        help="Name of the input file. By default ='test_files/customers2.csv'",
    )
    parser.add_argument(
        "--output_file",
        type=str,
        default="output_files/encrypted.csv",
        help="Name of the output file. By default ='output_files/encrypted.csv'",
    )
    args = parser.parse_args()
    main(args.input_file, args.output_file)
