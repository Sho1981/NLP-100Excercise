# -*- coding: utf-8 -*-
import json
import gzip
import re

fname_r = "jawiki-country.json.gz"
with gzip.open(fname_r, mode="r") as f:
    jsonlines = f.readlines()

for line in jsonlines:
    article_dict = json.loads(line)
    if article_dict['title'] == 'イギリス':
        l = [line for line in article_dict['text'].splitlines()
                  if re.match(r'\[\[Category:.+', line)]
        print('\n'.join(l))
