# Variáveis são usadas para salvar algo na memória do computador.
# PEP8: inicie variáveis com letras minúsculas, pode usar
# números e underline _.
# O sinal de = é o operador de atribuição. Ele é usado para
# atribuir um valor a um nome (variável).
# Uso: nome_variavel = expressão

nome_completo = 'Luiz Otávio Miranda'
soma_dois_mais_dois = 2 + 2
int_um = int('1')


print(int_um, type(int_um))
print('-----------------------')

print(int('1'), type(int('1')))
print('-----------------------')

print(nome_completo)
print('-----------------------')

print(soma_dois_mais_dois)

nome = 'Luiz'
idade = 20
maior_de_idade = idade >= 18
print('Nome:', nome, 'Idade:', idade)
print('-----------------------')

print('É maior?', maior_de_idade)