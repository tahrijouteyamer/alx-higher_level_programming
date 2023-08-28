#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a list that are integers

    Args:
        my_list (list): a list to print elements from
        x (int): a number of elements of my_list to print

    Returns:
        the number of elements printed
    """
    ret = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)

=============================
3-safe_print_division.py

#!/usr/bin/python3

def safe_print_division(a, b):
    """Returns the division of a by b."""
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)
