from calculatorGUI import *
from PokemonDictionary import *
import math
import sys

ballRatios = {"Great Ball": 1.5, "Ultra Ball": 2, "Master Ball":99999, "Dive Ball": 3.5, "Repeat Ball": 3,
              "Net Ball": 3, "Nest Ball": -1, "Timer Ball": 4, "Quick Ball": 5, "Dusk Ball": 3.5}

statusRatios = {"Asleep": 2.5, "Frozen": 2.5, "None": 1}

powerRatios = [1,1.5,2,2.5,2.5,2.5]

caughtRatios = [0.5,1,1.5,2,2.5]


class MiCalculadora(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.okButton, QtCore.SIGNAL('clicked()'), self.calculateRatio)

    def calculateRatio(self):
        try:
            poke = d.getPokemonByName(str(self.ui.pokemonLine.text().rstrip()))
            level = int(self.ui.levelLine.text())
            hpPerc = int(self.ui.hpLeftLine.text())
            caught = int(self.ui.caughtLine.text())
            ball = self.ui.ballBox.currentText().replace("é","e")
            status = self.ui.statusBox.currentText()
            opower = self.ui.opowerBox.currentIndex()

            if level>100:
                level=100
            if level<=0:
                level=1


            if hpPerc>100:
                hpPerc=100
            if hpPerc<=0:
                hpPerc=1

            pixmap = QtGui.QPixmap("images/minisprites/"+str(poke.getNumber())+".png")
            self.ui.spriteLabel.setPixmap(pixmap)
            self.ui.spriteLabel.setMask(pixmap.mask())



            fullHP = math.floor(((int(poke.getBaseHP())*2+31)*level)/100+level+10)

            curHP = math.floor(fullHP*hpPerc/100)

            ballMod = ballRatios.get(ball)
            if ballMod==None:
                ballMod=1
            elif ballMod==-1:
                aux = [1,math.floor((41-level)/10)]
                ballMod=max(aux)

            statMod = statusRatios.get(status)
            if statMod==None:
                statMod=1.5

            opowMod = powerRatios[opower]

            if caught<=30:
                dexMod=0
            elif caught>600:
                dexMod=2.5
            else:
                dexMod=caughtRatios[caught//150]
                if caught%150==0:
                    dexMod=dexMod-0.5


            x = (((3*fullHP-2*curHP)*poke.getRatio()*ballMod)/(3*fullHP))*statMod*opowMod


            if x>=255:
                self.ui.resultTextBox.setText("Capture will succeed - 100%")
            else:

                critProb = ((min((255,x))*dexMod)/6)/256

                normalCapProb = math.pow(x,(12/16))/63.8124

                resultString = "Normal capture probability of success is: "+str("%.4f"% (normalCapProb*100))+"%."+"\n"+"\n"

                if critProb>0:

                    critCapProb = math.pow(x,(3/16))/2.8263
                    totalProb = (critProb*critCapProb)+((1-critProb)*normalCapProb)

                    resultString = "Probability of critical capture: "+str("%.4f" % (critProb*100))+"%."+"\n"+\
                                   "\n"+"If critical capture, probability of success is: "+str("%.4f" % (critCapProb*100)) +"%.\n"+\
                                   "\n"+resultString+"Which makes a total probability of : "+str("%.4f" % (totalProb*100)) +"%."

                self.ui.resultTextBox.setText(resultString)

        except ValueError as err:
            self.ui.resultTextBox.setText("A field was left blank. Please fill every field."+"\n"+"\n"+str(err))
        except AttributeError as err:
            self.ui.resultTextBox.setText("No pokémon exists with that name, or maybe you entered a strange character in a field."+"\n"+"\n"+
                                          "Please check again every field before pressing the Calculate button")



if __name__=="__main__":
    d = CatchRatioDictionary("dataDictionary")
    app = QtGui.QApplication(sys.argv)
    myapp = MiCalculadora()
    myapp.show()
    sys.exit(app.exec_())



