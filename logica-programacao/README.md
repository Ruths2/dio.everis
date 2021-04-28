### Algoritmo:

É a sequência lógica de um passo a passo, como se fosse uma receita, com inicio, meio, e fim.

----

### Fluxograma:

É uma representação gráfica do algoritmo em formas geométricas, facilitando a sua leitura.

----

### Variável:

São valores mutáveis (objetos) ou espaço na memória do computador que pode variar durante a execução do algoritimo (números, caracteres, alfanuméricos ou lógica).

Exemplo variável:

- Números: 012345....
- Caracteres: abcd$_&-+()....
- Alfanuméricos: abcd$_&-+().... e 12345....
- Lógica: true ou false.

----

### Constante:

São valores imutáveis e não se alteram durante a vida útil do programa, ou espaço na memória do computador que não se modifica.

----

### Estrutura de desvio condicional e de repetição:

## if (se)
- A condição if serve para indicar uma condição qualquer, executando-o apenas se ela for verdadeira. 

 Exemplo :
 

```

# Código em python (role para o lado):

tabuada = int (input ( 'Digite a tabuada que você deseja: tabuada do '))
# Aqui o caracter = significa recebe, tabuada recebe...etc
# Int significa o tipo da resposta que eu espero, no caso é um número inteiro.
# Input é o comando que pede para o computador guardar a resposta do usuario, que no caso é a "tabuada"

if (tabuada <= 5):
# if (se) tabuada <= 5 : (tabuada for menor ou igual a 5, faça o seguinte:)
    print (' Ok. Vamos lá.....')
# print (escreva na tela)  Ok. vamos lá.....


```
## else (senão)

- A condição else serve como um caminho alternativo do if. Ou seja, o else vai ser executado se a condição sendo verificada no if for falsa.

Exemplo:


```

# Código em python (role para o lado):

tabuada = int (input ( 'Digite a tabuada que você deseja: tabuada do '))
# Aqui o caracter = significa recebe, tabuada recebe...etc
# Int significa o tipo da resposta que eu espero, no caso é um número inteiro.
# Input é o comando que pede para o computador guardar a resposta do usuario, que no caso é a "tabuada"

if (tabuada <= 5):
# if (se) tabuada <= 5: (tabuada for menor ou igual a 5, faça o seguinte:)
    print (' Ok. Vamos lá.....')
# print (escreva na tela) Ok. vamos lá.....    
else:
# else: (senão:)
    print ('Ótimo. É pra já!')
# print (escreva na tela) Ótimo. É pra já


```
## elif (se não se)

- A condição elif é utilizada quando queremos indicar uma outra condição caso o if inicial não for verdadeiro.  Se após, o elif for falso também, podemos utilizar outro elif para chegarmos ao nosso objetivo.

Exemplo:

```
# Código em python (role para o lado):

tabuada = int (input ( 'Digite a tabuada que você deseja: tabuada do '))
# Aqui o caracter = significa recebe, tabuada recebe...etc
# Int significa o tipo da resposta que eu espero, no caso é um número inteiro.
# Input é o comando que pede para o computador guardar a resposta do usuario, que no caso é a "tabuada"

if (tabuada <= 5):
# (se) tabuada <= 5: (tabuada for menor ou igual a 5, faça o seguinte:)
    print (' Ok. Vamos lá.....')
# print (escreva na tela) Ok. vamos lá.....
elif (tabuada == 7):
# elif (se não se) tabuada == 7 (tabuada for igual a 7, faça o seguinte:)
    print (' hummm....tabuada do 7 é a minha favorita.')
elif (tabuada <10) :
    print ('Legal, Aqui esta: ')
else:
    print ('Ótimo. É pra já!')
# else (senão:)
# print (escreva na tela) Ótimo. É pra já!


```


## while (enquanto)

- O comando while faz com que um conjunto de instruções seja executado varias vezes enquanto uma condição é atendida. Quando o resultado dessa condição passa a ser falso, a execução do loop para.

Exemplo:

```

# Código em python (role para o lado):

numero = 1
limite = 10

tabuada = int (input ('Digite a tabuada quevocê deseja? tabuada do '))
# Aqui o caracter = significa recebe, tabuada recebe...etc
# Int significa o tipo da resposta que eu espero, no caso é um número inteiro.
# Input é o comando que pede para o computador guardar a resposta do usuario, que no caso é a "tabuada"

while (numero <= limite):
    print (f'{tabuada}x{numero} = {tabuada*numero}')
    numero = numero+1

# while (enquanto) numero <= limite (numero é menor ou igual a limite)
# print (escreva na tela) tabuada x numero = (e resultado de tabuada x numero)
# nessa próxima linha pedimos ao python para somar + 1 todas as vezes que ele roda o loop, assim o código não repetira a mesma resposta toda vez e não ficará em um loop infinito.


```

## for (para)

- O comando for também faz com que um conjunto de instruções seja executado varias vezes, porém, no for, precisamos saber as condições de inicio e fim. Se não for possível identificar essas condições podemos utilizar o comando while.

Exemplo:


```

# Código em python (role para o lado):

tabuada = int (input ('Digite a tabuada quevocê deseja? tabuada do '))
# Aqui o caracter = significa recebe, tabuada recebe...etc
# Int significa o tipo da resposta que eu espero, no caso é um número inteiro.
# Input é o comando que pede para o computador guardar a resposta do usuario, que no caso é a "tabuada"

for c in range(1,11):
    print (f'{tabuada}x{c} = {c*tabuada}')
# for c (para o contador (o c significa contador, ele conta os numeros)) in range 1,11 (no intervalo de 1 a 11 faça o seguinte: (ele sempre ignora o numero em que vai parar))
# print (escreva na tela tabuada x c = resultadp de c x tabuada)


```
