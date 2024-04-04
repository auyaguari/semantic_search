from sentence_transformers import SentenceTransformer
import torch
from transformers import AutoTokenizer
from transformers import AutoModel

#model = SentenceTransformer('paraphrase-multilingual-mpnet-base-v2')
#model = SentenceTransformer('GanjinZero/UMLSBert_ENG')
newmodel = torch.load('/app/CODER/pretrain/output/last_model.pth')
tokenizer = AutoTokenizer.from_pretrained('sentence-transformers/paraphrase-multilingual-mpnet-base-v2')
model = newmodel.bert
import pandas as pd
df = pd.read_csv('allClefAtoms.csv')
device = "cuda:0" if torch.cuda.is_available() else "cpu"
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
            #inputs = tokenizer("Hello, my dog is cute", return_tensors="pt").to(device)
            #print("text:", df['str'][ind])
            inputs = tokenizer(df['str'][ind], return_tensors="pt").to(device)
            model.eval()
            model = model.to(device)
            #print("inputs", inputs)
            #print("**inputs", **inputs)
            sentence_embeddings = model(**inputs)
            sentence_embeddings = sentence_embeddings[1]
            sentence_embeddings = sentence_embeddings.to('cpu').detach().numpy()[0]
            df['tensor'][ind]=sentence_embeddings
            df['tensor2string'][ind]=np.array2string(df['tensor'][ind], separator=",", formatter={'float_kind':'{:e}'.format})
        except Exception as e:
            print(f"AttributeError: {e}")
        cont += 1
        print(cont)
    df.to_csv('vecAllClefAtomsCoderP.csv', encoding='utf-8')
except Exception as inst:
  print(type(inst))  
  print(inst.args)
  print(inst)

