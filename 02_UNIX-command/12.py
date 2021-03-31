# -*- coding: utf-8 -*-
import re

fname_r = "popular-names.txt"
fname_w1 = "col1.txt"
fname_w2 = "col2.txt"

with open(fname_r, mode="r") as f:
    datawords = [line.split() for line in f.readlines()]
    col1 = [words[0] for words in datawords]
    col2 = [words[1] for words in datawords]

with open(fname_w1, mode="w") as f:
    f.write('\n'.join(col1))
with open(fname_w2, mode="w") as f:
    f.write('\n'.join(col2))
