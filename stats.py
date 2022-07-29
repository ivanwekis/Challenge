import mask


def billing_stats(customers):
    """This function return the stats of the billing. It returns the average, maximum and minimum customers billing"""
    min_billing = 100000000
    max_billing = 0
    i = 0
    for customer in customers:
        value = float(customer.get("Billing"))
        if value > max_billing:
            max_billing = value
        if value < min_billing:
            min_billing = value
        i = i + 1
    average_billing = mask.average_billing(customers)
    print(
        "Stats for the Billing:\n average: {},minimum: {}, maximum: {}".format(
            average_billing, min_billing, max_billing
        )
    )


def name_stats(customers):
    """This function return the stats of the billing. It returns the average, maximum and minimum length of the
    customers name"""
    avg_name = 0
    min_name = 100000000
    max_name = 0
    for customer in customers:
        value = len(customer.get("Name"))
        avg_name = avg_name + value
        if value > max_name:
            max_name = value
        if value < min_name:
            min_name = value
    avg_name = avg_name / len(customers)
    print(
        "Stats for the Name :\n average: {}, minimum: {}, maximum: {}".format(
            avg_name, min_name, max_name
        )
    )
