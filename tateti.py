tablero = [' ' for _ in range(9)]

def imprimir_tablero():
    print(f"""
 {tablero[0]} | {tablero[1]} | {tablero[2]}
---+---+---
 {tablero[3]} | {tablero[4]} | {tablero[5]}
---+---+---
 {tablero[6]} | {tablero[7]} | {tablero[8]}
""")

def verificar_ganador():
    combinaciones = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Filas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columnas
        [0, 4, 8], [2, 4, 6]              # Diagonales
    ]
    for combinacion in combinaciones:
        if tablero[combinacion[0]] == tablero[combinacion[1]] == tablero[combinacion[2]] != ' ':
            return tablero[combinacion[0]]
    return None

def es_empate():
    return ' ' not in tablero

def jugar():
    jugador_actual = 'X'
    continuar = True
    
    while continuar:
        imprimir_tablero()
        print(f"Turno del jugador {jugador_actual}.")
        
        try:
            posicion = int(input("Elige una posición (0-8): "))
            if tablero[posicion] != ' ':
                print("La posición ya está ocupada, intenta de nuevo.")
            else:
                tablero[posicion] = jugador_actual
                ganador = verificar_ganador()
                if ganador:
                    imprimir_tablero()
                    print(f"¡El jugador {ganador} ha ganado!")
                    continuar = False
                elif es_empate():
                    imprimir_tablero()
                    print("¡Es un empate!")
                    continuar = False
                else:
                    jugador_actual = 'O' if jugador_actual == 'X' else 'X'
        except (ValueError, IndexError):
            print("Entrada inválida, elige un número entre 0 y 8.")

jugar()
