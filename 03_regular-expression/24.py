# -*- coding: utf-8 -*-
import pandas as pd
import re
data = pd.read_json("jawiki-country.json.gz", lines=True)
text = data[data['title']=='イギリス']['text'].values[0]

p = r'\[\[ファイル:([\w\s\.\(\)\'\-\&,]*)'
print('\n'.join([fname for line in text.splitlines()
                       for fname in re.findall(p, line) if re.match(p, line)]))