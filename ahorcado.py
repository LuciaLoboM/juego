#menu principal
#su entrada es el numero de jugadores, y su salida es elegir el inicio del juego 1 o juego 2

def menu1():
    print("¡Bienvenido!")
    print("Introduce 'S' para salir ")
    n_jugadores=int(input("Introduce el numero de jugadores: "))
    if n_jugadores==1:
        inicio1() #llamar a la funcion de un jugador
    elif n_jugadores==2:
        inicio2()#llamar a la funcion de dos jugadores


    else:
        print("Error \nintentelo de nuevo")
        menu1()
#inicio del juego de un jugador,
def inicio1():
    print ("MODO UN JUGADOR")
    print ("Bienvenido")
    print ("¿Quieres continuar?")
    n=int(input("1. si \t 2. no \n"))
    if n==1:
        juego1()
    elif n==2:
        menu1()
    else:
        print("Error, seleccione 1 ó 2")
        inicio1()
#inicio del juego multijugador
def inicio2():
    print ("MODO multiJUGADOR")
    print ("Bienvenidos")
    print ("¿Quiereis continuar?")
    n=int(input("1. si \t 2. no \n")) #no tengo muy claro si se puede definir la misma variable que en el anterior
    if n==1:
        juego2()
    elif n==2:
        menu1()
    else:
        print("Error")
        inicio2()
#primero definimos la funcion random
import random
#despues definimos los dibujos del ahoracado
AHORCADO = [
    '''
    +---+
    |   |
        |
        |
        |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========
    '''
    ,
    '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
   /|\  |
    /   |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
   /|\  |
    /\  |
        |
    =========
    '''
]
#biblioteca de palabras
palabras = 'bocina comida jugar silla  programacion videojuegos gatos perros ajolote mascota peces flores arbol libros lapiz telefono teclado discos cancion collar anillos sol luna nube juguete españa mexico escuela universidad queretaro hola adios semaforo carro coche moto'.split()
#se define una funcion para que busque las palabras como salida y la bibiloteca de palabras como entradas con la palabra random elige una palabra aleatoria de la lista de palabras, poniendo randint hace que obtengamos una palabra en entre el rango que nos da.
def buscarPalabraAleat(palabras):
    palabraAleatoria = random.randint(0, len(palabras) - 1)
    return palabras[palabraAleatoria]
#Es una funcion de inicio para definir nuevas variables
def inicializarJuego(palabra):
    palabraOculta = '_' * len(palabra) #transforma la palabra en una palabra oculta
    letrasAdivinadas = [] #para las letras que si son adivinadas
    intentosRestantes = len(AHORCADO) - 1  # Numero de intentos restantes
    return palabraOculta, letrasAdivinadas, intentosRestantes
#las entradas son las palabras y las letras que estan siendo adivinadas, y la salida es la palabra con las letras adivinadas.
#con el ciclo for se iterara la letra por la palabra original
def mostrarPalabra(palabra, letrasAdivinadas):
    resultado = ''
    for letra in palabra:
        if letra in letrasAdivinadas:
            resultado += letra
        else:
            resultado += '_'
    return resultado
# esta funcion se encarga de la verificacion, sus entradas es la palabra, la palabra oculta, las letras adivinadas y la letra.
#su salida es la verficacion de la letra la actualizacion de la palabra oculata
#se hacen dos caminos, uno si es correcta y otro si es incorrecta
def adivinarLetra(palabra, palabraOculta, letrasAdivinadas, letra):
    if letra in letrasAdivinadas:
        return palabraOculta, False  # La letra ya fue adivinada
    elif letra in palabra:
        nuevaPalabraOculta = ''
        for i in range(len(palabra)):
            if palabra[i] == letra:
                nuevaPalabraOculta += letra
            else:
                nuevaPalabraOculta += palabraOculta[i]
        return nuevaPalabraOculta, True
    else:
        return palabraOculta, False  # La letra no está en la palabra
#es la ejecucion del juego para un jugador. se llama desde el inicio de un jugador, se tratada la unificaion de todas las funciones antariores.
def juego1():
    palabra = buscarPalabraAleat(palabras).upper()
    palabraOculta, letrasAdivinadas, intentosRestantes = inicializarJuego(palabra)

    while True:
        print(AHORCADO[len(AHORCADO) - intentosRestantes - 1])
        print(f"Palabra: {mostrarPalabra(palabra, letrasAdivinadas)}")
        letra = input("Ingresa una letra: ").upper()

        palabraOculta, acierto = adivinarLetra(palabra, palabraOculta, letrasAdivinadas, letra)
        if acierto:
            letrasAdivinadas.append(letra)
        else:
            intentosRestantes -= 1

        if palabraOculta == palabra:
            print("¡Ganaste! La palabra era:", palabra)
            break
        elif intentosRestantes == 0:
            print("¡Perdiste! La palabra era:", palabra)
            break

menu1()
