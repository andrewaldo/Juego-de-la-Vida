import numpy as np

#Definimos el tamaño del tablero
N = 10

#Definimos los estados de las células
ON = 1
OFF = 0

#Creamos el tablero con todas las células muertas
grid = np.full((N, N), OFF)


#Esta función calcula la siguiente generación
def update(grid):

    #Copiamos el tablero para guardar los nuevos estados
    newGrid = grid.copy()

    #Recorremos todas las células del tablero
    for i in range(N):
        for j in range(N):

            #Contamos las ocho células vecinas
            total = int(
                grid[i, (j-1) % N] +
                grid[i, (j+1) % N] +
                grid[(i-1) % N, j] +
                grid[(i+1) % N, j] +
                grid[(i-1) % N, (j-1) % N] +
                grid[(i-1) % N, (j+1) % N] +
                grid[(i+1) % N, (j-1) % N] +
                grid[(i+1) % N, (j+1) % N]
            )

            #Si la célula está viva
            if grid[i, j] == ON:

                #Muere si tiene menos de 2 o más de 3 vecinos
                if total < 2 or total > 3:
                    newGrid[i, j] = OFF

            #Si la célula está muerta
            else:

                #Nace si tiene exactamente 3 vecinos vivos
                if total == 3:
                    newGrid[i, j] = ON

    #Devolvemos el tablero actualizado
    return newGrid
