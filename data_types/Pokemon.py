class Pokemon:          #Pokemon class to store Pokemon data
    def __init__(self,num,name,ratio,hp):
        self.__name=name
        self.__number=num
        self.__ratio=ratio
        self.__baseHP=hp

    def getName(self):
        return self.__name

    def getNumber(self):
        return self.__number

    def getRatio(self):
        return self.__ratio

    def getBaseHP(self):
        return self.__baseHP

    def toString(self):
        return "Pokemon no: "+str(self.__number)+" - "+self.__name+" - Base HP: "+str(self.__baseHP)+" - Ratio: "+str(self.__ratio)