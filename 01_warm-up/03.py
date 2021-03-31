# -*- coding: utf-8 -*-
import re

sent = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
list = [len(w) for w in re.findall(r"\w+", sent)]
print(list)

