'''Trabalhando com UserList()'''

# %%
from collections import UserList


# %%

ex = []
print(ex)  # []

ex.append(7)
print(ex)  # [7]

ex.append(15)
print(ex)  # [7, 15]


# %%
class MinhaLista(UserList):
    # somar
    def __add__(self, value):
        self.data.append(value)
        return self


ex1 = MinhaLista()
print(ex1)  # []

ret1 = ex1 + 7  # chama o __add__
print(ret1)  # [7]

_ = ex1 + 15  # Atribui a "_" (variável descartável)
print(ex1)  # [7, 15]


# %%
class MinhaLista2(UserList):
    # somar
    def __add__(self, value):
        # comportamento da lista normal
        if isinstance(value, list):  # de fato uma lista
            # return super().__add__(value)

            # extend modifica in-place, super().__add__ retorna novo objeto
            self.data.extend(value)  # Modifica in-place
        else:
            self.data.append(value)
        return self

    def __sub__(self, value):
        if value in self.data:
            self.data.remove(value)
            return self
        else:
            pass


ex2 = MinhaLista2()
print(ex2)  # []

# add
ret2 = ex2 + 7  # chama o __add__
print(ret2)  # [7]

ret2 = ex2 + 15
print(ret2)  # [7, 15]

ret2 = ex2 + [1, 2, 3]
print(ret2)  #  [7, 15, 1, 2, 3]

# sub
ret2 = ex2 - 2
print(ret2)  # [7, 15, 1, 3]
# %%
