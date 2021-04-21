# DIO-logica
# Fluxograma

# var == n1,n2,n3,n4,s,m,s
# type == float

n1 = float (input ('Digite a primeira nota:'))
n2 = float (input ('Digite a segunda nota:'))
n3 = float (input ('Digite a terceira nota:'))
n4 = float (input ('Digite a quarta nota:'))

s = n1+n2+n3+n4
m = s/4

print ('Sua média foi {:.1f}' . format (m))

if (m > 7):
   print ('Parabens! Você passou de ano.')
else:
    print ('Sinto muito, você foi reprovado.')
       