# 1 analise
# verifica se pode isentar o preço da pensagem com base na idade
# 2 definição
# colocar idade especificada em anos, saira um valo
# 3 especificação
def isento_tarifa(idade: int) -> bool:
    """
    Produz True se uma pessoa de *idade* anos é isento da tarifa de transporte público, isto é, tem menos que 18 anos ou 65 ou mais. Produz False caso contrário.
    Exemplos
    >>> isento_tarifa(17)
    True
    >>> isento_tarifa(18)
    False
    >>> isento_tarifa(50)
    False
    >>> isento_tarifa(65)
    True
    >>> isento_tarifa(70)
    True
    """
    return 17 >= idade or idade >= 65


# 1 analise
# transforma a data de padrão dia/mes/ano e um formato de ano/mes/dia
# 2 definição
# uma string organizada por dia/mes/ano e vai sair uma string ano/mes/dia
# 3 especificação
def dma_para_amd(data: str) -> str:
    """
    Transforma *data*, que deve estar no formato "dia/mes/ano", onde dia e mes tem dois dígitos e ano tem quatro dígitos, para o formato "ano/mes/dia".
    Exemplos:
    >>>dma_para_amd('02/07/1999')
    1999/07/02
    >>>dma_para_amd('09/03/2003')
    2003/03/09
    >>>dma_para_amd('20/09/2077')
    2077/09/20
    """
    dia: str = data[:2]
    mes: str = data[3:5]
    ano: str = data[6:]
    return ano + "/" + mes + "/" + dia


## 1 Análise
# verifica se está de acordo com a regra sem espaços extras, que diz que o texto não pode terminar nem começar com espaços.
# 2 Definição
# A informação recebida será um texto.
# As informações retornadas serão do tipo verdadeiro e falso
# 3 especificação
def tem_espaco(texto: str) -> bool:
    """
    Verifica se um texto tem espaço no inicio ou no fim.
     Exemplos:
     >>> tem_espaco(' Olá')
     True
     >>> tem_espaco('Olá ')
     True
     >>> tem_espaco('Olá')
     False
    """
    ultimo_caracter: str = texto[len(texto) - 1 :]
    primeiro_caracter: str = texto[:1]
    return primeiro_caracter == " " or ultimo_caracter == " "


import math
## 1 Análise
# inverter a sequencia dos numeros para ficar na sequencia correta considerando que não podemos usar operadores de string
# 2 Definição
# A informação recebida vai ser um numero inteiro positivo de 4 digitos
# A informação de saída será a ordem inversa desses numeros
# 3 especificação


def inverter(numero: int) -> int:
    """
    inverte a sequencia dos numeros recebidos usando módulo e divisão.
     Exemplos
     >>> inverter(1234)
     4321
     >>> inverter(9876)
     6789
     >>> inverter(1101)
     1011
    """
    numero_reserva: int = numero % 10
    numero = math.floor(numero / 10)
    numero_invertido: int = numero_reserva * 1000
    numero_reserva: int = numero % 10
    numero = math.floor(numero / 10)
    numero_invertido = numero_invertido + numero_reserva * 100
    numero_reserva: int = numero % 10
    numero = math.floor(numero / 10)
    numero_invertido = numero_invertido + numero_reserva * 10
    numero_invertido = numero_invertido + numero

    return numero_invertido

