
from Servicios.VectorizadorServicio import Vectorizador

if __name__ == '__main__':

    vectorizador =  Vectorizador("../output/last_model.pth",'sentence-transformers/paraphrase-multilingual-mpnet-base-v2' )
    vect = vectorizador("Hola mundo")
    print ("que paso")
    print(vect)
    