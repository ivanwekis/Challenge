def average_billing(customers):
    """This function receiver the customer data.
    Calculates the average billing of customers, and check if it is correct the data,
    that is, it´s a number. If it is not correct, an exception wil be thrown.
    Return the calculated average."""
    avg_billing = 0
    i = 0
    for customer in customers:
        try:
            avg_billing += float(customer.get("Billing"))
            i = i + 1
        except ValueError:
            print(
                "The following customer: {Name} does not have a correct billing: {Billing}".format(
                    **customer
                )
            )
            raise ValueError("ERROR while validating the billing field.")
    avg_billing = avg_billing / i
    return avg_billing


def encrypt_alpha_num(word):
    """In this function we received the word to encrypt.
    Returns the word encrypted."""
    encrypted_email = ""
    for letter in word:
        if letter.isalnum():
            encrypted_email += "X"
        else:
            encrypted_email += letter

    return encrypted_email
