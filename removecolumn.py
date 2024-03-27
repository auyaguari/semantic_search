import pandas as pd
df = pd.read_csv ('vecAllE3CCODEREngRec.csv', encoding = 'utf8')


dfFiltrado = pd.DataFrame(df,
                columns =['cui', 'aui',
                        'tensor2string'])

dfFiltrado.to_csv('allE3CCODEREngRec.csv', encoding='utf-8', index=False, sep='~')