#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except Exception as ve:
        print("Exception: {}".format(ve))
        return False
    else:
        return True
