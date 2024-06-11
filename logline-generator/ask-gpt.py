import pandas as pd

csv_path = input('csv path: ')
df = pd.read_csv(csv_path)

q = "just generate log lines with about 30 words in farsi (persian) language, for the below show title names without any redundant info before and after log line for every show name and also divide loglines using '''/''' character:\n"

for i in range(len(df)):
    q += '.'.join(df.loc[i]['title'].split('.')[1:]).strip() + '\n'

with open('logline-generator/ask-gpt.txt', 'w') as f:
    f.write(q)
