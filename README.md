# Trabalhando com conjuntos, os sets
Formas de se declarar uma lista:

1. usando chaves: `conj = {3,2,1}`;
2. usando o construtor set: `conj = set(3,2,1)`.

Use o operador "ou" (pipe, `|`) para unir conjuntos:
```python
a = {2,4,6}
b = {1,2,3}
c = a | b
print(c) # Resultado: {1,2,3,4,6}.
# repare que não houve repetição do elemento 2, porque
# ele um conjunto não permite valores repetidos.
```
Conjuntos não tem ordem, e portanto a indexação dos elementos falha.
```python
conjunto = {3,2,1} # Criação de um set.
print(conjunto[1]) # Este código vai falhar.
```

Shallow copy: as listas possuem a função `copy`, que copiam apenas as referências aos objetos (e não o objeto inteiro):
```python
usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

# Cópia das referências aos números.
assistiram = usuarios_data_science.copy() 
# Inserção da lista usuarios_machine_learning na lista assistiram.
assistiram.extend(usuarios_machine_learning)

print({*assistiram})
# Resultado: {42, 43, 13, 15, 23, 56}
# Desordenado e sem repetição.
print(set([*usuarios_data_science, *usuarios_machine_learning]))
# O construtor set só aceita uma lista como parâmetro.
# Por isso a descompactação da lista tem que ser dentro
# de outra lista.
```
# Mais operações de conjuntos
Os quatro operadores:

1. Pipe (`|`): retorna a união dos conjuntos.
2. Ampersand (`&`): retorna a interseção dos conjuntos.
3. Hifen (`-`): retorna a diferença entre conjuntos (a ordem dos fatores altera o conjunto resultante).
4. Caret (`^`): é um "ou exclusivo"; retorna a união menos a interseção.

Exemplos:
```python
a, b = {1,2,3,4,5}, {2,4,6,8}

# União
print(a | b) # Resultado: {1, 2, 3, 4, 5, 6, 8}

# Interseção
print(a & b) # Resultado: {2, 4}

# Diferença
print(a - b) # Resultado: {1, 3, 5}
print(b - a) # Resultado: {8, 6}

# Ou exclusivo.
print(a ^ b) # 2 e 4 estão na interseção; não aparecem no resultado.
# Resultado: {1, 3, 5, 6, 8}
```
# Outro tipo de conjunto e conjuntos de outros tipos
```python
usuarios = {1, 5, 76, 34, 52, 13, 17}

usuarios.add(13)
# Resultado: {1, 34, 17, 52, 5, 76, 13}
# Mesmo tamanho: o elemento 13 já existe.

usuarios.append(13) # Vai falhar: append pressupõe ordem.
# lista.append(el) insere um elemento no fim da lista.
# Conjunto não é lista.

usuarios.add(765)
# Resultado: {1, 34, 17, 52, 5, 765, 76, 13}
# Tamanho diferente: o elemento 765 não existia.

usuarios.remove(765)
# Resultado: {1, 34, 17, 52, 5, 76, 13}
# Tamanho diferente: o elemento 765 foi removido.
```

Frozensets são conjuntos imutáveis.

```python
usuarios = frozenset(usuarios)

usuarios.add(70) 
# Vai falhar: não se acrescenta nada ao frozenset.

usuarios.remove(1)
# Vai falhar: não se remove nada do frozenset.
```
# Dicionários
Como instanciar dicionários:
```python
# Construção com dict. Note a falta das aspas nos parâmetros.
dicionario = dict(nome='Thiago', idade=39, ativo=True)

# Construtor dict usando uma lista de tuplas como parâmetro:
dicionario = dict([ 
    ('nome', 'Thiago'), 
    ('idade', 39), 
    ('ativo', True)
])
# Dica: a função zip cria listas de tuplas, que podem 
# ser usadas para inicializar um dicionário.

# Criando um dicionário com chaves e o key/value pair 
# separado por dois pontos. Note que a chave também
# precisa de aspas. 
dicionario = {'nome': 'Thiago', 'idade': 39, 'ativo': True}
```

Exemplo: contando palavras em um texto.
```python
meu_texto = "Bem vindo meu nome é Guilherme eu gosto "\
            "muito de nomes e tenho o meu cachorro e "\
            "gosto muito de cachorro"

# Criar o conjunto de palavras, para remover repetições.
palavras = {*meu_texto.split()} 

# Criar o dicionário de aparições com o construtor dict.
aparicoes = dict(zip( 
    # zip() forma uma lista de tuplas com 
    # cada palavra seguida de zero.
    palavras, [0 for i in range(len(palavras))]
))
# Palavras inseridas no dicionário, todas com zero aparições.

# Percorrendo o texto e contando as aparições.
for palavra in meu_texto.split():
    aparicoes[palavra] += 1

print(aparicoes['Guilherme']) # Resultado: 1
print(aparicoes['gosto']) # Resultado: 2
# print(aparicoes['xpto']) # Vai falhar: chave inexistente.

# Sintaxe com get impede erros de chave inexistente.
print(aparicoes.get('xpto')) # Resultado: None.
print(aparicoes.get('xpto', 0)) # Resultado: 0.
print(aparicoes.get('cachorro', 0)) # Resultado: 2.
```
# Mais operações de dicionários
## Como adicionar, alterar e remover elementos de um dicionário
```python
# Acrescentando elementos ao dicionário:
aparicoes['Carlos'] = 1

# Atualizando elementos no dicionário é a mesma coisa:
aparicoes['Carlos'] = 3

# Removendo elementos do dicionário:
del aparicoes['Carlos']
```
## Procurando elementos em um dicionário
As chaves são procuradas no dicionário usando o operador `in`.
```python
print("cachorro" in aparicoes) # Retorna True.
```
Para pesquisar nos valores, use a lista resultante da função `values()` do dicionário.

## Iterando sobre o dicionário
Os dicionários tem as seguintes funções:
1. `keys()`: retorna as chaves;
2. `values()`: retorna os valores;
3. `items()`: retorna as tuplas (key, val).

```python
# Iterando sobre as chaves do dicionário:
[ print(key) for key in aparicoes ]

# Outra forma de iterar sobre as chaves do dicionário:
[ print(key) for key in aparicoes.keys() ]
# Perceba a lista keys() retornada do dicionário aparicoes.

# Iterando sobre os valores do dicionário:
[ print(val) for val in aparicoes.values() ]
# Perceba a lista values() retornada do dicionário aparicoes.


# Acessando o dicionário por meio do índice:
[ print(key, aparicoes[key]) for key in aparicoes ]

# Usando o método items() do dicionário e tuplas temporárias:
[ print(tupla) for tupla in aparicoes.items() ]

# Desempacotando a tupla em valores separados:
[ print(key, '=', val) for key, val in aparicoes.items() ]
```

# Default dict
Lógica para a contagem de palavras de um texto:
```python
meu_texto = "Bem vindo meu nome é Guilherme eu gosto "\
            "muito de nomes e tenho o meu cachorro e "\
            "gosto muito de cachorro"

meu_texto = meu_texto.lower()

aparicoes = {}

for palavra in meu_texto.split():
    ate_agora = aparicoes.get(palavra, 0) 
    # Sem o get(), há o risco de não retornar um valor padrão.
    aparicoes[palavra] = ate_agora + 1

print(aparicoes)
```

A estrutura `defaultdict` recebe em seu construtor uma função que retorna o valor padrão para cada chave. No caso, a função `int()`, sem parâmetros, retorna zero.

```python
from collections import defaultdict

# A estrutura defaultdict recebe em seu construtor uma
# função que retorna o valor padrão para cada chave.
# No caso, a função int(), sem parâmetros, retorna zero.
aparicoes = defaultdict(int)

# Se você tentar acessar um elemento inexistente, ele 
# atribui o valor padrão produzido a partir da função
# fornecida como parâmetro na construção do defaultdict.
print(aparicoes['nome'])
print(aparicoes[1])
print(aparicoes)
# Resultado: defaultdict(<class 'int'>, {'nome': 0, 1: 0})

def funcao(parm=None):
    return 100

aparicoes = defaultdict(funcao)
aparicoes[0]
aparicoes[1] = 30
print(aparicoes)
# Resultado: 
# defaultdict(<function funcao at 0x00000275862F04A0>, 
#   {0: 100, 1: 30}
# )
```
# Counter
Usando um `defaultdict` para contar as palavras de um texto:
```python
aparicoes = defaultdict(int)

for palavra in meu_texto.split():
    # Se não achar a aparição da palavra, retorna zero.
    aparicoes[palavra] += 1 
print(aparicoes)
```
Usando construtores diferentes para o `defaultdict`:

```python
class Conta:
    def __init__(self):
        print("Criando uma conta")

contas = defaultdict(Conta)
print(contas[15]) # O objeto não existia ainda no defaultdict.
print(contas[17])
print(contas[15]) # O objeto agora existe no defaultdict.
# Resultado:
# Criando uma conta
# <__main__.Conta object at 0x0000023B50383710>
# Criando uma conta
# <__main__.Conta object at 0x0000023B50383750>
# <__main__.Conta object at 0x0000023B50383710> #Aqui o objeto já existia.
```
## A classe `Counter` do pacote `collections`
Há uma classe chamada `Counter` do pacote `collections`, que é um dicionário que recebe uma lista como parâmetro. Cada elemento da lista será uma chave do `Counter`, e o valor será a contagem dos elementos dessa lista.

```python
from collections import Counter
aparicoes = Counter(meu_texto.split())

print(aparicoes)
# Resultado: Counter({
#   'meu': 2, 
#   'gosto': 2, 
#   'muito': 2, 
#   'de': 2, 
#   'e': 2, 
#   'cachorro': 2, 
#   'bem': 1, 
#   'vindo': 1, 
#   'nome': 1, 
#   'é': 1, 
#   'guilherme': 1, 
#   'eu': 1, 
#   'nomes': 1, 
#   'tenho': 1, 
#   'o': 1}
# )
```
# Colocando tudo em prática
```python
from collections import Counter # Importando a classe Counter

def analisa_frequencia_de_letras(texto):
    # Criando um Counter a partir das letras em minúsculo.
    aparicoes = Counter(texto.lower())
    # Somando os *valores* da contagem.
    total_de_caracteres = sum(aparicoes.values())


    # Criando uma lista de tuplas composta pela letra 
    # e o percentual de frequência, para cada tupla 
    # retornada pelo dicionário com o método items().
    proporcoes = [
        (letra, frequencia / total_de_caracteres) 
        for letra, frequencia in aparicoes.items()
    ]
    # Exemplo de retorno: [ ('a', 20), ('b', 15), ... ]

    
    # O contador é criado a partir de um dicionário porque
    # se você usar a lista de tuplas diretamente, o que será
    # contado são as tuplas, e não o valor que corresponde
    # a cada tupla na (segunda posição).
    proporcoes = Counter(dict(proporcoes))
    
    # Mas se um Counter é um dicionário, por que não usar
    # apenas o dicionário? Por causa do método most_common.

    # O método most_common do objeto Counter retorna 
    # uma lista de tuplas com os valores mais comuns
    # e sua contagem.
    mais_comuns = proporcoes.most_common(10)

    print('Os 10 elementos mais comuns: ')
    # Iterando a lista de tuplas...
    for caractere, proporcao in mais_comuns:
        print(f"{caractere} => {proporcao * 100 :.2f}%")
        # Note a formatação de ponto flutuante:
        # começa com dois pontos, seguido de ponto,
        # e finalmente o número de casas decimais 
        # seguido do tipo (no caso, f de flutuante).

analisa_frequencia_de_letras(texto1)
analisa_frequencia_de_letras(texto2)
# Resultado:
# Os 10 elementos mais comuns: 
#   => 15.61%
# a => 12.59%
# e => 9.11%
# o => 7.54%
# s => 7.10%
# r => 6.76%
# i => 5.46%
# d => 3.88%
# t => 3.85%
# n => 3.52%
# Os 10 elementos mais comuns:
#   => 16.43%
# a => 11.05%
# o => 9.37%
# e => 7.83%
# r => 5.53%
# s => 5.48%
# i => 4.90%
# d => 4.08%
# m => 3.99%
# u => 3.84%
```
