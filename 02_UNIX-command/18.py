# -*- coding: utf-8 -*-

fname_r = "popular-names.txt"

with open(fname_r, mode="r") as f:
    data = [line.split("\t") for line in f.readlines()]

data = sorted(data, reverse=True, key=lambda x: x[2])
print(''.join(' '.join(d) for d in data))