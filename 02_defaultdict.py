'''Trabalhando com defaultdict()'''

# %%
config = {}

config['css']
print(config['css'])  # KeyError: 'css'

# %%
config['css'] = '00f'
print(config['css'])  # 00f

# %%
from collections import defaultdict
from math import dist
from typing import Any, cast

# Anonima

# Type checker error
# func_anonima = lambda: None
# print(func_anonima()) # None

# Retorna o tipo Any
# func_anonima = lambda: Any
# print(func_anonima()) # typing.Any

# Correção com cast(Any, None)
func_anonima = lambda: cast(Any, None)
# print(func_anonima())  # None

# Nomeada

# Type checker error
# def func_none() -> None:
#    return None
# print(func_none())  # None


# Correção com (Any)
def func_none() -> Any:
    return None


# print(func_none())  # None

config2 = {}
# Com Anonimo
config2 = defaultdict(func_anonima)

# Com Nomeada
config2 = defaultdict(func_none)

print(config2['css'])  # None
print(config2['html'])  # None

config2.update({'css': '00a', 'html': '<body><body/>'})
print(
    config2
)  # defaultdict(<function func_none at 0x000001E140EFF9C0>, {'css': '00a', 'html': '<body><body/>'})

print(config2['css'])  # 00a
print(config2['html'])  # <body><body/>

# %%
'''
Caso de Uso Real do defaultdict()

O que é? 
Um dicionário que automaticamente cria valores padrão para chaves inexistentes!
Por que usar?
Elimina verificações manuais `if chave not in dict` e deixa o código mais limpo e Pythonico.

Em vez de:
if chave not in meu_dict:
    meu_dict[chave] = []
meu_dict[chave].append(valor)

Use:
meu_dict = defaultdict(list)
meu_dict[chave].append(valor)  # Mais limpo e Pythonico!
'''

# %%
# CONTAGEM - muito comum!
texto = 'tudo bem, já dar tudo certo, Deus é Deus e conosco, Amém'
contador = defaultdict(int)
for palavra in texto.split():
    contador[palavra] += 1  # Primeiro acesso cria com 0, depois incrementa
print(
    dict(contador)
)  # {'tudo': 2, 'bem,': 1, 'já': 1, 'dar': 1, 'certo,': 1, 'Deus': 2, 'é': 1, 'e': 1, 'conosco,': 1, 'Amém': 1}


# %%
# AGRUPAMENTO
class Pessoa:
    def __init__(self, nome, departamento) -> None:
        self.nome = nome
        self.departamento = departamento


pessoas = [
    Pessoa('Eduardo', 'Python'),
    Pessoa('Duno', 'Professora'),
]

grupos = defaultdict(list)
for pessoa in pessoas:
    grupos[pessoa.departamento].append(pessoa.nome)  # Cria lista se não existir
print(dict(grupos))  # {'Python': ['Eduardo'], 'Professora': ['Duno']}


# %%
# ACUMULADORES
class Venda:
    def __init__(self, valor, categoria) -> None:
        self.valor = valor
        self.categoria = categoria


vendas = [
    Venda(1035, 'Cama'),
    Venda(2057, 'Cama'),
    Venda(2454.25, 'Televisao'),
    Venda(3454.25, 'Televisao'),
]

total_por_categoria = defaultdict(float)
for venda in vendas:
    total_por_categoria[venda.categoria] += venda.valor  # Cria com 0.0
print(dict(total_por_categoria))
# %%
