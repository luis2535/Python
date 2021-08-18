import math
def é_hipotenusa(x):
    i=1
    j=1
    while i<=x:
        j=1
        while j<=i:
            if math.pow(x,2)==(math.pow(i,2)+math.pow(j,2)):
                return True
            j=j+1
        i=i+1
    return False

def soma_hipotenusas(X):
    i=1
    soma=0
    while i<=X:
        if é_hipotenusa(i):
            soma=soma+i
        i=i+1
    return soma


X=int(input())
Y=soma_hipotenusas(X)
print(Y)