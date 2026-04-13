# Henrick149177
# Problema 1


def voto_obrigatorio(idade: int) -> bool:
    """
    Determina se uma pessoa que possui *idade* anos é obrigada a votar.
    Produz True se a pessoa for obrigada ou False caso contrário.
    Por lei hoje no Brasil, todo cidadão que tenha entre 18 e 69 anos
    é obrigado a votar ou justificar o seu voto em uma eleição.
    Exemplos:
    >>> voto_obrigatorio(17)
    False
    >>> voto_obrigatorio(18)
    True
    >>> voto_obrigatorio(50)
    True
    >>> voto_obrigatorio(70)
    False
    >>> voto_obrigatorio(71)
    False

    """
    return idade > 17 and idade < 70


# Verificação
# correção dos exemplo alterando o resultado para False.
# correção de verificação de idade de or para and.
# adição de um espaço para o exemplo rodar corretamente.
# Revisão
# nada a ser melhorado


# Problema 2
# Analise
# Descobrir quantas notas de determinado valor preciso para alcançar o valor requisitado pelo cliente
# Definição de tipos e de dados
# As informações são o valor da nota em reais, e o valor o qual ele quer chegar que também estará em reais.
# Vai retornar a quantidade de notas que cabem ali como numero inteiro.
# Especificação
def quantidade_notas(quantia: int, nota: int) -> int:
    """
    Determine a quantidade de *nota* que preciso para
    alcançar a *quantia* requisitada.
    Exemplos:
    >>> quantidade_notas(1000, 100)
    10
    >>> quantidade_notas(125, 100)
    1
    >>> quantidade_notas(2500, 50)
    50
    >>> quantidade_notas(9999, 100)
    99

    """
    return quantia // nota


# Verificação
# alterei a operação de nota//quantia para o correto que é quantia//nota
# Revisão
# Alterei a ordem de recebimento dos parametros para ficar menos confuso


# Problema 3
# Analise
# Formatar o título e a página de um capítulo para sempre ficar em uma linha, com letras maiúsculas
# e com o mesmo comprimento.
# Definição de tipos e de dados
# As informações recebidas são o titulo do capítulo e o número da página que ele começa.
# Retornará um uma string formatada comforme pedido.
# Especificação
def formatacao(titulo: str, pagina: int) -> str:
    """
    Formata *titulo* e *pagina* para o formato com letras maiúsculas e 30 caracteres.
    Exemplos:
    >>> formatacao('Hello word',1)
    'HELLO WORD...................1'
    >>> formatacao('Parte 3',22)
    'PARTE 3.....................22'
    >>> formatacao('Inicio do Fim',153)
    'INICIO DO FIM..............153'
    >>> formatacao('RUST',15)
    'RUST........................15'

    """
    pagina_str: str = str(pagina)
    numero_pontos: int = 30 - len(titulo) - len(pagina_str)
    pontos: str = numero_pontos * "."
    titulo = titulo.upper()
    return titulo + pontos + pagina_str


# Verificação
# Foi necessário trocar o exemplo de 01 para 1, pois estava processando como decimal
# Revisão
# Criação da variavel pontos para ficar mais claro e mehlorar a concatenação
