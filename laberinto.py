laberinto = [
    [' ', 'X', 'X', 'X', 'X'], 
    [' ', 'X', ' ', ' ', ' '],
    [' ', 'X', ' ', 'X', ' '], 
    [' ', ' ', ' ', 'X', ' '], 
    ['X', 'X', 'X', 'X', 'S']
    ]

def recorrer_laberinto():
    lista=[]
    posicion=laberinto[0][0]
    for i in range(len(laberinto)-1):
        posicion1=laberinto[1+i][0]
        if posicion1==' ':
            lista.append('abajo')
        else:
            for j in range(len(laberinto)-1):
                posicion2=laberinto[i][j+1]
                if posicion2==' ':
                    lista.append('derecha')
 
                
                    

    





    return lista
print(recorrer_laberinto())


