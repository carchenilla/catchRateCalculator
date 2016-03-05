from bs4 import BeautifulSoup
import pickle
from Pokemon import Pokemon


class CatchRateCalculator:
    def __init__(self,htmlPath):
        self.__dictionary=getListfromHtml(htmlPath)

    def __init__(self,filePath):
        self.__dictionary?d


def getListfromHtml(path):
    pokemonDictionary={}
    with open(path + ".html", "r") as file:
        soup = BeautifulSoup(file,"lxml")
        tabla = soup.table.contents[1].contents[1].contents[1].contents
        for i in range(3,len(tabla),2):
            poke = Pokemon(tabla[i].th.string.strip(" "),tabla[i].a["title"].strip(" "),tabla[i].find_all("td")[-1].contents[0].strip(" "))
            pokemonDictionary[poke.getName()]=poke
    return(pokemonDictionary)


def dictionaryToFile(d):
    with open("catchRatioDictionary.p",'wb') as fp:
        pickle.dump(d,fp)



if __name__=="__main__":
    d = getListfromHtml("webpage")
    dictionaryToFile(d)