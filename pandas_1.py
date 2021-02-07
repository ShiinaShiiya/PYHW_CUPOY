import pandas as pd

#讀取資料夾中boston.csv讀取其欄位CHAS、NOX、RM，輸出成.xlsx檔案
r = pd.read_csv('boston.csv', usecols=['CHAS','NOX','RM'])
print(r)
r.to_excel('boston.xlsx')