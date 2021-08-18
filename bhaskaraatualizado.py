import math
def delta(x,y,z):
    return y**2-4*x*z

def imprime_raiz(x,y,z):
    if delta(x,y,z)==0:
        x=(-y)/(2*x)
        print("a raiz desta equação é", x)
    elif delta>0:
        x1=(-y - math.sqrt(delta(x,y,z)))/(2*x)
        x2=(-y + math.sqrt(delta(x,y,z)))/(2*x)
        print("as raízes da equação são", x1, "e", x2)
    else:
        print("esta equação não possui raízes reais")


a=float(input())
b=float(input())
c=float(input())
imprime_raiz(a,b,c)

