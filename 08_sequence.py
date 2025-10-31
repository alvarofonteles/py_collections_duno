'''Trabalhando com Sequence()'''

# %%
from collections.abc import Container, Iterable, Sized, Sequence


# %%
class MinhaSequencia2(Container, Iterable, Sized):
    def __init__(self, sequence):  # recebe uma sequencia [1, 2, 3] no construtor
        self.sequence = sequence

    def __contains__(self, value):  # verifica se contem na sequencia: x in y
        return value in self.sequence

    def __iter__(self):  # interacação com a sequencia: for x in y
        return iter(self.sequence)

    def __len__(self):  # verifica o tamanho da sequencia
        return len(self.sequence)


ex1 = MinhaSequencia2([1, 2, 3, 0])
print(ex1)  # <__main__.MinhaSequencia2 object at 0x00000144A2D6B2C0>

ret1 = 3 in ex1
print(ret1)  # True

ret2 = 8 in ex1
print(ret2)  # False

for x in ex1:
    print(x)  # 1 2 3 0

ret3 = len(ex1)
print(ret3)  # 4

print(isinstance(ex1, Container))  # True

print(isinstance(ex1, Iterable))  # True

print(isinstance(ex1, Sized))  # True

print(isinstance(ex1, Sequence))  # False


# %%
class MinhaSequencia3(Sequence):
    def __init__(self, sequencia):
        self.sequencia = sequencia

    def __len__(self):
        return len(self.sequencia)

    def __getitem__(self, posicao):  # pega a posicao(index) da sequencia
        return self.sequencia[posicao]


# Pronto! Já tem __contains__, __iter__ etc herdados
ex2 = MinhaSequencia3([1, 5, 6, 0])
print(ex2)  # <__main__.MinhaSequencia3 object at 0x00000144A2DB8BC0>


ret4 = 3 in ex1
print(ret4)  # True

ret5 = 8 in ex1
print(ret5)  # False

for x in ex2:
    print(x)  # 1 5 6 0

ret6 = len(ex2)
print(ret6)  # 4

print(isinstance(ex2, Sequence))  # True

print(isinstance(ex2, Container))  # True

print(isinstance(ex2, Iterable))  # True

print(isinstance(ex2, Sized))  # True
