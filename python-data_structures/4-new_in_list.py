#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        new_list = []
        for elem in my_list:
            new_list.append(elem)
        new_list[idx] = element
        return new_list
