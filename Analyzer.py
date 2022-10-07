import re # Regular Expressions
class AnalizadorSintactico:
    VARIABLES = set()
    TERMINALES = set()
    INICIAL = ""
    RULES = []
    RESULT = []
    PILA = []
    ENTRADA = []
    ACCION = []
    CADENA = ""
    ITERACIONES = 0
    CADENA_RES = ""

    def MetodoDesplazamientoReduccion(self,_rules,_variables,_terminales,_inicial,_cadena):
        self.RULES = _rules
        self.VARIABLES = _variables
        self.TERMINALES = _terminales
        self.INICIAL = _inicial
        self.CADENA = _cadena
        
        self.VARIABLES = list(self.VARIABLES)
        self.VARIABLES.sort(reverse=True)

        self.TERMINALES = list(self.TERMINALES)
        self.TERMINALES.sort(reverse=True)

        print(self.CADENA)

        return self.CalcularMDR()

        
    def CalcularMDR(self):

        self.PILA = "$"
        self.ENTRADA = self.CADENA
        self.ACCION = "Desplazamiento"

        print("------------------------------------")

        self.CADENA_RES += "{:<10} {:<17} {:<10} \n".format("PILA","ENTRADA","ACCION")

        while self.ENTRADA != "" or cambioDetectado == True:

            self.CADENA_RES += "{:<10} {:<17} {:<10} \n".format(self.PILA,self.ENTRADA+"$",self.ACCION)

            cambioDetectado = False
            self.ITERACIONES += 1

            for regla in self.RULES:
                #Si se puede aplicar una regla en la pila
                if regla[1] in self.PILA:
                    # Reemplazar la regla por la variable correspondiente
                    self.PILA = self.PILA.replace(regla[1],regla[0])
                    cambioDetectado = True
                    self.ACCION = "REGLA "+regla[1]


            # Pasar siguiente elemento a la izquierda

            # Si es una variable
            if cambioDetectado == False:
                for var in self.VARIABLES:
                    if re.search("^{}".format(var), self.ENTRADA):
                        self.PILA = self.PILA + self.ENTRADA[:len(var)] 
                        self.ENTRADA = self.ENTRADA[len(var)::]
                        cambioDetectado = True
                        self.ACCION = "Desplazamiento"

            if cambioDetectado == False:
                # Pasar el terminal
                for T in self.TERMINALES:
                    if T in ["(",")","[","]","+","*","-","/"]:

                        if cambioDetectado == False:
                            # Caracter especial para el REGEX
                            if re.search("^\{}".format(T), self.ENTRADA):
                                self.PILA = self.PILA + self.ENTRADA[:1] 
                                self.ENTRADA = self.ENTRADA[1::]
                                cambioDetectado = True
                                self.ACCION = "Desplazamiento"
                    else:
                        if cambioDetectado == False:
                            if re.search("^{}".format(T), self.ENTRADA):
                                self.PILA = self.PILA + self.ENTRADA[:len(T)] 
                                self.ENTRADA = self.ENTRADA[len(T):]
                                cambioDetectado = True
                                self.ACCION = "Desplazamiento"


        if self.PILA[1:] == self.INICIAL:
            self.CADENA_RES += "CADENA ACEPTADA"
        else: 
            self.CADENA_RES += "CADENA NO ACEPTADA"

        print(self.CADENA_RES)

        return self.CADENA_RES

        