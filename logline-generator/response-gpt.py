import pandas as pd
with open('logline-generator/response-gpt.txt', 'r') as f:
    answers = f.read()

fa_loglines = [{'fa_logline': x.strip()} for x in answers.split('/')]
csv_path = input('csv path: ')
df = pd.read_csv(csv_path)

detailed_df = pd.concat([df, pd.DataFrame(fa_loglines)], axis=1)
detailed_df.to_csv("delivery.csv", index=False)
