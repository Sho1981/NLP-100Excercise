# -*- coding: utf-8 -*-

word = "stressed"
reverse = "".join([word[-i] for i in range(1, len(word)+1)])
#reverse = "".join([ch for ch in reversed([c for c in word])])
print(reverse)
