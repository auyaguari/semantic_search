from sentence_transformers import SentenceTransformer
import torch
from transformers import AutoTokenizer
from transformers import AutoModel
from VectorizadorServicio import Vectorizador

if __name__ == '__main__':
    
    vectorizador =  Vectorizador("last_model.pth",'sentence-transformers/paraphrase-multilingual-mpnet-base-v2' )

