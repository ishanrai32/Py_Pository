import numpy as np
import pandas as pd

data = pd.read_csv('browser_rankings_data.csv', skiprows = 1)
data.dropna(inplace = True)
data['Rank'] = data['Rank'].astype(int)

data['short_key_pos'] = data.apply(lambda x: x['Short Description'].find(x['Keyword']), axis=1)
data['long_key_pos'] = data.apply(lambda x: x['Long Description'].find(x['Keyword']), axis=1)

import seaborn as sns
sns.set(rc = {'figure.figsize':(40,8)})
sns.barplot(x = data["Rank"], y = data["short_key_pos"])

sns.barplot(x = data["Rank"], y = data["long_key_pos"])

sns.set(rc = {'figure.figsize':(25,8)})
sns.barplot(x = data["App ID"], y = data["Rank"])
