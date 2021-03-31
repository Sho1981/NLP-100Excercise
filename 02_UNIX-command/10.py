# -*- coding: utf-8 -*-

filename = "popular-names.txt"

f = open(filename, "r")
datalines = f.readlines()
print(len(datalines))
f.close()

