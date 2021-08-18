#Entradas
N=int(input())
L=input().split()
for i in range(len(L)):
    L[i]=int(L[i])
#Processamento
A=0
B=0
for v in L:
    if (v==1):
        A = 1 if A==0 else 0
    if (v==2):
        A = 1 if A == 0 else 0
        B = 1 if B == 0 else 0


print(A)
print(B)
