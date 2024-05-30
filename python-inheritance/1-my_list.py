#!/usr/bin/python3
"""Module containing print_sorted func"""


class MyList(list):
    """Class inherited from list class"""

    def print_sorted(self):
        """Method to print sorted list"""
        new_list = sorted(self)
        print(new_list)
        return new_list


my_list = MyList()
my_list.append("salam")
my_list.append("1")
new_list = my_list.print_sorted()
print(new_list)
