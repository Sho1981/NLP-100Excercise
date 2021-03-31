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

sent = "I am an NLPer"
print(Ngrum(sent, 2))

words = re.findall(r"\w+", sent)
print(Ngrum(words, 2))
