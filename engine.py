#Para el juego de la vida vamos a usar varias librerias:
import numpy as np

#Definimos lo inicial para hacer el tablero y los patrones
N = 10

#La célula está viva si on 
ON = 1
#La célula está muerta si off
OFF = 0

#Creamos el grid con la libreria numpy
grid = np.full((N, N), OFF)

def update(grid):
  newGrid = grid.copy()
  #Hacemos una iteración que recorre cada elemento de la matriz
  for i in range(N):
    for j in range(N):
      #Contamos cuantas celulas vivas hay por el elemento que observamos
      #También, usamos el efecto de "wrap arround" para que las células en los bordes tengan vecinos en el otro lado del tablero
      total = int(grid[i,(j-1)%N] + grid[i,(j+1)%N] + 
                  grid[(i-1)%N,j] + grid[(i+1)%N,j] + 
                  grid[(i-1)%N,(j-1)%N] + grid[(i-1)%N,(j+1)%N] + 
                  grid[(i+1)%N,(j-1)%N] + grid[(i+1)%N,(j+1)%N])
      if grid[i, j] == ON:  # Hacemos este if cuando la célula está viva
        if (total < 2) or (total > 3):
          newGrid[i, j] = OFF  # Muere por soledad o sobrepoblación
        else:  #En caso de que la célula esté muerta se ejecuta este else
          if total == 3: #Si hay 3 vivas al rededor de la célula muerta, revive
            newGrid[i, j] = ON

  return newGrid
