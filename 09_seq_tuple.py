'''Trabalhando com Sequence()'''

# %%
from collections.abc import Sequence


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
