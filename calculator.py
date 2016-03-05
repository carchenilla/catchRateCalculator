from bs4 import BeautifulSoup
import pickle
from Pokemon import Pokemon

class CatchRatioCalculator:

    def __init__(self,path,mode=None):
        if mode==None:
            self.__dict=self.__loadDictionaryFromFile(path)
        else:
            self.__dict=self.__getListfromHtml(path)

    def getPokemonByName(self,name):
        return self.__dict.get(name)

    def getPokemonDictionary(self):
        return self.__dict

    def saveDictionaryToFile(self):
        with open("catchRatioDictionary.p",'wb') as fp:
            pickle.dump(self.__dict,fp)


    def __getListfromHtml(self,htmlPath):
        pokemonDictionary={}
        with open(htmlPath + ".html", "r") as file:
            soup = BeautifulSoup(file,"lxml")
            tabla = soup.table.contents[1].contents[1].contents[1].contents
            for i in range(3,len(tabla),2):
                poke = Pokemon(tabla[i].th.string.strip(" "),tabla[i].a["title"].strip(" "),tabla[i].find_all("td")[-1].contents[0].strip(" "))
                pokemonDictionary[poke.getName()]=poke
        return(pokemonDictionary)


    def __loadDictionaryFromFile(self,path):
        try:
            return(pickle.load(open(path+".p","rb")))
        except IOError as err:
            print("Problem while loading file - "+str(err))
        except pickle.PickleError as err:
            print("Problem with pickle - "+str(err))



if __name__=="__main__":
    d = CatchRatioCalculator("webpage","html")
    print(len(d.getPokemonDictionary()))