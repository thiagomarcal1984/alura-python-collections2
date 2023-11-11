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

a, b = {1,2,3,4,5}, {2,4,6,8}
print('O operador "ou" (pipe, |) une conjuntos:')
print(a | b) 

print('O operador "e" (ampersand, &) retorna a interseção:')
print(a & b) 
# Resultado: {2, 4}

print('O operador "diferença" (hifen, -) retorna a diferença.')
print('Repare que a ordem dos conjuntos afeta o resultado:')
print(a - b) # Resultado: {1, 3, 5}
print(b - a) # Resultado: {8, 6}

print('O operador "ou exclusivo" (caret, ^) retorna a união menos a interseção:')
print(a ^ b) # 2 e 4 estão na interseção; não aparecem no resultado.
# Resultado: {1, 3, 5, 6, 8}
