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
