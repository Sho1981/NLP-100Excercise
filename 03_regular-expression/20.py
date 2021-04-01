# -*- coding: utf-8 -*-
#import json
#import gzip
#fname_r = "jawiki-country.json.gz"
#with gzip.open(fname_r, mode="r") as f:
#    jsonlines = f.readlines()
"""
for line in jsonlines:
    article_dict = json.loads(line)
    if article_dict['title'] == 'イギリス':
        print(article_dict['text'])
"""
import pandas as pd
data = pd.read_json("jawiki-country.json.gz", lines=True)
print(data[data['title']=='イギリス']['text'].values[0])
