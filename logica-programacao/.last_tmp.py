# Estrutura-de-repetição
# var. int,n,lim

n = 1
lim = 10

print ('\n','*'*40)
while (n <= lim):
    print (f'\nContagem atual {n}')
    n = n+1

print ('\n','*'*40,'\n\nContagem encerrada\n\n','*'*40)


# Exercício-tabuada-do-9
# var. int,n,v,lim

#n = 9
n = 1
#v = 1
#lim = 90
lim = 10

tab = int (input('Qual tabuada você deseja? tabuada do '))
print (f'\nTabuada do {tab} ❣️\n')

while (n <= lim):
    print (f'{tab}x{n} = {tab*n}')
    #print (f'{tab}x{v} = {n}')
    #v = v+1
    n = n+1