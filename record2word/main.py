import aspose.words as aw
import pandas as pd

csv_dir = input('directory of csv to read: ')
count = int(input('how many to generate: '))
df = pd.read_csv(csv_dir)

for i in range(0, count):
    doc = aw.Document()
    doc_builder = aw.DocumentBuilder(doc)
    record = df.loc[i]    
    doc_builder.writeln(f"{record['title'].split('.')[1].strip()}/{record['year']}/{record['rating']}")
    doc_builder.writeln(record['content'])
    doc_builder.writeln(record['link'])
    doc.save(f"record['title'].docx")
