# -*- coding: utf-8 -*-

fname_r1 = "col1.txt"
fname_r2 = "col2.txt"
fname_w = "popular-names-v3.txt"

with open(fname_r1, mode="r") as f:
    col1 = f.read().split()
with open(fname_r2, mode="r") as f:
    col2 = f.read().split()

if (len(col1) - len(col2)):
    print('Error!! length of col1.txt is not equal to it of col2.txt.')
else:
    with open(fname_w, mode="w") as f:
        f.writelines([col1[i]+'\t'+col2[i]+'\n' for i in range(len(col1))])
