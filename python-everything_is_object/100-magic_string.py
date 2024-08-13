#!/usr/bin/python3
def magic_string():
    setattr(magic_string, "num", getattr(magic_string, "num", 0) + 1)
    print("BestSchool, " * magic_string.num + "BestSchool\n")
