class Pokemon:
    def __init__(self,num,name,ratio):
        self.__name=name
        self.__number=num
        self.__ratio=ratio

    def getName(self):
        return self.__name

    def getNumber(self):
        return self.__number

    def getRatio(self):
        return self.__ratio

    def toString(self):
        return "Pokemon no: "+self.__number+" - "+self.__name+" - Ratio: "+self.__ratio