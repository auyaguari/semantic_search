class Atom(object):
    __aui=None
    __str=None
    __cui=None
    def __init__(self, aui, str,cui):
        self.__aui=aui
        self.__cui=cui
        self.__str=str
    @property
    def aui(self):
        return self.__aui
    @aui.setter
    def aui(self, aui):
        self.__aui=aui
    @property
    def cui(self):
        return self.__cui
    @property
    def str(self):
        return self.__str
    