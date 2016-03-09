from bs4 import BeautifulSoup       #BeautifulSoup
from urllib.request import urlopen  #to open urls
import pickle                       #Pickle to store de dictionary of pokemon
from Pokemon import Pokemon         #Pokemon class, obviously

class PokemonDictionary:

    def __init__(self,path=None):      #path parameter to check if we load from html or file
        if path!=None:
            self.__dict=self.__loadDictionaryFromFile(path)
        else:
            self.__dict=self.__getDictionaryfromHtml()

    def getPokemonByName(self,name):        #get pokemon by name
        return self.__dict.get(name)

    def getPokemonDictionary(self):         #get actual dictionary (should it be private?)
        return self.__dict

    def saveDictionaryToFile(self):             #save dictionary to file, just in case
        with open("dataDictionary.p",'wb') as fp:
            pickle.dump(self.__dict,fp)


    def __getDictionaryfromHtml(self):
        print("Creating data from scratch")
        print("It may take a while depending on your web connection")
        print("Go watch some animus or anything")
        print()
        counter = 0

        pokemonDictionary={}    #Create dictionary
        page=urlopen("http://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_catch_rate")   #open URL
        soup = BeautifulSoup(page.read(),"lxml")            #open html with ratio table

        tabla = soup.table.contents[1].contents[1].contents[1].contents     #navigate to ratio table
        for i in range(3,len(tabla),2):     #extract from each row name, num, ratio and go to the other page to check the base HP
            num = int(tabla[i].th.string.strip(" "))
            name = tabla[i].a["title"].strip(" ")
            ratio = int(tabla[i].find_all("td")[-1].contents[0].strip(" "))

            print("Found pokemon "+name+". Going to check his base HP")
            #go check the base HP

            try:
                page2=urlopen("http://bulbapedia.bulbagarden.net/wiki/"+name.replace(" ","_")+"_%28Pok%C3%A9mon%29")
                soup2 = BeautifulSoup(page2.read(),"lxml")
                for tab in soup2.find_all("table"):     #navigate to base stat table
                    if len(tab.find_all("th"))>=2:
                        myTag = tab.find_all("th")[1]       #check for table with more than 2 headers
                        try:
                            if (myTag["style"]=="background: #FF5959; width: 30px;"):       #try to locate Base HP using style of cell
                                hp = int(myTag.string.rstrip().strip(" "))
                                break       #if found, we break out of the loop
                        except KeyError as err:         #possible exceptions we ignore if the header has no style key
                            pass
                        except AttributeError as err:   #possible exceptions we ignore if the header has no string value
                            pass
            except UnicodeEncodeError as err:
                if num==32:         #male nidoran
                    hp=46
                elif num==29:      #female nidoran
                    hp=55

            print("Found base HP of pokemon "+name+". Creating data and adding to dictionary")
            counter+=1
            print(str("%.2f" % (100*counter/721))+"% completed")
            print()

            poke = Pokemon(num,name,ratio,hp)       #create pokemon object
            pokemonDictionary[poke.getName()]=poke      #add pokemon to dictionary

        print("All Pokemon data were added. Done!")
        return(pokemonDictionary)


    def __loadDictionaryFromFile(self,path):
        try:
            return(pickle.load(open(path+".p","rb")))
        except IOError as err:
            print("Problem while loading file - "+str(err))
        except pickle.PickleError as err:
            print("Problem with pickle - "+str(err))



if __name__=="__main__":        #auxiliar main to store dictionary to file
    d = PokemonDictionary("dataDictionary")
    #d = CatchRatioDictionary()
    #d.saveDictionaryToFile()
    #print(len(d.getPokemonDictionary()))
    for p in d.getPokemonDictionary().values():
        print(p.toString())
    print()
    poke = d.getPokemonByName("Mantyke")
    print(str(poke.getBaseHP()))