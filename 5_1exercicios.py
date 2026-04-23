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
