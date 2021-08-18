import math

a=float(input())
b=float(input())
c=float(input())

if (b**2 - 4*a*c)>0:
    delta=math.sqrt(b**2 - 4*a*c)
    x1=(-b - delta)/(2*a)
    x2=(-b + delta)/(2*a)
    print("as raízes da equação são",x1,"e",x2)
elif (b**2 - 4*a*c) == 0:
    x=-b/(2*a)
    print("a raiz desta equação é",x)
else:
    print("esta equação não possui raízes reais")


