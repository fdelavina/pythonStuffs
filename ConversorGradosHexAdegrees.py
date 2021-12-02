# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 09:17:29 2021

@author: Francisco

                Ejemplo 

    para pasar de horas min seg a grados

                Terminal:
python ConversorGradosHexAdegrees.py 0 5 18 58.286
                            

                    Salida  
****** Conversor de Degree a Grados Hexagesimales y viceversa ***

Conversion de Grados Hexagesimales a Degree
Con hora=  5.0  Con minuto=  18.0  y con segundo=  58.286  el resultado en degree es  5.316190555555555




para parar de grados a horas min y segundos

python ConversorGradosHexAdegrees.py 1 42.4224121


"""

import sys

def GradosHexToDegree(GradosHex):

    return GradosHex[0] + GradosHex[1]/60 + GradosHex[2]/3600
    
def DegreeToGradosHex(degree):
    
    GradosHex = []
    
    GradosHex.append(int(degree)) #horas
    
    minutos= (degree-GradosHex[0])*60
    GradosHex.append(int(minutos)) #minutos

    segundos = (minutos-GradosHex[1])*60
    GradosHex.append(segundos)
    
    return GradosHex
    

if __name__ == "__main__":
    print(" ****** Conversor de Degree a Grados Hexagesimales y viceversa *** \n")

    if sys.argv[1] == "0": #Conversion de Grados Hexagesimales a Degree
        print("Conversion de Grados Hexagesimales a Degree")
        hora    = float(sys.argv[2])
        minuto  = float(sys.argv[3])
        segundo = float(sys.argv[4])
        
        GradosHex=[hora,minuto, segundo]
        
        Degree= GradosHexToDegree(GradosHex)
        print("Con hora= ",hora," Con minuto= ",minuto," y con segundo= ",segundo,\
              " el resultado en degree es ", Degree)
    if sys.argv[1] == "1": # Conversion de Degree a Grados Hexagesimales
        print("Conversion de Degree a Grados Hexagesimales")
        degree = float(sys.argv[2]     )
        GradosHex = DegreeToGradosHex(degree)
        
        print("Con degree = ",degree," el resultado es ","hora= ", GradosHex[0],"minuto= ", GradosHex[1],"segundo= ", GradosHex[2] )
        