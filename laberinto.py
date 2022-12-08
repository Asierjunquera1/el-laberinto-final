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
    while laberinto[i][j]!='S':
        if laberinto[i+1][j]==' ':
            i+=1
            lista.append('abajo')
    
        elif laberinto[i][j+1]==' ':
            j+=1
            lista.append('derecha')
    
        elif laberinto[i-1][j]==' ' and laberinto[i+1][j]=='X':
            i-=1
            lista.append('arriba')
    
        elif laberinto[i][j-1] and laberinto[i][j-1]=='X':
            j-=1
            lista.append('izquierda')
        

    return lista

print(recorrer_laberinto())
