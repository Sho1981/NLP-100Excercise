# -*- coding: utf-8 -*-
import re

def Ngrum(arg, n):
    if isinstance(arg, str):
        mode = str
    elif isinstance(arg, list):
        mode = list
    else:
        print("Error：Type of arg is not str or list!")

    if mode == str:
        return [tuple(arg[i+j] for j in range(n)) for i in range(len(arg)-n+1)]
    if mode == list:
        return [tuple(arg[i+j] for j in range(n)) for i in range(len(arg)-n+1)]

word1 = "paraparaparadise"
word2 = "paragraph"

X = set(Ngrum(word1, 2))
Y = set(Ngrum(word2, 2))
print("X=", X)
print("Y=", Y)
print("X|Y=", X|Y)
print("X&Y=", X&Y)
print("X-Y=", X-Y)
print("Y-X=", Y-X)

search_ngrum = "se"
x = tuple(re.findall(r".", search_ngrum))
print("'%s' in X?:" % search_ngrum)
print(x in X)
print("'%s' in Y?:" % search_ngrum)
print(x in Y)