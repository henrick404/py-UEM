#1 Analise
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
#2
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
#3
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
#4
from enum import Enum, auto
from dataclasses import dataclass


class Conceito(Enum):
    A = auto()
    B = auto()
    C = auto()
    D = auto()


@dataclass
class Desempenho:
    media: float
    conceito: Conceito


def media_aluno(
    nota1: float, peso1: int, nota2: float, peso2: int, nota3: float, peso3: int
) -> Desempenho:
    

    saida: Desempenho = Desempenho(
        ((nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / 3), Conceito.D
    )

    if saida.media > 8.0:
        saida.conceito = Conceito.A
    elif saida.media > 7.0:
        saida.conceito = Conceito.B
    elif saida.media > 5.0:
        saida.conceito = Conceito.C

    return saida


# ----------------------------------------------
from enum import Enum, auto
from dataclasses import dataclass


class Saida(Enum):
    QUADRANTE1 = auto()
    QUADRANTE2 = auto()
    QUADRANTE3 = auto()
    QUADRANTE4 = auto()
    EIXO_X = auto()
    EIXO_Y = auto()
    ORIGEM = auto()


@dataclass
class Cordenadas:
    x: int
    y: int


def determina_posicao(posicao: Cordenadas) -> Saida:
    """
    determina o quadrante com base na *posicao* passada
    Exemplos:
    >>> determina_posicao(Cordenadas(1,1)).name
    'QUADRANTE1'
    >>> determina_posicao(Cordenadas(0,0)).name
    'ORIGEM'
    >>> determina_posicao(Cordenadas(-1,-1)).name
    'QUADRANTE3'
    >>> determina_posicao(Cordenadas(0,1)).name
    'EIXO_Y'
    """
    x: int = posicao.x
    y: int = posicao.y
    if x == 0 and y == 0:
        retorno: Saida = Saida.ORIGEM
    elif x == 0 and y != 0:
        retorno: Saida = Saida.EIXO_Y
    elif x != 0 and y == 0:
        retorno: Saida = Saida.EIXO_X
    elif x > 0 and y > 0:
        retorno: Saida = Saida.QUADRANTE1
    elif x < 0 and y > 0:
        retorno: Saida = Saida.QUADRANTE2
    elif x < 0 and y < 0:
        retorno: Saida = Saida.QUADRANTE3
    else:
        retorno: Saida = Saida.QUADRANTE4

    return retorno
#------------------------------------------------
from dataclasses import dataclass

@dataclass
class Saida:
    numero_raizes: int
    x1: float
    x2: float


def delta(a: int, b: int, c: int) -> int:
    """
    calcula o delta com base em *a*, *b* e *c*
    """
    return (b**2) - (4 * a * c)


def raizes(a: int, b: int, c: int) -> Saida:

    valor_delta: int = delta(a, b, c)
    if valor_delta < 0:
        retorno: Saida = Saida(0, 0, 0)
    elif valor_delta == 0:
        raiz: float = round(-b / (2 * a), 2)
        retorno: Saida = Saida(1, raiz, 0)
    else:
        raiz1: float = round((-b + valor_delta**0.5) / (2 * a), 2)
        raiz2: float = round((-b - valor_delta**0.5) / (2 * a), 2)
        retorno: Saida = Saida(2, raiz1, raiz2)
    return retorno


# ------------------------------------------------
# Analise
# Descobrir o tempo de duraçãqo de um jogo com base no inicio e termino dele
# Definição Tipos
# Recebimento dos valores horas de inicio e termino e os minutos tambem
# de inicio e termino, todos do tipo inteiro.
# saida: o tempo de duração em horas e minutos em inteiro

from dataclasses import dataclass


@dataclass
class Tempo:
    """
    Guarda um horário
    """

    horas: int
    minutos: int


def duracao(inicio: Tempo, final: Tempo) -> Tempo:
    """
    Receba o *início* de um jogo e o *final* do jogo e calcula o tempo de duração
    do jogo (horas e minutos) sabendo-se que o tempo máximo de duração do jogo é
    de 24 horas e que o jogo pode iniciar em um dia e terminar no dia seguinte.
    Exemplos:
    >>> duracao(Tempo(1,20),Tempo(2,20))
    Tempo(horas=1, minutos=0)
    >>> duracao(Tempo(19,20),Tempo(2,30))
    Tempo(horas=7, minutos=10)
    >>> duracao(Tempo(19,20),Tempo(2,10))
    Tempo(horas=6, minutos=50)
    >>> duracao(Tempo(0,20),Tempo(0,40))
    Tempo(horas=0, minutos=20)
    >>> duracao(Tempo(0,0),Tempo(23,59))
    Tempo(horas=23, minutos=59)
    """
    diferenca: Tempo = Tempo(0, 0)

    if inicio.horas <= final.horas:  # 1
        diferenca.horas = (inicio.horas - final.horas) * (-1)
    else:
        diferenca.horas = 24 - (inicio.horas - final.horas)

    if inicio.minutos <= final.minutos:  # 2
        diferenca.minutos = (inicio.minutos - final.minutos) * (-1)
    else:
        diferenca.minutos = 60 - (inicio.minutos - final.minutos)

    if inicio.horas > final.horas and inicio.minutos > final.minutos:  # 3
        diferenca.horas = diferenca.horas - 1

    return diferenca


# Verificacao
# alteração do from dataclass para from dataclasses
# adição do @dataclass que não estava
# alteração dos exemplos para não dar conflito  de decimal
# tratamento de erro com o if3
# Revisão
# nada a ser melhorado
#----------------------------------
