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
print(dicionario)



meu_texto = "Bem vindo meu nome é Guilherme eu gosto "\
            "muito de nomes e tenho o meu cachorro e "\
            "gosto muito de cachorro"

print(meu_texto)

# Criar o conjunto de palavras, para remover repetições.
palavras = {*meu_texto.split()} 
print(palavras)

# Criar o dicionário de aparições com o construtor dict.
aparicoes = dict(zip( 
    # zip() forma uma lista de tuplas com 
    # cada palavra seguida de zero.
    palavras, [0 for i in range(len(palavras))]
))
# Palavras inseridas no dicionário, todas com zero aparições.
print(aparicoes)

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
