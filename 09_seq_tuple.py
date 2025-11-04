'''Trabalhando com Sequence()'''

# %%
from collections.abc import Sequence
from itertools import chain


class MinhaTupla(Sequence):
    def __init__(self, tupla_):
        self._data = tuple(tupla_)

    def __getitem__(self, idx):
        return self._data[idx]

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return f'Sua Tupla {self._data}'


ex1 = MinhaTupla([1, 2, 3])
print(ex1)  # Sua Tupla (1, 2, 3)

print(ex1[2])  # 3
print(ex1.count(2))  # 1
print(ex1.index(2))  # 1 (idx) → ÍNDICE onde está o valor 2

print(ex1[ex1.index(2)])  # 2 (val) → VALOR no índice 1 (que é 2)


# %%
# Set é mutável mas não se repete
set_ = {1, 2, 3, 3, 3, 3}
print(set(set_))  # {1, 2, 3}

set_.add(4)
print(set(set_))  # {1, 2, 3, 4}

set_ = {1}
print(set(set_))  # {1} Cria OUTRO set (não modifica)


# %%
class MinhaTupleSet(Sequence):
    def __init__(self, tuple_):
        tup = []
        for value in tuple_:
            if value not in tup:
                tup.append(
                    value
                )  # comportamento idêntico ao Set {1, 2, 3, 3, 3, 3} # {1, 2, 3}
        self._data = tuple(tup)

    def __getitem__(self, idx):
        return self._data[idx]

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return f'Sua TuplaSet {self._data}'


# Tupla é imutável mas se repete
tup = (1, 2, 3, 3, 3, 3)
print(tup[3])  # 3
print(tup)  # (1, 2, 3, 3, 3, 3)

ex2 = MinhaTupleSet([1, 2, 3, 3, 3, 3])
print(ex2)  # Sua TuplaSet (1, 2, 3)

for x in ex2:
    print(x)  # 1, 2, 3


# %%
class MinhaTupleSetOrds(Sequence):
    def __init__(self, tuple_, ordered=False):
        tup = []
        for value in tuple_:
            if value not in tup:
                tup.append(
                    value
                )  # comportamento idêntico ao Set {1, 2, 3, 3, 3, 3} # {1, 2, 3}
        self._data = tuple(tup) if not ordered else tuple(sorted(tup))

    def __getitem__(self, idx):
        return self._data[idx]

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return f'Sua TuplaSet {self._data}'


ex3 = MinhaTupleSetOrds([1, 4, 5, 2, 3, 3, 3, 3, 8, 10, 10, 10, 6])  # Ordenada
print(ex3)  # Sua TuplaSet (1, 4, 5, 2, 3, 8, 10, 6)

for x in ex3:
    print(x)  # 1, 4, 5, 2, 3, 8, 10, 6

ex4 = MinhaTupleSetOrds(
    [1, 4, 5, 2, 3, 3, 3, 3, 8, 10, 10, 10, 6], True
)  # Não Ordenada
print(ex4)  # Sua TuplaSet (1, 2, 3, 4, 5, 6, 8, 10)

for x in ex4:
    print(x)  # 1, 2, 3, 4, 5, 6, 8, 10

# %%


class MinhaTuplaFlat(Sequence):
    def __init__(self, tupla_):
        self._data = tuple(sum(tupla_, []))

    def __getitem__(self, idx):
        return self._data[idx]

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return f'Sua TuplaFlat {self._data}'


# Comportamento Flat Normal (Achatar)
ex5 = [1, 2, 3, 4, 5]
ex6 = [6, 7, 8, 9]

print([ex5, ex6])  # [[1, 2, 3, 4, 5], [6, 7, 8, 9]]

print(
    sum([ex5, ex6], [])
)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]  Achata listas aninhadas (remove estrutura)

# Comportamento Simulado TuplaFlat
ex7 = MinhaTuplaFlat([[1, 2, 3, 4, 5], [6, 7, 8, 9]])
print(ex7)  # Sua TuplaFlat (1, 2, 3, 4, 5, 6, 7, 8, 9)

# %%
# Exemplos alternativos reais e prático sem Sum()
'''
# 1. List comprehension
[item for sublist in [[1,2],[3,4]] for item in sublist]

# 2. Chain "conecta" múltiplas listas
from itertools import chain
listas = [[1, 2], [3, 4], [5, 6]]
resultado = list(chain(*listas))
print(resultado)  # [1, 2, 3, 4, 5, 6]
'''


# %%
class MinhaTuplaFlatChain(Sequence):
    def __init__(self, tupla_):
        self._data = tuple(chain(*tupla_))  # Flat Correto com Chain!

    def __getitem__(self, idx):
        return self._data[idx]

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return f'Sua TuplaFlatChain {self._data}'


# Comportamento TuplaFlat
# Chain "conecta" múltiplas listas
ex7 = MinhaTuplaFlatChain([[1, 2, 3, 4, 5], [6, 7, 8, 9]])
print(ex7)  # Sua TuplaFlat (1, 2, 3, 4, 5, 6, 7, 8, 9)

# %%
'''
from itertools import chain

# Flat instantâneo:
chain(*[[1,2], [3,4]])  # → [1, 2, 3, 4]

# Ou com from_iterable (mais legível):
chain.from_iterable([[1,2], [3,4]])  # → [1, 2, 3, 4]
'''


# %%
class MinhaTuplaFlatSize(Sequence):
    def __init__(self, tupla_):
        self._data = tuple(tupla_)

    def __getitem__(self, idx):
        return self._data[idx]

    def __len__(self):
        return len(tuple(sum(self._data, [])))  # somará os itens

    def __repr__(self):
        return f'Sua TuplaFlatSize {self._data}'


ex8 = MinhaTuplaFlatSize([[1, 2, 3, 4, 5], [6, 7, 8, 9]])
print(ex8)  # Sua TuplaFlatSize ([1, 2, 3, 4, 5], [6, 7, 8, 9])


print(len(ex8))  # 9 soma os itens
print(len(ex8._data))  # 2 conta as listas


# %%
# Functor = "Container que pode ser mapeado"
class MinhaTuplaFunctor(Sequence):
    def __init__(self, tuple_) -> None:
        self._data = tuple(tuple_)

    def __getitem__(self, idx):
        return self._data[idx]

    def __len__(self) -> int:
        return len(self._data)

    def __repr__(self) -> str:
        return f'Sua TuplaFunctor {self._data}'

    def fmap(self, function):
        return MinhaTuplaFunctor(function(x) for x in self._data)


ex9 = MinhaTuplaFunctor([1, 2, 3, 4, 5, 6])
print(ex9)  # Sua TuplaFunctor (1, 2, 3, 4, 5, 6)

# Padrão Map
ex10 = [1, 2, 3, 4, 5, 6]
ret1 = list(map(lambda x: x**2, ex10))
print(ret1)  # [1, 4, 9, 16, 25, 36] (lista plana)

# Simulando o map padrão, com function fmap
ret2 = ex9.fmap(lambda x: x**2)
print(ret2)  # Sua TuplaFunctor (1, 4, 9, 16, 25, 36) (mantém o container)

# Extra: Pipeline funcional estilo Haskell:
ret3 = ex9.fmap(lambda x: x * 2).fmap(lambda x: x + 1)
print(ret3)  # Sua TuplaFunctor (3, 5, 7, 9, 11, 13)
