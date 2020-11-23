#%% 
import pandas as pd
import sqlite3
import os
import sys

data_folder = r'C:\Users\aspit\Git\MHDLab-Projects\Energy Storage\data'

con = sqlite3.connect(os.path.join(data_folder, 'nlp_justenergystorage.db'))
cursor = con.cursor()

df = pd.read_sql_query("SELECT * FROM texts", con, index_col='ID')

df = df.dropna(subset=['processed_text'])
df = df[df['language'] == 'en']

#%%

# %%
num_papers = str(len(df))

print('Number of papers: ' + num_papers)

# %%
search_terms = ", ".join(set(df['searchterm']))


print('Search Terms: ' + search_terms)





# %%
