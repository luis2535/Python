x=input("Digite um número inteiro: ")
tamanho=x
x=int(x)
soma=0
i=0
while i<len(tamanho):
    y=x%10
    x=x//10
    soma=soma+y
    i=i+1
print(soma)