laberinto = [
    [' ', 'X', 'X', 'X', 'X'], 
    [' ', 'X', ' ', ' ', ' '],
    [' ', 'X', ' ', 'X', ' '], 
    [' ', ' ', ' ', 'X', ' '], 
    ['X', 'X', 'X', 'X', 'S']
    ]
def recorrer_laberinto():
    i=0
    j=0
    lista=[]
    posiciones_anteriores=[(0, 0)]
    while laberinto[i][j]!='S':
        if (laberinto[i+1][j]==' ' or laberinto[i+1][j]=='S') and (i+1, j) not in posiciones_anteriores:
            i+=1
            lista.append('abajo')
            posiciones_anteriores.append((i, j))
            
        elif laberinto[i][j+1]==' ' and (i, j+1) not in posiciones_anteriores:
            j+=1
            lista.append('derecha')
            posiciones_anteriores.append((i, j))

        elif laberinto[i-1][j]==' ' and (i-1, j) not in posiciones_anteriores:
            i-=1
            lista.append('arriba')
            posiciones_anteriores.append((i, j))
            
        elif laberinto[i][j-1]==' ' and (i, j-1) not in posiciones_anteriores:
            j-=1
            lista.append('izquierda')
            posiciones_anteriores.append((i, j))


    return lista

print(recorrer_laberinto())
