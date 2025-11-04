'''Trabalhando com minhaABC/Factor'''

# %%
from minhaABC import Factor


class MinhaFunctor(Factor):
    def __init__(self, list_):
        self._data = list_

    def __getitem__(self, idx):
        return self._data[idx]

    def __len__(self):
        return len(self._data)

    def fmap(self, function):
        return [function(x) for x in self._data]

    def __repr__(self):
        return f'Sua MinhaFunctor {self._data}'


ex1 = MinhaFunctor([1, 2, 3, 4, 5])
print(ex1)

ret1 = ex1.fmap(lambda x: x**2)
print(ret1)
