import re


def validate_phone_number(phone_number):
    phone_number_str = str(phone_number)
    phone_number_str = phone_number_str.replace(' ', '')

    pattern = re.compile('[+]57[0|3|6][0|1|2|3|5][0-9][0-9]{7}')
    match = pattern.match(phone_number_str)
    print('..::MATCH PHONE_NUMBER')
    print(match)
    if match:
        return True
    else:
        return False
