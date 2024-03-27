from DAOHelper import DBHelper
import pandas.io.sql as psql
import psycopg2 as pg

class DAOCorpus(object):
    
    __db = None
    
    def __init__(self):
        self.__db = DBHelper()
        
    def por_vectorizar(self):

        sql = """
            select vec.aui, conso.cui from umls.vectores_clef as vec
            inner join umls.mrconso2023 conso ON vec.aui  = conso.aui
            order by vec.aui limit 10;
        """
        connection = pg.connect("host=localhost dbname=umls user=postgres password=admin")
        dataframe = psql.read_sql(sql, connection)
        return dataframe;   
