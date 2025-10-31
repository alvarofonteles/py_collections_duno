'''Trabalhando com Container()'''

# %%
from collections.abc import Container


# %%
class MeuConteiner(Container):
    pass


'''ex1 = (
    MeuConteiner()
)  # TypeError: Can't instantiate abstract class MeuConteiner without an implementation for abstract method '__contains__'
print(ex1)'''


# %%
class MeuConteiner2(Container):
    def __init__(self, value):
        self.data = value

    def __contains__(self, value):
        return value in self.data


ex2 = MeuConteiner2('Deus, gratidão!')

print(ex2)  # <__main__.MeuConteiner2 object at 0x00000144A2EC97C0>

# Abstração de um Container
ret1 = 'Deus' in ex2
print(ret1)  # True

ret1 = 'Deuses' in ex2
print(ret1)  # False

ret2 = isinstance(ex2, Container)  # Pois herda
print(ret2)  # True


# %%
class MeuConteiner3:  # Sem herança
    def __init__(self, value):
        self.data = value

    def __contains__(self, value):  # Mas tem a representação
        return value in self.data


ex2 = MeuConteiner3('Deus, gratidão!')
print(ex2)  # <__main__.MeuConteiner2 object at 0x00000144A2EC97C0>

# Abstração de um Container
ret1 = 'Deus' in ex2
print(ret1)  # True

ret1 = 'Deuses' in ex2
print(ret1)  # False

ret2 = isinstance(
    ex2, Container
)  # Mesmo sem Herança, mas com     def __contains__(self, value): # Mas tem a representação
print(ret2)  # True
