#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        return a / b
    except:
        return None
    finally:
        result = a / b
        print("Inside result: {:d}".format(result))