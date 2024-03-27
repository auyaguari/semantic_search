from sentence_transformers import SentenceTransformer
import torch
from transformers import AutoTokenizer
from transformers import AutoModel


class Vectorizador():
    __modelo = None
    __device = None
    __tokenizer = None
    def __init__(self, modelo, tokenizer):
        
        self.__device =  "cuda:0" if torch.cuda.is_available() else "cpu"
        newmodel = torch.load(modelo)
        self.__tokenizer = AutoTokenizer.from_pretrained(tokenizer)
        self.__modelo = newmodel.bert
    def vectorizar(self, cadena):
        inputs = self.__tokenizer(cadena, return_tensors="pt").to(self.__device)
        self.__model.eval()
        self.__model = self.__model.to(self.__device)
        sentence_embeddings = self.__model(**inputs)
        sentence_embeddings = sentence_embeddings[1]
        sentence_embeddings = sentence_embeddings.to('cpu').detach().numpy()[0]
        return sentence_embeddings