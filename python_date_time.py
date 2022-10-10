from datetime import date



data_atual = date.today()
print(data_atual)

#
# Vamos a um exemplo concreto de datas e horários para poder programar
# em Python e com o módulo datetime: Uma empresa nos contratou para implementar
# o sistema de pontos deles, controlando quando um funcionário chega e sai.
# O sistema deve exibir a data e a hora a cada registro, como confirmação
# para o funcionário.

# Conhecemos o módulo datetime da biblioteca nativa do Python,
# então até sabemos pegar a data atual através da classe date,
# basta a importarmos e chamarmos o método today():


# Mas calma… como esperado? Seria legal se conseguíssemos imprimir a data
# no formato brasileiro DD/MM/AAAA para evitar confusões! O problema é que
# o date automaticamente força o padrão ANSI sempre que tentamos imprimir.

# Formatando nossa data em uma string
# Como a classe date consegue nos fornecer separadamente
# cada seção da data, podemos resolver esse problema com
# uma simples formatação de string:

data_em_texto = '{}/{}/{}'.format(data_atual.day, data_atual.month, data_atual.year)
print(data_em_texto)


