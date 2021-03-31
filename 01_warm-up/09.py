# -*- coding: utf-8 -*-
import re
import random

def shuffle(words):
    if len(words) == 1:
        return words
    return [words.pop(random.randint(0, len(words)-1))] + shuffle(words)

def shf_word(word):
    if len(word) < 5:
        return word
    else:
        chars = re.findall(r".", word)
        return "".join([chars[0]] + shuffle(chars[1:len(word)-1]) + [chars[-1]])

def encode_shuffle(sent):
    return " ".join([shf_word(w) for w in sent.split()])

sent = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(encode_shuffle(sent))
