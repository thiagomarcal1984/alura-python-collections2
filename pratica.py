texto1 = """
O grupo de 34 brasileiros autorizados a deixar a Faixa de Gaza nesta sexta-feira (10), depois de mais de um mês de guerra, segue aguardando a liberação para atravessar a fronteira com o Egito, pela passagem de Rafah, ainda sem previsões de quando o deslocamento será realizado.

A espera ocorre porque, por conta da guerra, o consenso entre as autoridades que controlam a fronteira é que as ambulâncias sempre têm prioridade para deixar o local - o que não está acontecendo por conta dos ataques às regiões em que estão os hospitais.

Há expectativas de que os brasileiros ainda possam ser autorizados a atravessar a fronteira neste sábado (11), desde que o comboio de ambulâncias que tenta deixar Gaza consiga realizar o deslocamento e chegar até o posto de comando em Rafah.

O ministro das Relações Exteriores, Mauro Vieira, porém, não dá certeza sobre a data de saída.

Brasileiros estão na expectativa para sair da Faixa de Gaza
Brasileiros estão na expectativa para sair da Faixa de Gaza

Por que as ambulâncias precisam sair antes?
Os hospitais enviam informações às autoridades sobre as ambulâncias e os feridos que precisam deixar Gaza para atendimento médico. Com esses dados, há uma mobilização na fronteira para que, assim que esses veículos cheguem ao local, possam ser liberados.

Dessa forma, enquanto as ambulâncias registradas para atravessar para o Egito não chegam, nenhum grupo de estrangeiros é liberado para sair.

No entanto, com os constantes ataques aos hospitais, as ambulâncias não conseguem se deslocar de um ponto a outro em segurança e, eventualmente, a fronteira fecha sem que ninguém consiga sair de Gaza.

Foi o que aconteceu nesta sexta com os brasileiros. O grupo, que faz parte da 7ª lista de estrangeiros que foi autorizado a deixar o território palestino, não pôde sair porque somente cinco ambulâncias conseguiram atravessar a fronteiro, e todas demoraram a conseguir fazer o deslocamento, afirmou o embaixador brasileiro em Gaza, Alessandro Candeias.

Segundo o embaixador, parte dessa demora é consequência da "forte presença militar israelense em combates ao redor de hospitais".

Como a passagem só fica aberta por poucas horas durante o dia - decisão de Israel e Egito, que afirmam que terroristas do Hamas podem atravessar a fronteira -, os ataques atrasam significativamente o processo de saída dos feridos e dos estrangeiros de Gaza.

Maior hospital da Faixa de Gaza para de funcionar por falta de combustível, diz Ministério da Saúde do Hamas

Brasileiros repatriados terão apoio para chegar ao país
De acordo com a agência de notícias do Governo Federal, todos os brasileiros que aguardam para deixar a Faixa de Gaza foram realocados em uma única residência em Rafah, para agilizar o traslado quando houver a autorização para atravessarem a fronteira.

O ministro Mauro Vieira, em coletiva de imprensa, disse que o grupo está reunido e conta com assistência financeira para alimentação e para custear as taxas de passagem na fronteira.
"""

texto2 = """
Ao menos 16 pessoas ficaram feridas, sendo uma em estado grave, durante um tumulto ocorrido numa promoção de uma loja no Centro de Macapá. Clientes relataram ao g1 que a confusão teria começado por volta das 19h, quando as portas foram abertas.

Vídeos divulgados em redes sociais mostram uma mulher sendo pisoteada e com sangramentos pelo corpo.

O g1 solicitou posicionamento da empresa proprietária da loja, mas até a publicação desta matéria não teve resposta.

Polícia Militar foi acionada para controlar a multidão — Foto: Rafael Aleixo/g1

Francisco Barbosa da Silva é filho de Fúlvia de Jesus de Barbosa, de 53 anos, que está internada em estado grave no HE da capital. Ele relatou que estava próxima da mãe, mas que não conseguiu ajudar de imediato por conta da multidão.

“Fomos cedo pra lá, às 17h. Fomos comprar um guarda-roupas e uma fritadeira elétrica. Ela foi arredando e começaram a empurrar ela. Ela tentou sair, mas foram arrastando ela pra dentro e ela não conseguiu sair. Pisaram nela. O vidro quebrou e ela ficou muito ferida”, disse o filho.

A Secretaria de Estado da Saúde (Sesa) informou que o Serviço de Atendimento Móvel de Urgência (Samu) havia socorrido ao menos 16 pessoas, mas que esse número poderia aumentar.

A autônoma Joelly Valério ficou ferida em uma das pernas após a porta de vidro da loja quebrar.

“No começo era muita confusão e o pessoal ia empurrando a gente. A gente andava pelo impulso das pessoas de trás, e foi quando quebrou a porta de vidro. Eu caí de joelhos no chão e vi muitas pessoas feridas. Faltou um pouco mais de organização e segurança”, disse a autônoma.

A Polícia Militar foi acionada e controlou o tumulto minutos depois, como explicou o capitão oficial de operações Márcio Silva Lima.

“Se acumularam muitos consumidores aqui na entrada e na hora que abriram os portões para fazer as vendas houve um tumulto e algumas pessoas foram pisoteadas. Foi acionado o Corpo de Bombeiros para fazer a condução dos feridos até o Hospital de Emergência. Fizemos o controle da ordem pública aqui no local”, informou o capitão.
"""
from collections import Counter
def analisa_frequencia_de_letras(texto):
    aparicoes = Counter(texto.lower())
    total_de_caracteres = sum(aparicoes.values())


    proporcoes = [
        (letra, frequencia / total_de_caracteres) 
        for letra, frequencia in aparicoes.items()
    ]

    proporcoes = Counter(dict(proporcoes))
    
    # Os 10 elementos mais comuns.
    mais_comuns = proporcoes.most_common(10)
    print('Os 10 elementos mais comuns: ')
    for caractere, proporcao in mais_comuns:
        print(f"{caractere} => {proporcao * 100 :.2f}%")
        # Note a formatação de ponto flutuante:
        # começa com dois pontos, seguido de ponto,
        # e finalmente o número de casas decimais 
        # seguido do tipo (no caso, f de flutuante).

analisa_frequencia_de_letras(texto1)
analisa_frequencia_de_letras(texto2)
