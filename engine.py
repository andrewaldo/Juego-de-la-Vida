import numpy as np

# Tamaño del tablero
N = 10

# Estados de las células
ON = 1
OFF = 0

# Creamos el tablero inicial
grid = np.full((N, N), OFF)

# Función para actualizar el tablero
def update(grid):
    newGrid = grid.copy()

    for i in range(N):
        for j in range(N):

            # Contamos los 8 vecinos de cada célula
            total = (
                grid[(i-1) % N, (j-1) % N] +
                grid[(i-1) % N, j] +
                grid[(i-1) % N, (j+1) % N] +
                grid[i, (j-1) % N] +
                grid[i, (j+1) % N] +
                grid[(i+1) % N, (j-1) % N] +
                grid[(i+1) % N, j] +
                grid[(i+1) % N, (j+1) % N]
            )

            # Reglas del Juego de la Vida
            if grid[i, j] == ON:
                if total < 2 or total > 3:
                    newGrid[i, j] = OFF
            else:
                if total == 3:
                    newGrid[i, j] = ON

    return newGrid
