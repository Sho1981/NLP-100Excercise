# -*- coding: utf-8 -*-

word1 = "パトカー"
word2 = "タクシー"
l = min(len(word1), len(word2))
join = "".join([word1[i] + word2[i] for i in range(l)])
print(join)
