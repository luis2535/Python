def usuario_escolhe_jogada(N,M,P):
    C = int(input("Quantas peças você vai tirar? "))
    print()
    while(C>M or C<1):
        print("Oops! Jogada inválida! Tente de novo.")
        print()
        C=int(input("Quantas peças você vai tirar? "))
        print()
    V=N-C
    P=1
    return V,C,P
def computador_escolhe_jogada(N,M,P):
    i=1
    aux=M
    while(i<=M):
        V=N-M
        if V%(M+1)==0:
            P=0
            return V,M,P
        M=M-1
    P=0
    M=aux
    S=N-M
    return S,M,P

def partida():
    print("Você escolheu uma partida!")
    print()
    N=int(input("Quantas peças? "))
    M=int(input("Limite de peças por jogada? "))
    P=0
    if N%(M+1)==0:
        print()
        print("Você começa")
        print()
        P=0
    else:
        print()
        print("Computador começa!")
        print()
        P=1
    while N!=0:
        if P==1:
            N, J, P=computador_escolhe_jogada(N,M,P)
            if J==1:
                print("O computador tirou uma peça.")
            else:
                print("O computador tirou",J,"peças.")
            if N==1:
                print("Agora resta apenas uma peça no tabuleiro.")
                print()
            elif N>1:
                print("Agora restam",N,"peças no tabuleiro.")
                print()
            else:
                print("Fim de jogo! O computador ganhou!")
                print()
        else:
            N, J, P=usuario_escolhe_jogada(N,M,P)
            if J==1:
                print("Você tirou uma peça.")
            else:
                print("Você tirou",J,"peças.")
            if N==1:
                print("Agora resta apenas uma peça no tabuleiro.")
                print()
            elif N>1:
                print("Agora restam",N,"peças no tabuleiro.")
                print()
            else:
                print("Fim de jogo! Você ganhou!")
                print()

def campeonato():
    print("Você escolheu campeonato!")
    print()
    i=1
    A=0
    B=0
    while (i<=3):
        print("**** Rodada",i,"****")
        print()
        N = int(input("Quantas peças? "))
        M = int(input("Limite de peças por jogada? "))
        P = 0
        if N % (M + 1) == 0:
            print()
            print("Você começa")
            print()
            P = 0
        else:
            print()
            print("Computador começa!")
            print()
            P = 1
        while N != 0:
            if P == 1:
                N, J, P = computador_escolhe_jogada(N, M, P)
                if J == 1:
                    print("O computador tirou uma peça.")
                else:
                    print("O computador tirou", J, "peças.")
                if N == 1:
                    print("Agora resta apenas uma peça no tabuleiro.")
                    print()
                elif N > 1:
                    print("Agora restam", N, "peças no tabuleiro.")
                    print()
                else:
                    print("Fim de jogo! O computador ganhou!")
                    B=B+1
                    print()
            else:
                N, J, P = usuario_escolhe_jogada(N, M, P)
                if J == 1:
                    print("Você tirou uma peça.")
                else:
                    print("Você tirou", J, "peças.")
                if N == 1:
                    print("Agora resta apenas uma peça no tabuleiro.")
                    print()
                elif N > 1:
                    print("Agora restam", N, "peças no tabuleiro.")
                    print()
                else:
                    print("Fim de jogo! Você ganhou!")
                    A=A+1
                    print()
        i=i+1
    print("**** Final do campeonato! ****")
    print()
    print("Placar: Você",A,"X",B,"Computador")

print("Bem-vindo ao jogo do NIM! Escolha:")
print()
print("1 - para jogar uma partida isolada")
print("2 - para jogar um campeonato")

X=int(input())
if X==1:
    partida()
elif(X==2):
    campeonato()
