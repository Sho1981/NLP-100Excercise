# -*- coding: utf-8 -*-
import re

sent = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New \
        Nations Might Also Sign Peace Security Clause. Arthur King Can."
one_num = [1, 5, 6, 7, 8, 9, 15, 16, 19]

words = re.findall(r"\w+", sent)
dict = {}
for i in range(len(words)):
    if i+1 in one_num:
        dict[words[i][0]] = i+1
    else:
        dict[words[i][0:2]] = i+1

print(dict)

