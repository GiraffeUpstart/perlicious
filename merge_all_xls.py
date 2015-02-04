# Concatenate all xls files in current folder using pandas
import os
import pandas as pd

path = os.getcwd()
files = os.listdir(path)
files_xls = [f for f in files if f[-3:] == 'xls']

df = pd.DataFrame()

for f in files_xls:
    data = pd.read_excel(f)
    df = df.append(data)

df.to_excel("all_merged.xls")
