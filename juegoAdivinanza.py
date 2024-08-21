import random

def juegoAdivinanza():
    numeroSecreto = random.randint(1,100)
    intentos=0
    adivinado= False #condicion para bucle, para terminar el juego 
    print('bienvenido al juego')
    print('Debes adivinar un número del 1 al 100. Intenta adivinarlo!')

    while not adivinado:
        #solicitar un nro
        adivinanza= input('Elige un número del 1 al 100: ')
        #verificar si la entrada es un nro
        if adivinanza.isdigit(): #devuelve booleano
            adivinanza=int(adivinanza)
            intentos +=1
            if adivinanza< numeroSecreto:
                print(f'El número secreto es mayor a {adivinanza}')
            elif adivinanza > numeroSecreto:
                print(f'el número secreto es menor a {adivinanza}')
            else:
                print(f'Has ganado! el número {adivinanza} es el secreto y lo lograste en {intentos} intentos')
                adivinado=True  
        else:
            print('Introduzca un número valido entre 1 al 100')
            

juegoAdivinanza() 
