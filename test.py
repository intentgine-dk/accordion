import pandas as pd
from func import db, gdrive, tools, query, date_func

df = tools.file_to_df('{20-1174-1 Workday Customer FIN LE FY21 Content Syndication} 702_Leads 21092020.xls')

for key in df.columns:
    if len(df[key].value_counts()) == 0:
        del df[key]

print(df.columns)