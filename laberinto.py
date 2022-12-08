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
    lista2=[(0, 0)]
    while laberinto[i][j]!='S':
        if laberinto[i+1][j]==' ' and (i+1, j) not in lista2:
            i+=1
            lista.append('abajo')
            lista2.append((i, j))
    
        elif laberinto[i][j+1]==' ' and (i, j+1) not in lista2:
            j+=1
            lista.append('derecha')
            lista2.append((i, j))

        elif laberinto[i-1][j]==' ' and (i-1, j) not in lista2:
            i-=1
            lista.append('arriba')
            lista2.append((i, j))
            
        elif laberinto[i][j-1]==' ' and (i, j-1) not in lista2:
            j-=1
            lista.append('izquierda')
            lista2.append((i, j))
        

    return lista

print(recorrer_laberinto())
