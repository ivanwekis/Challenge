import re


class ValidationError(Exception):
    pass


def validate_email(email):
    """It is necessary to check if the format of the email is correct. Using Regex is simple to verify that.
    We received by parameter the email to validate. If isn´t valid thrown an exception."""
    regex_sentence = "^[a-z0-9]+[@]\w+[.]\w{2,3}$"
    if not re.search(regex_sentence, email):
        print("The following email isn´t correct, please, correct it: {}".format(email))
        raise ValidationError("ERROR while validating email.")
