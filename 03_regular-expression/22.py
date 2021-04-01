# -*- coding: utf-8 -*-
import pandas as pd
import re
data = pd.read_json("jawiki-country.json.gz", lines=True)
text = data[data['title']=='イギリス']['text'].values[0]
p = r'\[\[Category:.+'
s = r'Category:(\w*)'
print('\n'.join([re.search(s, line).group(1) for line in text.splitlines()
                                             if re.match(p, line)]))
