dobleRalla = 4//2
print(dobleRalla)
# // es para una divicion de numeros enteros

con1ralla = 4/2
print(con1ralla)
#esta es una divicion pero para valores float

sonIguales = "casa" == "asca"
print(sonIguales)
#el resultado es false, por que no son iguales, por ende "==" hace una comparacion

probando = 3<5
print(probando)
#resultado es true en la comaracion

negacion = not 3>5
print(negacion)
#el resultado es true por que como puse no es mayor 3 que 5, me confirmo el resultado

logistica = 3>5 and 2<6
print(logistica)
#aqui el resultado es false, por q 3 no es mayor q 5, por ende las dos operqaciones no dan el mismo resultado

disyuncion = 3>5 or 2<6
print(disyuncion)
#aqui me da true por que exactamente uno de las dos operaciones si da el resultado

concatenacion = "yo soy" + " tu padre"
print(concatenacion)
# aqui la + une dos sting, pero hay que recordar poner un espacio entre las doble comilla y el segundo string para que
#no queden las palabras juntas

repeticion = ("ja"*4) + (5*"ji")
print(repeticion)
#la repeticion se cumplen, y da lo mismo el orden de lados que pongas el numero de las veces de repeticion

tipo = type("4")
tipo1 = type(4)
tipo2 = type(4.0)
tipo3 = type(1>5)
print(tipo, tipo1, tipo2, tipo3)
#<class 'str'> <class 'int'> <class 'float'> <class 'bool'> ese es el resultado

Exponensacion =(3**2),(2**3**2)
print(Exponensacion)
# ese es el resultado (9, 512)

modulo = 7%2
print(modulo)
# el modulo es lo que sobra de la divicion por que 7/2 da 6 y me sobra 1, y ese es el resultado que da modulo "1"

distinto = 2!=2
print(distinto)
#el resultado es False por que != significa que no es, pero en este caso 2 si es igual a 2, por ende dice que es falso

resultado1 = 10 + 10 + 10 * 10
print(resultado1)
# el resultado es 120, por que se comienza primero por la multiplicacion y despues por las sumas

unuarios = -3**3
print(unuarios)
#el resultado de esto es 0.037037037037037035 y si fuera, -3**3 el resultado seria -27, a esto se le llama operacione
#operaciones matematicas unarias

ejercicio = "son las " + str(12+3)
print(ejercicio)
#aqui convertimos un calculo en un string poniendo str antes de la operacion y el resultado es "son las 15"

nombre = "dennisse"
edad = 28
print("soy", nombre, end="")
print("y tengo", edad,"años")
print("cumplidos")
#aqui python une las oraciones "soy, nombre" + y "tengo edad años", esto lo une en la misma linea con end=""
#pero siguio la misma linea, que yo le mencione que siguiera, como en las otras lineas no se lo mostre, por ende no lo
# hizo

print("este print",end=":D")
print("no cambia","de linea",end=";")
#este es el resultado de esto "este print:Dno cambia de linea;" aqui podemoas ver que nosotros ponemos agregar
#lo que queramos despues de un "end=", donde este lo agregara y lo unira con la horacion siguiente, la cual tenia salto
#salto de linea


mensaje = "hoy habra"
temp = 34
mensaje2 = "grados"
print(mensaje,temp,mensaje2)
#este print:Dno cambia de linea;hoy habra 34 grados, python le agrega, auyomaticamente espacio a las oraciones
#que yo tenia, y que en print uni pero solo por sus asignaciones, con una ","

print("El tesoro","esta","en",sep="...")
#aqui yo le digo a sep(separacion) que en cada separacion pornga 3 puntos, y es asi como queda
#El tesoro...esta...en   aqui se exeptua la ultima palabra por ser la final

print("El tesoro","esta","en","",sep="...")
#pero aqui quedaria asi: El tesoro...esta...en... , aqui si se le agrega los tres puntos despues del en
#y esto se consigue insertando despues del "en" final, unas entre comillas basias, asi, "".

#ahora veremos input()
#input es para que el computados guarde informacion de entrada desde el usuario, y este se guardara en python
#se guardara donde nosotros designemos input, entonces el computador se detendra, esperara informacion de entrada,
#y luego la guardara en ella ejemplo

nombre = input("¿cual es tu nombre?")
saludos = "hola"
pregunta = "¿como estas?"
print(saludos,nombre,pregunta)
#el resultado fue:
# ¿cual es tu nombre?dennisse
#hola dennisse ¿como estas?
#aqui yo respondi con mi nombre, como usuario

coste_variable = input("costo variable")
coste_fijo ="10"
coste_total =coste_fijo + coste_variable
print(coste_total)
#aqui el resultado dio 103, en vez de 13, y es por que tanto el dato de la variable coste_feijo
#como el que usuario agrego que era un 3 por ejemplo, los leyo como string, por que es asi como los lee
#para que este ocupe valores de numero ya sea int o float, devemos asignarselo de la siguiente manera
#int(input())    float(input())    bool(input())  str(int(input("" + ""))) etc...

coste_variable = int(input("costo variable"))
coste_fijo =10
coste_total =coste_fijo + coste_variable
print(coste_total)
#ahora el resultado que le dio, es 13, si yo como usuario le agrego el 3 como el monto de la variable coste_variable
#en este caso paso de string a int y lo sumo, dandome un valor en int
