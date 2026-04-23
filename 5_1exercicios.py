# Analise
# descobrir o peso ideal com base nas informações recebidas
# Tipos de dados
# dados a receber: sexo em tipo genero, e altura em float
# dados devolvidos: peso ideal em float

from enum import Enum, auto


class Genero(Enum):
    """O genero de uma pessoa"""

    FEMININO = auto()
    MASCULINO = auto()


def peso_ideal(sexo: Genero, altura: float) -> float:
    """
    calcula o peso ideal de uma pessoa baseado em *sexo*, sendo a operação
    (72.7 * altura) – 58 para homens, e (62.1 * altura) – 44.7 para mulheres
    Exemplos:
    >>>peso_ideal(Genero.MASCULINO, 2.0)
    87.4
    >>>peso_ideal(Genero.MASCULINO, 1.0)
    14.7
    >>>peso_ideal(Genero.FEMININO, 1.0)
    17.7

    """
    if sexo == Genero.MASCULINO:
        peso: float = (72.7 * altura) - 58
    else:
        peso: float = (62.1 * altura) - 44.7

    return round(peso, 1)

#-------------------------------------------------
# Analise
# Descobrir se um número é positivo, negativo ou nulo
# Tipos de dados
# dados a receber: um número do tipo int
# dados devolvidos: tipo do numero positivo, negativo ou nulo

from enum import Enum, auto

class Valor(Enum):
    "se é positivo negatipo ou nulo"

    POSITIVO = auto()
    NEGATIVO = auto()
    NULO = auto()

def sinal(numero: int) -> Valor:
    """
    Descobre se um *numero* é negativo, positivo ou nulo
    Exemplos:
    >>> sinal(1).name
    'POSITIVO'
    >>> sinal(-1).name
    'NEGATIVO'
    >>> sinal(0).name
    'NULO'
    """
    if numero > 0:
        sinal: Valor = Valor.POSITIVO
    elif numero < 0:
        sinal: Valor = Valor.NEGATIVO
    else:
        sinal: Valor = Valor.NULO

    return sinal

# -------------------------------------------------
# Analise
# Descobrir o valor total de uma compra
# Tipos de dados
# dados a receber: o código do produto do tipo Codigo, e a quantidade do tipo int
# dados devolvidos: valor total da compra em float

from enum import Enum, auto


class Codigo(Enum):
    C1001 = auto()
    C1324 = auto()
    C6548 = auto()
    C2987 = auto()
    C7623 = auto()


def valor_total(codigo: Codigo, quantia: int) -> float:
    """
    Calcula o valor de uma compra com base no preço do produto e com base na *quantia*
    Exemplos:
    >>> valor_total(Codigo.C1001,5)
    26.6
    >>> valor_total(Codigo.C1324,10)
    64.5
    >>> valor_total(Codigo.C7623,7)
    45.15
    """
    if codigo == Codigo.C1001 or Codigo.C2987:
        total: float = quantia * 5.32
    elif codigo == Codigo.C1324 or Codigo.C7623:
        total: float = quantia * 6.45
    else:
        total: float = quantia * 2.37

    return total
#----------------------------------------------------- 
