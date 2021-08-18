def soma_matrizes(m1,m2):
    linha1=len(m1)
    coluna1=len(m1[0])
    linha2=len(m2)
    coluna2=len(m2[0])
    if linha1 == linha2 and coluna1 == coluna2:
        matriz=[]
        for i in range(len(m1)):
            linha=[]
            for j in range(len(m1[0])):
                soma=m1[i][j]+m2[i][j]
                linha.append(soma)
            matriz.append(linha)
        print(matriz)
    else:
        print(False)

