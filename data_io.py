import mask
import validations


class FormatError(Exception):
    pass


def read_file(input_file_path):
    """This function allows you to check if the file entered by parameters exists.
    The input parameters are the input file path.
    If exists, it returns the data of the file."""
    try:
        data = ""
        with open(input_file_path, "r") as file:
            data = file.read()
        return data
    except FileNotFoundError:
        raise FileNotFoundError("The path of the file is incorrect.")


def write_header_and_encrypted_data(header, customers, output_file_path):
    """This functions writes the header without been encrypted in the encrypted file and later
    encrypt the data.
    The function receives by param the header of the file, the data of the customers and the output file path."""

    text_encrypted = ",".join(header)
    text_encrypted += "\n"

    average = mask.average_billing(customers)

    for customer in customers:
        line = ""
        non_coma = 0
        for key in customer:
            if non_coma:
                line += ","
            if key == "Email":
                validations.validate_email(customer.get(key))
                email = mask.encrypt_alpha_num(customer.get(key))
                line += email
            if key == "Name":
                name = mask.encrypt_alpha_num(customer.get(key))
                line += name
            elif key == "Billing":
                line += str(average)
            else:
                line += customer.get(key)
            non_coma += 1
        line += "\n"
        text_encrypted += line
    with open(output_file_path, "w") as encrypted_csv:
        encrypted_csv.write(text_encrypted)


def get_customers_dictionary(data, header_expected_list):
    """This function receives the data of the file and the expected header list.
    The algorithm checks if the header is correct, in that case, exports the data to a list of dictionaries for
    a better execution.
    It returns the list of dictionaries and the file header.
    """
    customers_list_dictionary = []
    customers_list = data.split("\n")
    header_csv = customers_list[0].split(",")

    if set(header_csv).issuperset(
        header_expected_list
    ):  # Here we check that the expected header are in the file
        for num_line in range(1, len(customers_list)):
            customer_aux = {}
            customer_list = customers_list[num_line].split(",")
            for column in range(len(header_csv)):
                customer_aux[header_csv[column]] = customer_list[column].replace(
                    "\n", ""
                )
            customers_list_dictionary.append(customer_aux)
    else:
        raise FormatError("The header of the .csv file does not have a correct format.")
    return customers_list_dictionary, header_csv
