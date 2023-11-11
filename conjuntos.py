usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

print('Lista usuarios_data_science:', usuarios_data_science)
print('Lista usuarios_machine_learning:', usuarios_machine_learning)

# O comando copy das listas copia apenas a referência
# aos objetos, ele não copia cada objeto completamente.
# Isso é chamado de shallow copy (cópia rasa).
assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)

print("Imprimir uma lista com a combinação das outras duas:")
print(assistiram)

# Conjuntos (sets) são listas sem repetição de elementos.
print("Imprimir um conjunto com a combinação das duas listas:")
print(set(assistiram))
print("Usando desempacotamento das duas listas com asterisco (*):")
print(set([ # Desempacota a lista em parâmetros separados.
    *usuarios_data_science, 
    *usuarios_machine_learning,
]))

print("Outra forma de criar sets é usando chaves {}:")
print({*usuarios_data_science, *usuarios_machine_learning})

print("Sets não permitem busca por índice (conj[0], por exemplo)")
print("Nos sets não há ordem.")
conjunto = {3,2,1} # Criação de um set.
# print(conjunto[1]) # Este código vai falhar.

print('Há ainda o operador "ou" (pipe, |) para unir conjuntos:')
print({1,2,3} | {2,4,6})
print('O operador "ou" (pipe, |) não funciona para listas.')
# print([1,2,3] | [2,4,6]) # Vai quebrar.
