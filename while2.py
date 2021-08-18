#Questão1
i=n=soma=0
while(n != 999):
    n=int(input('Digite um valor: '))
    if n == 999:
        break
    soma += n
    i += 1
print(f'o número de valores digitados é {i} e a soma é {soma}')

#Questão2
import random
v=0
while True:
    jogo = ['pedra', 'papel', 'tesoura']
    comp = random.choice(jogo)
    n=str(input('Pedra, Papel, Tesoura! ')).strip().lower()
    print(f'Você jogou {n} e o computador jogou {comp}')
    if n == 'pedra' and comp == 'papel':
        print('Você perdeu!')
        break
    elif n == 'pedra' and comp == 'pedra':
        print('Empate, jogue novamente!')
    elif n == 'pedra' and comp == 'tesoura':
        print('Você venceu!')
        v += 1
    elif n == 'papel' and comp == 'tesoura':
        print('Você perdeu!')
        break
    elif n == 'papel' and comp == 'papel':
        print('Empate, jogue novamente!')
    elif n == 'papel' and comp == 'pedra':
        print('Você venceu!')
        v += 1
    elif n == 'tesoura' and comp == 'pedra':
        print('Você perdeu!')
        break
    elif n == 'tesoura' and comp == 'tesoura':
        print('Empate, jogue novamente!')
    elif n == 'tesoura' and comp == 'papel':
        print('Você venceu!')
        v += 1
print(f'Você venceu do computador {v} vezes')

#Questão3