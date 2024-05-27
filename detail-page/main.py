import pandas as pd
from engine import getDetailByLink

csv_dir = input('list of items in csv dir: ')
df = pd.read_csv(csv_dir)
start_idx = input('what is the start index: ')
count = input('how many data to collect from start index: ')

current_range = range(start_idx, min(len(df), start_idx + count))

detail_data = []
for i in current_range:
    item = df.loc[i]
    print(item)
    url = item['link']
    detail_data.append(getDetailByLink(url))

detailed_df = pd.concat([df, pd.DataFrame(detail_data, index=current_range)], axis=1)
detailed_df.to_csv('out_detailed_50.csv', index=False)