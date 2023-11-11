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
