# -*- coding: utf-8 -*-
import pandas as pd
import re
data = pd.read_json("jawiki-country.json.gz", lines=True)
text = data[data['title']=='イギリス']['text'].values[0]
p = r'\[\[Category:.+'
print('\n'.join([line for line in text.splitlines() if re.match(p, line)]))
