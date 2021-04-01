# -*- coding: utf-8 -*-
import sys

def d_num_list(length, n):
    """
    Making divided number list that number 'length' is divided by number n
    for example length = 100, n = 8 -> [13, 13, 13, 13, 12, 12, 12, 12]
    """
    if n == 1:
        return [length]
    d = length // n
    if (length % n):
        return [d+1] + d_num_list(length-d-1, n-1)
    else:
        return [d] + d_num_list(length-d, n-1)

def d_index_list(length, n):
    """
    Making index list that number 'length' is divided by number 'n'.
    for example length = 100, n = 8 -> [0, 13, 26, 39, 52, 64, 76, 88]
    """
    num_list = d_num_list(length, n)
    return [sum(num_list[:i]) for i in range(len(num_list))]

fname_r = "popular-names.txt"

n = sys.argv[-1]
while not(n.isdigit()):
    n = input('Input number >')
n = int(n)

with open(fname_r, mode="r") as f:
    datalines = f.readlines()

indexs = d_index_list(len(datalines), n)

split_datalines = [datalines[indexs[i]:indexs[i+1]] for i in range(n-1)]
split_datalines.append(datalines[indexs[-1]:])

"""
for i in range(n):
    print("File No. %d" % (i+1))
    print(''.join(split_datalines[i]))
"""