# -*- coding: utf-8 -*-
from nltk import FreqDist

fname_r = "popular-names.txt"

with open(fname_r, mode="r") as f:
    col1 = [line.split()[0] for line in f.readlines()]

f_list = FreqDist(col1).items()
f_list = sorted(f_list, reverse=True, key=lambda x: x[1])

print(''.join([name + ' ' + str(freq) + '\n' for name, freq in f_list]))