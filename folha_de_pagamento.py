# 1 Analise
# Calcular o salario de cada funcionario levando em conta o total de gratificações e de imposto.
# 2 Definição de tipos
# As informações são salario base e salario liquido que serão expresso em R$,
# a gratificação e o imposto serão expressos em porcentagem.
# 3 Especificação
def salario(salario_base: float) -> float:
    """
    Calcula o valor em reais  que o funcionario irá
    receber considerando imposto e gratificações.
    Exemplos
    salario(1500.00)
    1.441.80
    salario(2000.00)
    1922.40
    salario(10000.00)
    9612.00
    """
    gratificacoes: float = salario_base * 0.08
    total_vantagens: float = salario_base + gratificacoes
    imposto: float = total_vantagens * 0.11
    salario_liquido: float = total_vantagens - imposto
    return round(salario_liquido, 2)
