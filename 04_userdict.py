# %%
oracao = '''
Senhor, muito obrigado por cada dia que estou contigo.
Pai, tudo é Teu, e, no Seu tempo, as coisas virão até mim.
'''

print(f'{oracao.strip()} Amém 🙏')
# %%
from collections import UserDict

# %%
ex1 = {}
ex1['collections'] = 'UserDict'
print(ex1)  # {'collections': 'UserDict'}

# %%


class MinhaDict(UserDict):
    pass


ex2 = MinhaDict()
print(ex2)  # {}

ex2['estudo'] = 'Collections'
print(ex2)  # {'estudo': 'Collections'}

print(ex2['estudo'])  # Collections


# %%
class MinhaDict2(UserDict):
    def __lshift__(self, value):
        self.data['fixo'] = value


ex3 = MinhaDict2()
print(ex3)  # {}

ex3 << 'python'
print(ex3)  # {'fixo': 'python'}

ex3 << 'collections'
print(ex3)  # {'fixo': 'collections'}

ex3['num'] = 245
print(ex3)  # {'fixo': 'collections', 'num': 245}


# %%
# Dessa forma __lshift__ seria basicamente um "atalho" para o __setitem__ que já existe.


class MinhaDict3(UserDict):
    def __lshift__(self, key_value):
        key, value = key_value  # ex: ('chave', 'valor')
        self.data[key] = value
        return self  # IMPORTANTE para encadear!


ex4 = MinhaDict3()
print(ex4)  # {}

ex4 << ('fixo2', 'python')
print(ex4)  # {'fixo2': 'python'}

ex4 << ('fixo2', 'collections')
print(ex4)  # {'fixo2': 'collections'}

ex4 << ('python', 'linguagem') << ('collections', 'modulo')
print(ex4)  # {'fixo2': 'collections', 'python': 'linguagem', 'collections': 'modulo'}

ex4['num'] = 245
print(
    ex4
)  # {'fixo2': 'collections', 'python': 'linguagem', 'collections': 'modulo', 'num': 245}


# %%
class MinhaDict4(UserDict):
    def __lshift__(self, value):
        self.data['fixo'] = value

    def __setitem__(self, key, value) -> None:
        self.data[key] = value


ex5 = MinhaDict4()
print(ex5)  # {}

ex5 << 'python'
print(ex5)  # {'fixo': 'python'}

ex5 << 'collections'
print(ex5)  # {'fixo': 'collections'}

ex5['num'] = 245
print(ex5)  # {'fixo': 'collections', 'num': 245}


# %%
class MinhaDict5(UserDict):
    def __lshift__(self, value):
        self.data['fixo'] = value

    def __setitem__(self, key, value):
        self.data[key] = value * 3  # modificado a estrutura


ex6 = MinhaDict5()
print(ex6)  # {}

ex6['num1'] = 245
print(ex6)  # {'num1': 735}


ex6['num2'] = 19
print(ex6)  # {'num1': 735, 'num2': 57}

# %%
