# Analise
# calcular o peso ideal de uma pessoa com base em altura e sexo.

# Definição de tipos
# informações recebidas:altura em metros(float) e o sexo em F ou M(string)
# informações devolvidas: peso ideal em string
# Especificação
def peso_ideal(altura: float, genero: str) -> float:
    """
    Calcula o peso ideal de uma pessoa pela conta (72.7 * altura) – 58 para o caso de *genero* for M,
    e (62.1 * altura) – 44.7 no caso de *genero ser F.
    Exemplos:
    >>> peso_ideal(2.0,'F')
    79.5
    >>> peso_ideal(2.0,'M')
    87.4
    >>> peso_ideal(1.0,'M')
    14.7
    """
    if genero == "F":
        ideal: float = (62.1 * altura) - 44.7
    else:
        ideal: float = (72.7 * altura) - 58

    return round(ideal, 1)


# Verificação
# correção nos exemplos trocando para string ao invés de um valor inválido
# Revisão
# Nada a melhorar
