from random import randint, choice
import copy

todas_las_cartas = {
    "personajes": ['Juanito', 'Ernesto', 'Antonio', 'Leidy', 'Carlos', 'Señor Sanchez'],
    "armas":  ['Cuchillo', 'Banana', 'Latigo', 'Cañon de guerra', 'Uzi', 'Cuchillo de plastico', 'Lanzacohetes'],
    "lugares": ['Sala', 'Comedor', 'Baño', 'Patio', 'Chochera', 'Azotea', 'Balcon', 'Cancha', 'Lavanderia']
}

datos_juego = copy.deepcopy(todas_las_cartas)

sobre = {
    "personaje": datos_juego['personajes'].pop(randint(0, 5)),
    "arma": datos_juego['armas'].pop(randint(0, 6)),
    "lugar": datos_juego['lugares'].pop(randint(0, 8))
}

jugadores = {
    "jugador1": {
        "nombre": "",
        "cartas": [],
        "hoja": {
            "personajes": [],
            "armas": [],
            "lugares": []
        }
    },
    "jugador2": {
        "nombre": "",
        "cartas": [],
        "hoja": {
            "personajes": [],
            "armas": [],
            "lugares": []
        }
    }
}


def llave_con_items():
    while True:
        random_key = choice(list(datos_juego.keys()))
        if datos_juego[random_key]:
            return random_key


def barajar():
    for _ in range(7):
        random_key = choice(list(datos_juego.keys()))
        if datos_juego[random_key]:
            carta_jugador1 = datos_juego[random_key].pop(
                randint(0, len(datos_juego[random_key]) - 1))
            jugadores['jugador1']['cartas'].append(carta_jugador1)
        else:
            random_key = llave_con_items()
            carta_jugador1 = datos_juego[random_key].pop(
                randint(0, len(datos_juego[random_key]) - 1))
            jugadores['jugador1']['cartas'].append(carta_jugador1)

        random_key = choice(list(datos_juego.keys()))
        if datos_juego[random_key]:
            carta_jugador2 = datos_juego[random_key].pop(
                randint(0, len(datos_juego[random_key]) - 1))
            jugadores['jugador2']['cartas'].append(carta_jugador2)
        else:
            random_key = llave_con_items()
            carta_jugador2 = datos_juego[random_key].pop(
                randint(0, len(datos_juego[random_key]) - 1))
            jugadores['jugador2']['cartas'].append(carta_jugador2)


def informacion_juego():
    print(f"todas las cartas: {todas_las_cartas}")
    print(f"contenido del sobre: {sobre}")
    print(f"informacion Jugador 1: {jugadores['jugador1']}")
    print(f"informacion Jugador 2: {jugadores['jugador2']}")
    print(f"cartas sin jugar: {datos_juego}")


def menu():
    print("Opciones:")
    print("a) Realizar una suposición")
    print("b) Realizar una acusación")
    print("c) Ver hoja de usuario")
    print("d) Salir del juego")

def obtener_rival(jugador):
    if jugador == 'jugador1':
        return 'jugador2'
    elif jugador == 'jugador2':
        return 'jugador1'

def verificar_cartas_jugador_rival(jugador, personaje, arma, lugar):
    if personaje in jugadores[jugador]['cartas']:
        print(f'El jugador {jugadores[jugador]["nombre"]} tiene {personaje} en su baraja')
    elif arma in jugadores[jugador]['cartas']:
        print(f'El jugador {jugadores[jugador]["nombre"]} tiene {arma} en su baraja')
    elif lugar in jugadores[jugador]['cartas']:
        print(f'El jugador {jugadores[jugador]["nombre"]} tiene {lugar} en su baraja')
    else:
        print(f'Ninguna de las cartas que anotaste en tu hoja las tiene {jugadores[jugador]["nombre"]} en su baraja.')

def mostrar_hoja_jugador(jugador):
    hoja = jugadores[jugador]['hoja']
    personajes_registrados = len(hoja['personajes'])
    armas_registradas = len(hoja['armas'])
    lugares_registrados = len(hoja['lugares'])
    
    if verificar_tabulate():
        from tabulate import tabulate
        # Convierte el diccionario en una lista de listas
        tabla = [['Personaje', 'Arma', 'Lugar']]
        if personajes_registrados == lugares_registrados == armas_registradas:
            for idx in range(personajes_registrados):
                tabla.append([hoja['personajes'][idx], hoja['armas'][idx], hoja['lugares'][idx]])
            print(tabulate(tabla, headers='firstrow', tablefmt='pretty'))
    else:
        if personajes_registrados == lugares_registrados == armas_registradas:
            print('|Personaje|\t|Arma|\t|Lugar|')
            for idx, item in enumerate(hoja['personajes']):
                print(f'|{hoja["personajes"][idx]}|\t|{hoja["armas"][idx]}|\t|{hoja["lugares"][idx]}|')

def jugar_vs_amigo():
    jugador_activo = 'jugador1'
    while (True):
        print(f'{"#" * 10} es el turno de {jugadores[jugador_activo]["nombre"]}')
        menu()
        opcion = str(input())
        if opcion.lower() == 'a':
            print(f'Sabiendo que todas las posibilidades son: {todas_las_cartas}')
            print('Usted está suponiendo que: ')
            
            personaje_seleccionado = str(input('La persona que cometió el crimen fue: ')).capitalize()
            arma_seleccionada = str(input('Usó esta arma: ')).capitalize()
            lugar_seleccionado = str(input('Y cometió el crimen en este lugar de la mansión: ')).capitalize()
            
            verificar_cartas_jugador_rival(obtener_rival(jugador_activo), personaje_seleccionado, arma_seleccionada, lugar_seleccionado)
            print('Fin de tu turno')
            anotar_hoja = str(input('Ahora tienes 2 opciones:\na)Anotar en la hoja\nb)Continuar jugando '))
            if anotar_hoja.lower() == 'a':
                jugadores[jugador_activo]['hoja']['personajes'].append(str(input('Anote en la hoja el nombre del criminal: ')).capitalize())
                jugadores[jugador_activo]['hoja']['armas'].append(str(input('Anote en la hoja el arma que usó: ')).capitalize())
                jugadores[jugador_activo]['hoja']['lugares'].append(str(input('Anote en la hoja el lugar donde pasó: ')).capitalize())
                print('Registraste éste renglon en la hoja.')
            jugador_activo = obtener_rival(jugador_activo)

        if opcion.lower() == 'b':
            print(f'Sabiendo que todas las posibilidades son: {todas_las_cartas}')
            print('Usted está acusando y confirma que: ')
            
            personaje_seleccionado = str(input('La persona que cometió el crimen fue: ')).capitalize()
            arma_seleccionada = str(input('Usó esta arma: ')).capitalize()
            lugar_seleccionado = str(input('Y cometió el crimen en este lugar de la mansión: ')).capitalize()
            
            if(sobre['personaje'] == personaje_seleccionado and sobre['arma'] == arma_seleccionada and sobre['lugar'] == lugar_seleccionado):
                print(f'{jugadores[jugador_activo]["nombre"]}, acabas de descrubir el crimen, ganaste una condecoración por parte de la policia!')
                break
            else:
                print(f'{jugadores[jugador_activo]["nombre"]}, Usted acaba de perder, por default ganó: {jugadores[obtener_rival(jugador_activo)]["nombre"]}.\n Quien cometió el crimen tenía estos datos: {sobre}')
                reintentar = str(input('Reintentar?\na)Si\nb)no'))
                if reintentar == 'a':
                    jugador_activo = obtener_rival(jugador_activo) #continuamos con el juego
                else:
                    break
        if opcion == 'c':
            mostrar_hoja_jugador(jugador_activo)
        if opcion == 'd':
            break

def jugar_vs_cpu():
    jugador_activo = 'jugador1'
    turnos_cpu = 1 
    turnos_cpu_hasta_acusar = randint(3, 20) #minimo 3 turnos y maximo 20
    while (True):
        print(f'{"#" * 10} es el turno de {jugadores[jugador_activo]["nombre"]}')
        menu()
        if turnos_cpu == turnos_cpu_hasta_acusar:
            cpu_personaje = choice(todas_las_cartas['personajes'])
            cpu_arma = choice(todas_las_cartas['armas'])
            cpu_lugar = choice(todas_las_cartas['lugares'])
            print(f'CPU ha decidido acusar con estas cartas: {cpu_personaje}, {cpu_arma}, {cpu_lugar}')
            if cpu_personaje == sobre['personaje'] and cpu_arma == sobre['arma'] and cpu_lugar == sobre['lugar']:
                print(f'{jugadores[jugador_activo]["nombre"]}, acaba de descrubir el crimen, y se ganó una condecoración por parte de la policia!')
            else:
                print(f'CPU perdió la esperanza de ganar y decidió rendirse, por default gana {jugadores[obtener_rival(jugador_activo)]["nombre"]}')
                break
        elif jugador_activo == 'jugador2' and turnos_cpu < turnos_cpu_hasta_acusar:
            cpu_personaje = choice(todas_las_cartas['personajes'])
            cpu_arma = choice(todas_las_cartas['armas'])
            cpu_lugar = choice(todas_las_cartas['lugares'])
            jugadores[jugador_activo]['hoja']['personajes'].append(cpu_personaje)
            jugadores[jugador_activo]['hoja']['armas'].append(cpu_arma)
            jugadores[jugador_activo]['hoja']['lugares'].append(cpu_lugar)
            print("CPU ha decidido escribir en su hoja.")
            turnos_cpu += 1
            jugador_activo = obtener_rival(jugador_activo)
            continue
        else:
            opcion = str(input())

        if opcion.lower() == 'a':
            print(f'Sabiendo que todas las posibilidades son: {todas_las_cartas}')
            print('Usted está suponiendo que: ')
            
            personaje_seleccionado = str(input('La persona que cometió el crimen fue: ')).capitalize()
            arma_seleccionada = str(input('Usó esta arma: ')).capitalize()
            lugar_seleccionado = str(input('Y cometió el crimen en este lugar de la mansión: ')).capitalize()
            
            verificar_cartas_jugador_rival(obtener_rival(jugador_activo), personaje_seleccionado, arma_seleccionada, lugar_seleccionado)
            print('Fin de tu turno')
            anotar_hoja = str(input('Ahora tienes 2 opciones:\na)Anotar en la hoja\nb)Continuar jugando '))
            if anotar_hoja.lower() == 'a':
                jugadores[jugador_activo]['hoja']['personajes'].append(str(input('Anote en la hoja el nombre del criminal: ')).capitalize())
                jugadores[jugador_activo]['hoja']['armas'].append(str(input('Anote en la hoja el arma que usó: ')).capitalize())
                jugadores[jugador_activo]['hoja']['lugares'].append(str(input('Anote en la hoja el lugar donde pasó: ')).capitalize())
                print('Registraste éste renglon en la hoja.')
            jugador_activo = obtener_rival(jugador_activo)

        if opcion.lower() == 'b':
            print(f'Sabiendo que todas las posibilidades son: {todas_las_cartas}')
            print('Usted está acusando y confirma que: ')
            
            personaje_seleccionado = str(input('La persona que cometió el crimen fue: ')).capitalize()
            arma_seleccionada = str(input('Usó esta arma: ')).capitalize()
            lugar_seleccionado = str(input('Y cometió el crimen en este lugar de la mansión: ')).capitalize()
            
            if(sobre['personaje'] == personaje_seleccionado and sobre['arma'] == arma_seleccionada and sobre['lugar'] == lugar_seleccionado):
                print(f'{jugadores[jugador_activo]["nombre"]}, acabas de descrubir el crimen, ganaste una condecoración por parte de la policia!')
                break
            else:
                print(f'{jugadores[jugador_activo]["nombre"]}, Usted acaba de perder, por default ganó: {jugadores[obtener_rival(jugador_activo)]["nombre"]}.\n Quien cometió el crimen tenía estos datos: {sobre}')
                reintentar = str(input('Reintentar?\na)Si\nb)no'))
                if reintentar == 'a':
                    jugador_activo = obtener_rival(jugador_activo) #continuamos con el juego
                else:
                    break
        if opcion == 'c':
            mostrar_hoja_jugador(jugador_activo)
        if opcion == 'd':
            break

def verificar_tabulate():
    try:
        import tabulate
        return True
    except ModuleNotFoundError:
        print('Tabulate es necesario para que las tablas se vean bonitas, se procederá a instalarlo. No presione ninguna tecla.')
        try:
            import subprocess
            subprocess.check_call(['pip', 'install', 'tabulate'])
            print('Tabulate ha sido instalado')
            return True
        except subprocess.CalledProcessError:
            print('No se pudo instalar tabulate. por favor instalalo manualmente en tu terminal ejectuando: pip install tabulate asegurate de tener conexion a internet')
            return False

if __name__ == "__main__":
    print('-*' * 10 + 'CLUE en Python' + '-*' * 10)
    modo_juego = str(
        input('a)Quiero jugar CLUE con un amigo\nb)Quiero jugar contra la PC: '))
    if modo_juego:
        if modo_juego.lower() == 'a':
            jugadores['jugador1']['nombre'] = str(input('Ingrese el nombre del jugador 1:'))
            jugadores['jugador2']['nombre'] = str(input('Ingrese el nombre del jugador 2:'))
            barajar()
            jugar_vs_amigo()
        if modo_juego.lower() == 'b':
            jugadores['jugador1']['nombre'] = str(input('Ingrese el nombre del jugador 1:'))
            jugadores['jugador2']['nombre'] = 'CPU'
            barajar()
            jugar_vs_cpu()        
        print('Gracias por jugar.')
    else:
        print("No ingresó opcion para jugar...")
