#!/usr/bin/python3
"""Module defines a function that divide element by elment on a list"""


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            element_a = my_list_1[i]
            element_b = my_list_2[i]
            new_list.append(element_a / element_b)
        except ZeroDivisionError:
            new_list.append(0)
            print("division by 0")
        except (TypeError, ValueError):
            new_list.append(0)
            print("wrong type")
        except IndexError:
            new_list.append(0)
            print("out of range")
        finally:
            pass
    return new_list
