import math, sys
from GUI_files.calculatorGUI import *
from data_types.PokemonDictionary import *

ballRatios = {"Super Ball": 1.5, "Ultra Ball": 2, "Master Ball":99999, "Ocaso Ball": 3.5}

statusRatios = {"Dormido": 2, "Congelado": 2, "Ninguno": 1}

caughtRatios = [0.5,1,1.5,2,2.5]

class MiCalculadora(QDialog):
    def __init__(self, dict, parent=None):
        self.d = dict
        QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        names = sorted([str(p.getName()) for p in self.d.getPokemonDictionary().values()])
        self.ui.pokemon_Name_box.addItems(names)
        self.ui.calculateButton.clicked.connect(self.calculateRatio)
        self.ui.calculateButton.clicked.connect(self.calculateRatio)

    def calculateRatio(self):
        try:
            poke = self.d.getPokemonByName(str(self.ui.pokemon_Name_box.currentText()))
            level = int(self.ui.level_edit.text())
            hpPerc = int(self.ui.hp_edit.text())
            caught = int(self.ui.captured_edit.text())
            ball = self.ui.ball_box.currentText().replace("é","e")
            status = self.ui.status_box.currentText()

            if level>100:
                level=100
            elif level<=0:
                level=1


            if hpPerc>100:
                hpPerc=100
            elif hpPerc<=0:
                hpPerc=1

            if caught>802:
                caught = 802
            elif caught<0:
                caught = 0


            try:
                pixmap = QPixmap("images/minisprites/"+str(poke.getNumber())+".png")
                self.ui.spriteLabel.setPixmap(pixmap)
                self.ui.spriteLabel.setMask(pixmap.mask())
            except IOError as err:
                self.ui.textBrowser.append("Cannot load sprite for "+str(poke.getName()))

            fullHP = math.floor(((int(poke.getBaseHP())*2+31)*level)/100+level+10)

            curHP = math.floor(fullHP*hpPerc/100)


            if ball=="Nido Ball":
                ballMod = max([1, 8-0.2*(level-1)])
            elif ball=="Beast Ball":
                if (str(poke.getName())) in ["Nihilego", "Buzzwole", "Pheromosa", "Xurkitree", "Celesteela", "Kartana", "Guzzlord"]:
                    ballMod = 5
                else:
                    ballMod = 0.1
            else:
                ballMod = ballRatios.get(ball)
                if ballMod == None:
                    ballMod = 1

            statMod = statusRatios.get(status)
            if statMod==None:
                statMod=1.5

            if caught<=30:
                dexMod=0
            elif caught>600:
                dexMod=2.5
            else:
                dexMod=caughtRatios[caught//150]
                if caught%150==0:
                    dexMod=dexMod-0.5


            x = (((3*fullHP-2*curHP)*poke.getRatio()*ballMod)/(3*fullHP))*statMod


            if x>=255:
                self.ui.textBrowser.setText("Capture will succeed - 100%")
            else:

                critProb = ((min((255,x))*dexMod)/6)/256

                normalCapProb = math.pow(x/255,0.75)

                resultString = "Normal capture probability of success is: "+str("%.4f"% (normalCapProb*100))+"%."+"\n"+"\n"

                if critProb>0:

                    critCapProb = math.pow(x/255,(3/16))
                    totalProb = (critProb*critCapProb)+((1-critProb)*normalCapProb)

                    resultString = "Probability of critical capture: "+str("%.4f" % (critProb*100))+"%."+"\n"+\
                                   "\n"+"If critical capture, probability of success is: "+str("%.4f" % (critCapProb*100)) +"%.\n"+\
                                   "\n"+resultString+"Which makes a total probability of : "+str("%.4f" % (totalProb*100)) +"%."

                self.ui.textBrowser.setText(resultString)

        except ValueError as err:
            self.ui.textBrowser.setText("A field was left blank. Please fill every field."+"\n"+"\n"+str(err))
        except AttributeError as err:
            self.ui.textBrowser.setText("No pokémon exists with that name, or maybe you entered a strange character in a field."+"\n"+"\n"+
                                          "Please check again every field before pressing the Calculate button")



if __name__=="__main__":
    app = QApplication(sys.argv)
    myapp = MiCalculadora(dict=PokemonDictionary("dataDictionary"))
    myapp.show()
    sys.exit(app.exec_())



