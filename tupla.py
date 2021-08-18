#Questão1
tupla=('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenovo','vinte')
n=int(input('Digite um número de 0 a 20: '))
while n<0 or n>20:
    n=int(input('Tente novamente. Digite um número de 0 a 20: '))
print(f'O número que você digitou foi {tupla[n]}')

#Questão2
brasileirao=('Flamengo','Santos','Palmeiras','Grêmio','Athletico-PR','São Paulo','Internacional','Corinthians','Fortaleza','Goias','Bahia','Vasco','Atlético-MR',
             'Fluminense','Botafogo','Ceará','Cruzeiro','CSA','Chapecoense','Avai')
print(brasileirao[:5])
print(brasileirao[16:])
print(sorted(brasileirao))
for pos, time in enumerate (brasileirao):
    if time=='Chapecoense':
        print(f'A posição da {time} é {pos+1}° colocado')

#Questão3
import random
numeros=(random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10))
maior=-1
menor=11
print('Os números sorteados foram:',end=' ')
for c in numeros:
    print(c,end=' ')
    if c > maior:
        maior=c
    if c < menor:
        menor=c
print()
print(f'O maior numero sorteado foi {maior}')
print(f'O menor número sorteado foi {menor}')

#Questão4
a=int(input('Digite o primeiro valor: '))
b=int(input('Digite o segundo valor: '))
c=int(input('Digite o terceiro valor: '))
d=int(input('Digite o quarto valor: '))
tupla=(a,b,c,d)
print(f'Os valores digitados foram {tupla}')
pares=0
print(f'O número 9 foi digitado {tupla.count(9)} vezes')
pos3=0
for pos, num in enumerate(tupla):
    if num%2==0:
        pares += 1
    if num == 3 and pos3 == 0:
        pos3=-1
        print(f'O número 3 aparece na posição {pos+1}')
if pos3 == 0:
    print('O número 3 não apareceu em nenhuma posição')
print(f'O número de pares é {pares}')

#Questão5
Listapreços=('Lápis', 1.00,'Borracha',2.00,'Caderno',15.00,'Estojo',25.00,'Transferidor',4.20,'Mochila',120.32,'Livro',34.90)
print('-'*30)
print('LISTAGEM DE PREÇOS'.center(30))
print('-'*30)
for pos in range(len(Listapreços)):
    if pos%2==0:
        print(f'{Listapreços[pos]:.<30}R${Listapreços[pos+1]:.2f}')

print('-'*30)
#Questão6
palavras=('aprender','estudar','programar','python','curso','trabalhar','futuro')
for c in range(len(palavras)):
    print(f'Na palavra {palavras[c].upper()} temos as seguintes vogais:', end=' ')
    for h in palavras[c]:
        if h in 'aeiou':
            print(h,end=' ')
    print()
