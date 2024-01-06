import pandas as pd

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

unique_labels = set(data['whoAmI'])
one_hot_encoding = pd.DataFrame(0, columns=unique_labels, index=data.index)
one_hot_encoding = one_hot_encoding.add(data['whoAmI'].eq(unique_labels).astype(int), axis=0)

data_one_hot = pd.concat([data, one_hot_encoding], axis=1)

data_one_hot = data_one_hot.drop('whoAmI', axis=1)

data_one_hot.head()