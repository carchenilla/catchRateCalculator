# -*- coding: utf-8 -*-


from PyQt5.QtCore import QRect, QMetaObject, QObject
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QApplication, QFormLayout, QWidget, QLabel, QComboBox, QSizePolicy, QSpacerItem, QLineEdit, QTextBrowser, QPushButton, QDialog


def _fromUtf8(s):
    return str(s)

try:
    _encoding = QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(430, 486)
        icon = QIcon()
        icon.addPixmap(QPixmap(_fromUtf8("images/icon.ico")), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.formLayoutWidget_2 = QWidget(Dialog)
        self.formLayoutWidget_2.setGeometry(QRect(230, 80, 181, 131))
        self.formLayoutWidget_2.setObjectName(_fromUtf8("formLayoutWidget_2"))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_5 = QLabel(self.formLayoutWidget_2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_5)
        self.ball_box = QComboBox(self.formLayoutWidget_2)
        self.ball_box.setObjectName(_fromUtf8("ball_box"))
        self.ball_box.addItem(_fromUtf8(""))
        self.ball_box.addItem(_fromUtf8(""))
        self.ball_box.addItem(_fromUtf8(""))
        self.ball_box.addItem(_fromUtf8(""))
        self.ball_box.addItem(_fromUtf8(""))
        self.ball_box.addItem(_fromUtf8(""))
        self.ball_box.addItem(_fromUtf8(""))
        self.ball_box.addItem(_fromUtf8(""))
        self.ball_box.addItem(_fromUtf8(""))
        self.ball_box.addItem(_fromUtf8(""))
        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.ball_box)
        self.label_6 = QLabel(self.formLayoutWidget_2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_6)
        self.status_box = QComboBox(self.formLayoutWidget_2)
        self.status_box.setObjectName(_fromUtf8("status_box"))
        self.status_box.addItem(_fromUtf8(""))
        self.status_box.addItem(_fromUtf8(""))
        self.status_box.addItem(_fromUtf8(""))
        self.status_box.addItem(_fromUtf8(""))
        self.status_box.addItem(_fromUtf8(""))
        self.status_box.addItem(_fromUtf8(""))
        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.status_box)
        spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.formLayout_2.setItem(1, QFormLayout.FieldRole, spacerItem)
        spacerItem1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.formLayout_2.setItem(3, QFormLayout.FieldRole, spacerItem1)
        self.captured_edit = QLineEdit(self.formLayoutWidget_2)
        self.captured_edit.setObjectName(_fromUtf8("captured_edit"))
        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.captured_edit)
        self.label = QLabel(self.formLayoutWidget_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label)
        self.formLayoutWidget_3 = QWidget(Dialog)
        self.formLayoutWidget_3.setGeometry(QRect(20, 80, 171, 131))
        self.formLayoutWidget_3.setObjectName(_fromUtf8("formLayoutWidget_3"))
        self.formLayout_3 = QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label_8 = QLabel(self.formLayoutWidget_3)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_8)
        self.pokemon_Name_box = QComboBox(self.formLayoutWidget_3)
        self.pokemon_Name_box.setObjectName(_fromUtf8("pokemon_Name_box"))
        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.pokemon_Name_box)
        spacerItem2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.formLayout_3.setItem(1, QFormLayout.FieldRole, spacerItem2)
        self.label_9 = QLabel(self.formLayoutWidget_3)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_9)
        self.level_edit = QLineEdit(self.formLayoutWidget_3)
        self.level_edit.setObjectName(_fromUtf8("level_edit"))
        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.level_edit)
        self.label_10 = QLabel(self.formLayoutWidget_3)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_10)
        self.hp_edit = QLineEdit(self.formLayoutWidget_3)
        self.hp_edit.setObjectName(_fromUtf8("hp_edit"))
        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.hp_edit)
        self.spriteLabel = QLabel(self.formLayoutWidget_3)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spriteLabel.sizePolicy().hasHeightForWidth())
        self.spriteLabel.setSizePolicy(sizePolicy)
        self.spriteLabel.setText(_fromUtf8(""))
        self.spriteLabel.setObjectName(_fromUtf8("spriteLabel"))
        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.spriteLabel)
        self.textBrowser = QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QRect(20, 260, 391, 192))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.label_3 = QLabel(Dialog)
        self.label_3.setGeometry(QRect(335, 460, 71, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QLabel(Dialog)
        self.label_4.setGeometry(QRect(20, 30, 251, 16))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.logolabel = QLabel(Dialog)
        self.logolabel.setGeometry(QRect(280, 20, 121, 51))
        self.logolabel.setText(_fromUtf8(""))
        self.logolabel.setObjectName(_fromUtf8("logolabel"))
        pixmap = QPixmap("images/logo.png")
        self.logolabel.setPixmap(pixmap)
        self.logolabel.setMask(pixmap.mask())
        self.calculateButton = QPushButton(Dialog)
        self.calculateButton.setGeometry(QRect(340, 230, 72, 23))
        self.calculateButton.setObjectName(_fromUtf8("calculateButton"))

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Calculadora de captura", None))
        self.label_5.setText(_translate("Dialog", "Ball", None))
        self.ball_box.setItemText(0, _translate("Dialog", "Poké Ball", None))
        self.ball_box.setItemText(1, _translate("Dialog", "Super Ball", None))
        self.ball_box.setItemText(2, _translate("Dialog", "Ultra Ball", None))
        self.ball_box.setItemText(3, _translate("Dialog", "Master Ball", None))
        self.ball_box.setItemText(4, _translate("Dialog", "Honor Ball", None))
        self.ball_box.setItemText(5, _translate("Dialog", "Ocaso Ball", None))
        self.ball_box.setItemText(6, _translate("Dialog", "Sana Ball", None))
        self.ball_box.setItemText(7, _translate("Dialog", "Beast Ball", None))
        self.ball_box.setItemText(8, _translate("Dialog", "Gloria Ball", None))
        self.ball_box.setItemText(9, _translate("Dialog", "Nido Ball", None))
        self.label_6.setText(_translate("Dialog", "Status", None))
        self.status_box.setItemText(0, _translate("Dialog", "Ninguno", None))
        self.status_box.setItemText(1, _translate("Dialog", "Dormido", None))
        self.status_box.setItemText(2, _translate("Dialog", "Paralizado", None))
        self.status_box.setItemText(3, _translate("Dialog", "Congelado", None))
        self.status_box.setItemText(4, _translate("Dialog", "Quemado", None))
        self.status_box.setItemText(5, _translate("Dialog", "Envenenado", None))
        self.captured_edit.setText(_translate("Dialog", "0", None))
        self.label.setText(_translate("Dialog", "Nº pkmn capt.", None))
        self.label_8.setText(_translate("Dialog", "Pokemon", None))
        self.label_9.setText(_translate("Dialog", "Nivel", None))
        self.level_edit.setText(_translate("Dialog", "10", None))
        self.label_10.setText(_translate("Dialog", "%HP restante", None))
        self.hp_edit.setText(_translate("Dialog", "100", None))
        self.label_3.setText(_translate("Dialog", "by Carchenilla", None))
        self.label_4.setText(_translate("Dialog", "La calculadora molona del Carche 2.0", None))
        self.calculateButton.setText(_translate("Dialog", "Calculate", None))

