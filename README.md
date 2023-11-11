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
