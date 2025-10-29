'''
Trabalhando com OrderedDict().

No Python 3.7+, dicts normais JÁ mantêm ordem por padrão!
OrderedDict é útil apenas para métodos especiais: move_to_end() e popitem()
'''

'''
Mudança na representação do OrderedDict

Python < 3.8:
OrderedDict([(2, 'dois'), (3, 'tres'), (4, 'quatro'), (1, 'um')])

Python 3.8+:
OrderedDict({2: 'dois', 3: 'tres', 4: 'quatro', 1: 'um'})
'''
# %%
from collections import OrderedDict

digito = [2, 3]
string = ['dois', 'tres']

# Versão com for (mais verbosa)
ex1 = dict((digito, string) for digito, string in zip(digito, string))
print(ex1)  # {2: 'dois', 3: 'tres'}

# Versão direta (mais pythonica)
ex1_1 = dict(zip(digito, string))
print(ex1_1)  # {2: 'dois', 3: 'tres'}

digito.append(4)
string.append('quatro')

ex1_1 = dict(zip(digito, string))
print(ex1_1)  # {2: 'dois', 3: 'tres', 4: 'quatro'}

# %%
digito2 = [2, 3]
string2 = ['dois', 'tres']

numero = [(digito2, string2) for digito2, string2 in zip(digito2, string2)]
print(f'numero 1 = {numero}')  # numero 1 = [(2, 'dois'), (3, 'tres')]

numero.append((5, 'cinco'))
print(f'numero 2 = {numero}')  # numero 2 = [(2, 'dois'), (3, 'tres'), (5, 'cinco')]

numero.append((4, 'quatro'))
print(
    f'numero 3 = {numero}'
)  # numero 3 = [(2, 'dois'), (3, 'tres'), (5, 'cinco'), (4, 'quatro')]

# %%
# OrderedDict mantém a ordem de inserção (igual dict normal)
#
ex2 = OrderedDict()
ex2[0] = 'Linus'
print(ex2)  # OrderedDict({0: 'Linus'})

ex2[99] = 'Live'
print(ex2)  # OrderedDict({0: 'Linus', 99: 'Live'})

ex2.update({3: 'Jogo'})
print(ex2)  # OrderedDict({0: 'Linus', 99: 'Live', 3: 'Jogo'})

for x in ex2:
    print(x)  # 0 99 3

##
ex2 = OrderedDict(ex1_1)
print(ex2)  # OrderedDict({2: 'dois', 3: 'tres', 4: 'quatro'})

ex2.update({1: 'um'})
print(ex2)  # OrderedDict({2: 'dois', 3: 'tres', 4: 'quatro', 1: 'um'})

# %%
# Para ordenação por itens usar sorted()
ex3 = OrderedDict(sorted(ex2.items()))
print(ex3)  # OrderedDict({1: 'um', 2: 'dois', 3: 'tres', 4: 'quatro'})
ex3 = OrderedDict(sorted([(1, 'b'), (2, 'd'), (3, 'a'), (4, 'c')], key=lambda x: x[1]))
print(ex3)  # OrderedDict({3: 'a', 4: 'b', 1: 'c', 2: 'd'})
# %%
#
#
# MÉTODOS ÚNICOS DO OrderedDict (que dict normal NÃO tem)
digito3 = [2, 3, 1]
string3 = ['dois', 'tres', 'um']

# move_to_end() - Move chave para início ou final
od = OrderedDict(zip(digito3, string3))
print("Original:", od)  # OrderedDict({2: 'dois', 3: 'tres', 1: 'um'})
# %%
# Move a ordem ATUAL
od.move_to_end(2)  # Move chave 2 para o final
print("move_to_end(2):", od)  # OrderedDict({3: 'tres', 1: 'um', 2: 'dois'})

# Agora trabalha na NOVA ordem
od.move_to_end(1, last=False)  # Move chave 1 para o início
print("move_to_end(1, last=False):", od)  # OrderedDict({1: 'um', 3: 'tres', 2: 'dois'})

# popitem() - Remove do início ou final
# Remove do final (padrão)
removido_final = od.popitem()  # Remove o ÚLTIMO da ordem atual
print(
    f"popitem(): removido {removido_final} ->", od
)  # popitem(): removido (2, 'dois') -> OrderedDict({1: 'um', 3: 'tres'})

# Remove do início
removido_inicio = od.popitem(last=False)  # Remove o PRIMEIRO da ordem atua
print(
    f"popitem(last=False): removido {removido_inicio} ->", od
)  # popitem(last=False): removido (1, 'um') -> OrderedDict({3: 'tres'})

# %%
