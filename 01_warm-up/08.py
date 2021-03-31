# -*- coding: utf-8 -*-
import re

def cipher(target):
    if not isinstance(target, str):
        print("Error: Type of target is not string!")
        return None

#    list = []
#    for c in target:
#        if c.islower():
#            list.append(chr(219 - ord(c)))
#        else:
#            list.append(c)
#    return "".join(list)

    return re.sub(r'[a-z]', lambda m: chr(219 - ord(m.group())), target)

sent = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New \
Nations Might Also Sign Peace Security Clause. Arthur King Can."

print(sent)
print()

#encipher
print("encipher ->", cipher(sent))
print()

#decipher
print("decipher ->", cipher(cipher(sent)))

