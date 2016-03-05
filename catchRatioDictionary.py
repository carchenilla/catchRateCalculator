from bs4 import BeautifulSoup       #BeautifulSoup to navigate in the HTML file
import pickle                       #Pickle to store de dictionary of pokemon
from Pokemon import Pokemon         #Pokemon class, obviously

class CatchRatioDictionary:

    def __init__(self,path,mode=None):      #mode parameter to check if we load from html or file
        if mode==None:
            self.__dict=self.__loadDictionaryFromFile(path)
        else:
            self.__dict=self.__getListfromHtml(path)

    def getPokemonByName(self,name):        #get pokemon by name
        return self.__dict.get(name)

    def getPokemonDictionary(self):         #get actual dictionary (should it be private?)
        return self.__dict

    def saveDictionaryToFile(self):             #save dictionary to file, just in case
        with open("dataDictionary.p",'wb') as fp:
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



if __name__=="__main__":        #auxiliar main to store dictionary to file
    d = CatchRatioDictionary("webpage","html")
    d.saveDictionaryToFile()
    print(len(d.getPokemonDictionary()))