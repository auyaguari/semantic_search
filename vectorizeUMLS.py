from sentence_transformers import SentenceTransformer
#model = SentenceTransformer('paraphrase-multilingual-mpnet-base-v2')
model = SentenceTransformer('GanjinZero/UMLSBert_ENG')
import pandas as pd
df = pd.read_csv('allE3CReduceRec.csv')
import numpy as np
df["tensor"] = np.nan
df['tensor'] = df['tensor'].astype(object)
df["tensor2string"] = np.nan
df['tensor2string'] = df['tensor2string'].astype(str)
print(df)
cont = 0
try:
    for ind in df.index:
        #print(df['aui'][ind], df['str'][ind])
        try:
            sentence_embeddings = model.encode(df['str'][ind])
            #print(type(sentence_embeddings))
            df['tensor'][ind]=sentence_embeddings
            df['tensor2string'][ind]=np.array2string(df['tensor'][ind], separator=",", formatter={'float_kind':'{:e}'.format})
        except Exception as inst:
            print('fallo, fallo, fallo')
        cont += 1
        print(cont)
    df.to_csv('vecAllE3CCODEREngRec.csv', encoding='utf-8')
except Exception as inst:
  print(type(inst))  
  print(inst.args)
  print(inst)

