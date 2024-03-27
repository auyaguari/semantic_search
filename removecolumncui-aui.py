import pandas as pd
df = pd.read_csv ('allE3CReduce.csv', encoding = 'utf8')


dfFiltrado = pd.DataFrame(df,
                columns =['cui', 'aui'])

dfFiltrado.to_csv('allcui-aui-reduce.csv', encoding='utf-8', index=False, sep='~')