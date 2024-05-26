import pandas as pd
from engine import getDetailByLink

csv_dir = input('list of items in csv dir: ')
df = pd.read_csv(csv_dir)

detail_data = []
for i in range(5):
    item = df.loc[i]
    print(item)
    url = item['link']
    detail_data.append(getDetailByLink(url))

detailed_df = pd.concat([df, pd.DataFrame(detail_data)], axis=1)
detailed_df.to_csv('out_detailed.csv', index=False)