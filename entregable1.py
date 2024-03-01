#menu principal
def menu1():
    print("¡Bienvenido!")
    print("Introduce el numero de jugadores: ")
    print("Introduce 'S' para salir ")
    n_jugadores=int(input())
    if n_jugadores==1:
        inicio1() #llamar a la funcion de un jugador
    elif n_jugadores==2:
        inicio2()#llamar a la funcion de dos jugadores
    else:
        print("Error \nintentelo de nuevo")
        menu1()
#inicio del juego
def inicio1():
    print ("MODO UN JUGADOR")
    print ("Bienvenido")
    print ("¿Quieres continuar?")
    print ("1. si \t 2. no \n")
    n=int(input())
    if n==1:
        juego1()
    elif n==2:
        menu1()
    else:
        print("Error")
        inicio1()
#inicio del juego multijugador
def inicio2():
    print ("MODO multiJUGADOR")
    print ("Bienvenidos")
    print ("¿Quiereis continuar?")
    print ("1. si \t 2. no \n")
    n=int(input()) #no tengo muy claro si se puede definir la misma variable que en el anterior
    if n==1:
        juego2()
    elif n==2:
        menu1()
    else:
        print("Error")
        inicio2()
#en esta funcion correra el funcionamiento del juego para una persona
def juego1():
    palabra_oculta='ARBOL'
    print('_ '*len(palabra_oculta))
    L=input("Introduce una letra")
    if L=="A":
        print('A _ _ _ _')
