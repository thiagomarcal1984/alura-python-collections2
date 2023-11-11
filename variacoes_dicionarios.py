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
