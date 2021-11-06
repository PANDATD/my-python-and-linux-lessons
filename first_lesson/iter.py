#!/bin/usr/python3.10
mylist = [
    "Tejas",
    "Kunal",
    "Vignesh",
    "Datta",
]

""" Itor and Itrables
    - List, Set, Tuple, Dict Are the Itrables.
    - All these objects have a iter() method which is used to get an iterator
 """

myiter = iter(mylist)
print(next(myiter))
print(next(myiter))
