#primero definimos la funcion random
import random

#menu principal
#su entrada es el numero de jugadores, y su salida es elegir el inicio del juego 1 o juego 2
def menu1():
    print("---¡Bienvenido!---")
    print("Introduce 'S' para salir ")
    print("Para leer instrucciones pulse 3")
    n_jugadores=int(input("Introduce el numero de jugadores: "))
    if n_jugadores==1:
        inicio1() #llamar a la funcion de un jugador
    elif n_jugadores==2:
        inicio2()#llamar a la funcion de dos jugadores
    elif n_jugadores==3:#abre y lee las instrucciones
        file_instrucciones='intrucciones.txt'
        with open(file_instrucciones,"r") as file:
            contenido=file.read()
            print(f"Contenido de {file_instrucciones}:\n{contenido}")
        menu1()
    else:
        print("Error \nintentelo de nuevo")
        menu1()
#inicio del juego de un jugador,
def inicio1():
    print ("---MODO UN JUGADOR---")
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
    print ("---MODO multiJUGADOR---")
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
#biblioteca de palabras, en este apartado voy a añ
p_numeros=['uno','dos','tres','cuatro','cinco','seis','siete','ocho','nueve','diez','once','doce','trece','catorce','quince','veinte','treinta','cuarenta','cincuenta','sesenta','ochenta','noventa','cien']
p_paises=['mexico','egipto','grecia','india','dinamarca','españa','albania','argentina','brasil','colombia','australia','canada','honduras','francia','italia','portugal','marruecos','bolivia,''china','japon','eeuu','alemania','bielorrusia','rusia']
p_colores=['rojo','amarillo','verde','morado','marron','negro','blanco','rosa','naranja','azul','salmon','coral','gris','violeta','cian']
p_animales=['leon','elefante','tigre','jirafa','cebra','koala','delfin','aguila','oso','serpierte','hipopotamo','lobo','rinoceronte','mono','chimpance','babuino','puma','panda','gorila','flamenco','nutria','pavo','ajolote','armadillo','puercoespin','guepardo','murcielago','lemur','narval','wombat']
p_frutas=['manzana','platano','fresa','uva','kiwi','mango','tamarindo','naranja','piña','sandia','melon','cereza']
p_profesiones=['medico','enfermero','maestro','profesor','cuidador','ingeniero','mecanico','electricista','fontanero','abogado','juez','fiscal','escritor','poeta','musico','cantante','actor','compositor','chef','fotografo','presentador']
p_deportes=['futbol','baloncesto','tocho','tenis','padel','natacion','atletismo','ciclismo','voleibol','golf','criquet','beisbol','esgrima']
p_instrumentos=['guitarra','piano','violin','flauta','trompeta','bateria','saxofon','violonchelo','clarinete','xilofono']
p_en=['agua','fuego','tierra','aire','sol','luna','estrella','viento','rocas','arena']
p_dificiles=['xorxal','lixivia','pixel','niquel','bucelario','cicuta','yuxtaposicion','fulgido','marmol']
#hacemos una matriz que contenga todas las palabras anteriores
palabras = [p_numeros,p_paises,p_colores,p_animales,p_frutas,p_profesiones,p_deportes,p_instrumentos,p_en,p_dificiles]
#la siguiente funcion simplemente despliegla el menu de palabras que hay
def menuOpcionesDePalabras():
    print('-----OPCIONES DE PALABRAS-----')
    print('1.Números')
    print('2.Paises')
    print('3.Colores')
    print('4.Animales')
    print('5.Frutas')
    print('6.Profesiones')
    print('7.Deportes')
    print('8.Instrumentos')
    print('9.Elementos Naturales')
    print('10.Dificiles')
#la siguiente funcion despliegla el menu de palabras que hay, recoge la elecion del usuario y termina eligiendo la palabra oculta final
def opcionesDePalabras(palabras):
    menuOpcionesDePalabras()
    eleccion=int(input('Elige una opcción: '))
    if eleccion==1:
        lista=palabras[0]
    elif eleccion==2:
        lista=palabras[1]
    elif eleccion==3:
        lista=palabras[2]
    elif eleccion==4:
        lista=palabras[3]
    elif eleccion==5:
        lista=palabras[4]
    elif eleccion==6:
        lista=palabras[5]
    elif eleccion==7:
        lista=palabras[6]
    elif eleccion==8:
        lista=palabras[7]
    elif eleccion==9:
        lista=palabras[8]
    elif eleccion==10:
        lista=palabras[9]
    else:
        print('¡¡¡¡¡¡¡¡¡¡error!!!!!!!!!!!')
    return buscarPalabraAleat(lista)
#se define una funcion para que busque las palabras como salida y la bibiloteca de palabras como entradas con la palabra random elige una palabra aleatoria de la lista de palabras, poniendo randint hace que obtengamos una palabra en entre el rango que nos da.
def buscarPalabraAleat(lista):
    palabraAleatoria = random.randint(0, len(lista) - 1)
    return lista[palabraAleatoria]
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
    palabra = opcionesDePalabras(palabras)
    palabraOculta, letrasAdivinadas, intentosRestantes = inicializarJuego(palabra)

    while True:
        print(AHORCADO[len(AHORCADO) - intentosRestantes - 1])
        print(f"Palabra: {mostrarPalabra(palabra, letrasAdivinadas)}")
        letra = input("Ingresa una letra: ").lower()

        palabraOculta, acierto = adivinarLetra(palabra, palabraOculta, letrasAdivinadas, letra)
        if acierto:
            letrasAdivinadas.append(letra)
        else:
            intentosRestantes -= 1
        if palabraOculta == palabra:
            print("¡Ganaste! La palabra era:", palabra)
            break
        elif intentosRestantes == 0:
            print(AHORCADO[6])
            print("¡Perdiste! La palabra era:", palabra)
            break
#En esta funcion, se ejecuta el juego para dos, he tenido que añadir otro inicio del juego tambien para que pudiera funcionar bien
def juego2():
    nombre1 = input("Ingrese el nombre del primer jugador: ")
    nombre2 = input("Ingrese el nombre del segundo jugador: ")
    palabra = opcionesDePalabras(palabras)
    palabraOculta, letrasAdivinadas, intentosRestantes1, intentosRestantes2 = inicializarJuego2(palabra)
    j=0
    while True:
        print(f"Palabra: {mostrarPalabra(palabra, letrasAdivinadas)}")
        if (j % 2 == 0):
            print(AHORCADO[len(AHORCADO) - intentosRestantes1 - 1])
            letra = input(f"{nombre1}, ingresa una letra: ").lower()
            intentosRestantes1 -= 1
        else:
            print(AHORCADO[len(AHORCADO) - intentosRestantes2 - 1])
            letra = input(f"{nombre2}, ingresa una letra: ").lower()
            intentosRestantes2 -= 1
        palabraOculta, acierto = adivinarLetra(palabra, palabraOculta, letrasAdivinadas, letra)
        if acierto:
            letrasAdivinadas.append(letra)
        if palabraOculta == palabra:
            print(f"¡Ganaste, {nombre1}! La palabra era:", palabra)
            break
        elif intentosRestantes1 == 0:
            print(f"¡Ganaste, {nombre2}! La palabra era:", palabra)
            break
        elif intentosRestantes2 == 0:
            print(f"¡Ganaste, {nombre1}! La palabra era:", palabra)
            break
        j+=1
#es una adaptacion de iniciarjuego2 para que pueda correr con dos personas
def inicializarJuego2(palabra):
    palabraOculta = '_' * len(palabra) #transforma la palabra en una palabra oculta
    letrasAdivinadas = [] #para las letras que si son adivinadas
    intentosRestantes1 = len(AHORCADO) - 1# Numero de intentos restantes
    intentosRestantes2= len(AHORCADO)-1
    return palabraOculta, letrasAdivinadas, intentosRestantes1, intentosRestantes2
menu1()
