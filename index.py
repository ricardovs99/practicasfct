#ejercicio1

print ( "BIENVENIDO A EMPAREJANDO.COM" )

print ("Necesitamos conocer algunos datos sobre ti para encontrar tu pareja ideal")

nombre  =  input ( "Escribe tu nombre:" )
ano  =  int ( input ( "�A�o de nacimiento?" ))
taburete  =  input ( "�Te gusta Taburete? [Si / No]" )
edad  =  2020 - ano

print ( "Hola" + nombre + ". Si no me equivoco tienes" , edad , "a�os." )

if ( taburete == "Si"  o  taburete == "Si"  o  taburete == "S"  o  taburete == "s" ):
    print ( "OK boomer. Lo tuyo va a ser un caso dif�cil" )
elif:
    print ( "Bueno, al menos es un comienzo. Veremos qu� se puede hacer contigo" )

#ejercicio2

contador = 1

mientras que ( contador < edad ):
    print ( "Que no cumple" , contador )
    contador + = 1

print ( "�Que si cumple" , contador , "!" )

#ejercicio3

print ( "Hola" + nombre + ". Si no me equivoco tienes" , edad , "a�os." )

if  taburete  en ( 'Si' , 'S�' , 'S' , 's' , 'si' , 's�' ):
    print ( "OK boomer. Lo tuyo va a ser un caso dif�cil" )
elif:
    print ( "Bueno, al menos es un comienzo. Veremos qu� se puede hacer contigo" )
    
    
para  contador  en  rango ( 1 , edad ):
    print ( "Que no cumple" , contador )

print ( "�Que si cumple" , edad , "!" )

#ejercicio4

Obtener el a�o para hacer el c�lculo de la edad
ano_actual = fecha . hoy (). a�o
edad  =  ano_actual - ano

print ( "Hola" + nombre + ". Si no me equivoco tienes" , edad , "a�os." )


if  taburete  en ( 'Si' , 'Si' , 'S' , 's' , 'si' , 's�' ):
    tab�  =  verdadero
elif:
    tab�  =  falso

if ( tab� ):
    print ( "OK boomer. Lo tuyo va a ser un caso dif�cil" )
elif:
    print ( "Bueno, al menos es un comienzo. Veremos qu� se puede hacer contigo" )


usuario = [ nombre , edad , tab� ]

para  dato  en  usuario :
    imprimir ( dato )

#ejercicio5

usuario = {"nombre" : nombre ,
           "edad" : edad ,
           "taburete" : taburete}

para  dato  en  usuario . valores ():
    imprimir ( dato )
    
#ejercicio6

alfabetoMinus = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
     'm', 'n', '�', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alfabetoMayus = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
     'M', 'N', '�', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

'''
Funci�n codificar
Palabra: String a codificar
Avance: int posiciones que avanza en el alfabeto
'''
def Codificar(Palabra, Avance):
    Clave = ''
    Tope = len(alfabetoMayus)
    Posicion = 0
    for letra in Palabra:
        for i in range(Tope):
            if (i + Avance < Tope):
                Posicion = i + Avance
            else:
                Posicion = abs((Tope - i) - Avance)
            if letra == alfabetoMinus[i]:
                Clave = Clave + alfabetoMinus[Posicion]
            elif letra == alfabetoMayus[i]:
                Clave = Clave + alfabetoMayus[Posicion]
    return Clave

#***************************************
Clave = Codificar("Hola", 3)
print(Clave)

#ejercicio7

horas = float(input("Introduce tus horas de trabajo: "))
coste = float(input("Introduce lo que cobras por hora: "))
paga = round(horas * coste, 3)
print("Tu paga es " + str(paga))

#ejercicio8

n = int(input("Introduce un n�mero entero: "))
suma = n * (n + 1) / 2
print("La suma de los primeros numeros enteros desde 1 hasta " + str(n) + " es " + str(suma))
    