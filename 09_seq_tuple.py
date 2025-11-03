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
