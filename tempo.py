from dataclasses import dataclass


@dataclass
class Tempo:
    horas: int
    minutos: int
    segundos: int


def tempo_para_string(t: Tempo) -> str:
    """
    Converte *t* em uma mensagem para o usuário. Cada componente de *t* aparece
    com a sua unidade, mas se o valor do componente for 0, ele não aparece na
    mensagem. Os componentes são separados com "e" ou "," respeitando as regras
    do Português. Se *t* for Tempo(0, 0, 0), devolve "0 segundo(s)".
    >>> tempo_para_string(Tempo(0, 0, 0))
    '0 segundo(s)'
    >>> tempo_para_string(Tempo(0, 0, 10))
    '10 segundo(s)'
    >>> tempo_para_string(Tempo(0, 1, 20))
    '1 minuto(s) e 20 segundo(s)'
    >>> tempo_para_string(Tempo(0, 2, 0))
    '2 minuto(s)'
    >>> tempo_para_string(Tempo(1, 2, 1))
    '1 hora(s), 2 minuto(s) e 1 segundo(s)'
    >>> tempo_para_string(Tempo(4, 0, 25))
    '4 hora(s) e 25 segundo(s)'
    >>> tempo_para_string(Tempo(2, 4, 0))
    '2 hora(s) e 4 minuto(s)'
    >>> tempo_para_string(Tempo(3, 0, 0))
    '3 hora(s)'
    """
    h: str = str(t.horas) + " hora(s)"
    m: str = str(t.minutos) + " minuto(s)"
    s: str = str(t.segundos) + " segundo(s)"

    if t.horas == 0 and t.minutos == 0:
        hora_escrita: str = s
    elif t.horas == 0 and t.minutos != 0 and t.segundos == 0:
        hora_escrita: str = m
    elif t.horas != 0 and t.minutos == 0 and t.segundos == 0:
        hora_escrita: str = h
    elif t.horas == 0 and t.minutos != 0 and t.segundos != 0:
        hora_escrita: str = m + " e " + s
    elif t.horas != 0 and t.minutos == 0 and t.segundos != 0:
        hora_escrita: str = h + " e " + s
    elif t.horas != 0 and t.minutos != 0 and t.segundos == 0:
        hora_escrita: str = h + " e " + m
    elif t.horas != 0 and t.minutos != 0 and t.segundos != 0:
        hora_escrita: str = h + ", " + m + " e " + s

    return hora_escrita
