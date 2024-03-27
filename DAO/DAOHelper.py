import psycopg2
class DBHelper:
    __connection = None
    __cursor = None
    def __init__(self):
        self.__connection = psycopg2.connect(user = "postgres",
                                        password = "admin",
                                        host = "localhost",#Clef
                                        #host = "172.21.0.4",
                                        port = "5432",
                                        database = "umls")
        self.__cursor = self.__connection.cursor();
    def query(self, query, params):
       self.__cursor.execute(query, params)
       return self.__cursor;

    def close(self):
        self.__connection.close();