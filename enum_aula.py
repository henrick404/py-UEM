from enum import Enum, auto


class Cor(Enum):
    VERDE = auto()
    AMARELO = auto()
    VERMELHO = auto()


def proxima_cor(atual: Cor) -> Cor:
    """
    retorna a proxima cor que o semaforo assumira
    >>> proxima_cor(Cor.VERDE).name
    'AMARELO'
    >>> proxima_cor(Cor.AMARELO).name
    'VERMELHO'
    >>> proxima_cor(Cor.VERMELHO).name
    'VERDE'
    """

    if atual == Cor.VERDE:
        proxima = Cor.AMARELO
    elif atual == Cor.AMARELO:
        proxima = Cor.VERMELHO
    elif atual == Cor.VERMELHO:
        proxima = Cor.VERDE
    return proxima
