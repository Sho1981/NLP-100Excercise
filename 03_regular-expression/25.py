# -*- coding: utf-8 -*-
import pandas as pd
import re
import pprint

def input_basic_dict(datalines, start_id, basic_dict):
    for line in lines[start_id+1:]:
        if re.match(r'^\|', line):
            field = re.search(r'\|(\w*)', line).group(1)
            value = re.search(r'=\s?(.*)', line).group(1)
            basic_dict[field] = value
        elif re.match(r'\*+', line):
            basic_dict[field] += line
        elif re.match(r'\}\}', line):
            break
        else:
            continue

#main
data = pd.read_json("jawiki-country.json.gz", lines=True)
lines = data[data['title']=='イギリス']['text'].values[0].splitlines()
basic_dict = {}
for i, ls in enumerate(lines):
    if re.match(r'\{\{基礎情報', ls):
        input_basic_dict(lines, i, basic_dict)
        break
pprint.pprint(basic_dict)
