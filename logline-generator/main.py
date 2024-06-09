from engine import generate_logline
import pandas as pd

csv_dir = input("csv path: ")
df = pd.read_csv(csv_dir)
fa_loglines = []

for i in range(10):
    record = df.loc[i]
    fa_loglines.append({"fa_logline": generate_logline('.'.join(record["title"].split('.')[1:]))})


detailed_df = pd.concat([df, pd.DataFrame(fa_loglines)], axis=1)
detailed_df.to_csv("delivery.csv", index=False)
