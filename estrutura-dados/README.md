# <span style='color:#ff5dae;'>Estrutura de dados</span>

## <span style='color:#cb74ff;'>Arrays</span>

  Array, também conhecida como matriz e vetor, é um espaço na memória, reservado para guardar dados de modo ordenado, ou seja, para cada linha, uma informação e é uma das estruturas de dados mais utilizadas pela sua simplicidade. 
  
  As arrays possuem tamanhos fixos e a diferença entre um vetor e uma matriz  é que o vetor é um array de apenas 1 dimensão e a matriz é um array de 2 (ou mais) dimensões.
  
  Exemplo de array vetor:
 
<a href="https://imgbb.com/"><img src="https://i.ibb.co/5BRppdr/Screenshot-20210428-030331.png" alt="Screenshot-20210428-030331" border="0" /></a>
  
  Exemplo de array matriz:

<a href="https://ibb.co/BzHtHBW"><img src="https://i.ibb.co/5MX6XLp/Screenshot-20210428-030224.png" alt="Screenshot-20210428-030224" border="0" /></a>

 Apos colocar os respectivos dados na memoria não se pode mudar.
  
## <span style='color:#cb74ff;'>Listas</span>

 É um conjunto de estruturas chamadas de "nós". O nó é quem armazena as informações para a lista gerenciar. Existem dois tipos de listas: as listas ligadas e as listas duplamente ligadas.
 
 As listas ligadas somente conseguem ver que vem despois, ou seja, ela somente anda para frente, enquanto a lista duplamente ligada consegue ver quem vem depois e quem veio anteriormente, assim ela anda para frente e para trás.
 
 
 Exemplo lista ligada:
 
<a href="https://ibb.co/d7QDyJs"><img src="https://i.ibb.co/DL7QngP/lista-com-dois-elementos.png" alt="lista-com-dois-elementos" border="0" /></a>

 Exemplo lista duplamente ligada:
 
<a href="https://ibb.co/DGJx8KP"><img src="https://i.ibb.co/FsrS07k/lista-duplamente-ligada.png" alt="lista-duplamente-ligada" border="0" /></a>
  
 
## <span style='color:#cb74ff;'>Pilhas</span>

 A pilha é considerada uma estrutura de dados simples, sendo fácil de implementar. As pilhas trabalham com o formato LIFO (o último a entrar é o primeiro a sair, “Last In, First Out”, em inglês). 
 
 Lembre-se da pilha como uma pilha de livros, em que o primeiro livro que foi inserido na pilha, normalmente é o último que sai dela, enquanto o último adicionado é o primeiro a ser retirado.
 
<a href="https://imgbb.com/"><img src="https://i.ibb.co/m0Pj3n0/Pilha-Java1.jpg" alt="Pilha-Java1" border="0" /></a>
 
  Exemplo do formato LIFO com as operações push (empilhar) e pop (desempilhar):
  
<a href="https://ibb.co/3BJV2w2"><img src="https://i.ibb.co/syBcnhn/Lifo-stack.png" alt="Lifo-stack" border="0" /></a>

## <span style='color:#cb74ff;'>Filas</span>

 A estrutura de dados fila segue também um formato padrão, igualmente a pilha, porém ao contrario, conhecido como formato FIFO (o primeiro a entrar é o primeiro a sair, “First In, First Out”, em inglês).
 
  Lembre-se da fila como uma fila de banco, em que o primeiro a chegar da fila é o primeiro a ser atendido, ou seja, primeiro a sair da fila.
  
<a href="https://ibb.co/D47M4Wz"><img src="https://i.ibb.co/Y2td2QP/fila-de-banco.jpg" alt="fila-de-banco" border="0" /></a>
  
  Exemplo do formato LIFO com as operações enqueue (enfileirar) e dequeue (desenfileirar):
  
<a href="https://imgbb.com/"><img src="https://i.ibb.co/PCSfybW/Fifo-queue.png" alt="Fifo-queue" border="0" /></a>

## <span style='color:#cb74ff;'>Tabela hash</span>

 A tabela hash, também conhecida por tabela de espalhamento, é uma estrutura de dados especial, que associa chaves de pesquisa (hash) a valores. Seu objetivo é, a partir de uma chave simples, fazer uma busca rápida e obter o valor desejado.
  
  Exemplo de uma tabela hash:
  
<a href="https://ibb.co/TtxV8H3"><img src="https://i.ibb.co/tDT7sbr/Screenshot-20210428-185131.png" alt="Screenshot-20210428-185131" border="0" /></a>

## <span style='color:#cb74ff;'>Grafo</span>

 Um grafo é uma coleção de vértices (V) (pontos ou circulos) e uma coleção de arcos (E)(linhas entre esse pontos ou entre circulos) constituídos por pares de vértices. É uma estrutura usada para representar um modelo em que existem relações entre os objectos de uma certa coleção.

  Exemplo de um grafo:
  
<a href="https://ibb.co/7JwQ1Lm"><img src="https://i.ibb.co/1fDMmjW/grafo-exemplo-1-768x460.gif" alt="grafo-exemplo-1-768x460" border="0" /></a> 
  
   No exemplo acima, conseguimos ver que : V = {1, 2, 3, 4, 5, 6} e E = {(1,3), (1,6), (2,5), (3,4), (3,6)

## <span style='color:#cb74ff;'>Árvores</span>

 A estrutura de dados árvore é uma das mais importantes estruturas não lineares. Ela tem as características topologica de uma árvore. Diferente das listas, em que os dados se encontram numa sequência, nas árvores, os dados estão em forma hierárquica.
 
 A imagem abaixo ilustra a representação de uma árvore, onde é possível perceber a analogia do termo utilizado para a estrutura.
 
<a href="https://imgbb.com/"><img src="https://i.ibb.co/qgvQSXJ/trees-01b.png" alt="trees-01b" border="0" /></a>
<a href="https://imgbb.com/"><img src="https://i.ibb.co/5vW39pM/trees-01a.png" alt="trees-01a" border="0" /></a>

A estrutura arvore armazena seus dados em nós (nodos). Existe o nó raiz, os nós filhos e pais, e os nós folhas.

Exemplo: 
- Nó raiz :

<a href="https://imgbb.com/"><img src="https://i.ibb.co/th1SBqg/trees-01a-3.png" alt="trees-01a-3" border="0" /></a>

- Nós pais e filhos:

<a href="https://imgbb.com/"><img src="https://i.ibb.co/t4s6rFc/Screenshot-20210428-153756.png" alt="Screenshot-20210428-153756" border="0" /></a>

<a href="https://imgbb.com/"><img src="https://i.ibb.co/B6wPN9b/Screenshot-20210428-154046.png" alt="Screenshot-20210428-154046" border="0" /></a>

- Nós folhas :

<a href="https://imgbb.com/"><img src="https://i.ibb.co/HKJ1hp0/Screenshot-20210428-154255.png" alt="Screenshot-20210428-154255" border="0" /></a>

 Abaixo uma imagem bonitinha para ser lembrado dos nós folhas 😊❣️⬇️

<a href="https://imgbb.com/"><img src="https://i.ibb.co/GWTTZFr/trees-09.png" alt="trees-09" border="0" /></a>
