# -*- coding: utf-8 -*-
import re

fname_r = "popular-names.txt"
fname_w = "popular-names-v2.txt"

with open(fname_r, mode="r") as f:
    datalines = [re.sub(r'\t', ' ', line) for line in f.readlines()]

with open(fname_w, mode="w") as f:
    f.writelines(datalines)

