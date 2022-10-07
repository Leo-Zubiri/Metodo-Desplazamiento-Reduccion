"""
Instrucción para convertir la ventana .ui en .py
pyuic5 Window.ui -o Window.py
"""
import Analyzer

from statistics import linear_regression
import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "Window.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.btnGenerar.clicked.connect(self.Generar)

        # Área de variables
        self.Rules = []
        self.Variables = set()
        self.Terminales = set()
        self.Inicial = ""
        self.Output = ""
        self.Input = []

        self.analyze = Analyzer.AnalizadorSintactico()
        
    # Área de los Slots

    def Generar(self):
        print("Generando")

        self.Rules = self.txtRules.toPlainText().replace(" ","").split('\n')
        self.Variables = self.txtVariables.toPlainText().replace(" ","").split('\n')
        self.Terminales = self.txtTerminales.toPlainText().replace(" ","").split('\n')
        self.Inicial = self.txtInicial.toPlainText().replace(" ","")
        self.Input = self.txtInput.toPlainText().replace(" ","")

        mapaRulesValores = self.mapearInput(self.Rules) 
        conjVariables = self.conjuntoElementos(self.Variables)  
        conjTerminales = self.conjuntoElementos(self.Terminales)
        nodoInicial = self.Inicial
        cadena = self.Input
        print("Cadena",cadena)

        res = self.analyze.MetodoDesplazamientoReduccion(mapaRulesValores,conjVariables,conjTerminales,nodoInicial,cadena)

        self.txtOutput.setPlainText(res)


    def conjuntoElementos(self,lista = []):
        conjunto = set()
        for linea in lista:
            linea = linea.split(',')
            conjunto.update(set(linea))
        return conjunto
        
    def mapearInput(self,lista=[]):
        reglas = []
        for linea in lista:
            if "->" in linea:
                linea = linea.split('->')
                var = linea[0]
                regla = linea[1]
                reglas.append([var,regla])
        return reglas


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())