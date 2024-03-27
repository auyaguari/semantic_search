from sentence_transformers import SentenceTransformer
import torch
from transformers import AutoTokenizer
from transformers import AutoModel
from VectorizadorServicio import Vectorizador

if __name__ == '__main__':
    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    vectorizador =  Vectorizador("last_model.pth",device)

