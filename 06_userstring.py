'''Trabalhando com UserString()'''

# %%
from collections import UserString


# %%
class MinhaString(UserString):  # Herda de UserString
    # Não precisa de __init__ porque herda o pai
    pass


# O UserString já tem um __init__ que espera:
# UserString(seq) onde seq é a string inicial

# ex1 = MinhaString()
# print(ex1)  # __init__() Argument missing for parameter "seq"

ex2 = MinhaString('é bom, Deus é bom, o tempo todo!')
print(ex2)  # é bom, Deus é bom, o tempo todo!

print(ex2.upper())  # É BOM, DEUS É BOM, O TEMPO TODO!

ex2 = ex2.capitalize()
print(ex2)  # É bom, Deus é bom, o tempo todo!


# %%
# Conteúdo antigo Python 2+
class MinhaString2(UserString):
    def __iter__(self):
        return iter(self.data)

    def next(self):
        for x in self.data:
            yield x  # Pausa aqui e retorna x, continua na próxima vez


# __iter__
ex3 = MinhaString2('Deus')
for char in ex3:
    print(char)  # D e u s

# next
ex4 = MinhaString2('Deus')
for char in ex4.next():  # next() é um gerador
    print(char)  # D e u s


# %%
class MinhaString3(UserString):  # Herda de UserString
    def exclamar(self):
        return self.data + "!!!"

    def duplicar(self):
        return self.data * 2


texto = MinhaString3("Python")
print(texto.data)  # "Python"

print(texto.exclamar())  # Python!!!

print(texto.duplicar())  # PythonPython

# %%
