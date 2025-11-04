'''
Trabalhando com MutableSequence()

ANTES DE COMEÇAR - CONCEITOS BÁSICOS:

1. MUTABILIDADE:
   - IMUTÁVEL: Não pode ser alterado após criação (tuple, str)
   - MUTÁVEL: Pode ser alterado após criação (list, dict, set)

2. ABCs (Abstract Base Classes):
   - Sequence: Interface para sequências IMUTÁVEIS
   - MutableSequence: Interface para sequências MUTÁVEIS

3. MÉTODOS OBRIGATÓRIOS:
   Sequence: __getitem__, __len__
   MutableSequence: __getitem__, __len__, __setitem__, __delitem__, insert

MutableSequence vs Sequence

Sequence (IMUTÁVEL - Tuple) - Só leitura:
- __getitem__ - acessar elementos
- __len__ - obter tamanho

MutableSequence (MUTÁVEL - List) - Leitura + Escrita:
[OBRIGATÓRIOS]
- __getitem__ - acessar elementos
- __len__ - obter tamanho
- __setitem__ - modificar elementos
- __delitem__ - deletar elementos
- insert - inserir em posição específica

[IMPLEMENTADOS AUTOMATICAMENTE]
- append - via insert(len(self), value)
- pop - via __getitem__ + __delitem__
- clear - via __delitem__ repetido
- extend - via append repetido

[OPCIONAIS - SOBRESCREVER PARA PERFORMANCE]
- append - otimizar se sua estrutura tiver append nativo
- clear - otimizar se tiver clear nativo
'''

# %%
# Contúdo Extra inicial ( Overview )
#
from collections.abc import MutableSequence


class ListMutSeq(MutableSequence):
    def __init__(self, lista_):
        self._data = list(lista_)

    def __getitem__(self, idx):
        return self._data[idx]

    def __len__(self):
        return len(self._data)

    def __setitem__(self, idx, val):
        self._data[idx] = val

    def __delitem__(self, idx):
        del self._data[idx]

    def insert(self, index, val):
        self._data.insert(index, val)

    # OPCIONAL: Otimizações de performance
    def append(self, val):
        self._data.append(val)

    def clear(self):
        self._data.clear()

    def __repr__(self):
        return f'ListMutSeq({self._data})'


# Criando
lista = ListMutSeq([1, 2, 3])
print(lista)  # ListMutSeq([1, 2, 3])

# Acesso
print(lista[0])  # 1
print(len(lista))  # 3

# Modificação
lista[1] = 99
print(lista)  # ListMutSeq([1, 99, 3])

# Inserção
lista.insert(1, 50)
print(lista)  # ListMutSeq([1, 50, 99, 3])

# Append (automático)
lista.append(100)
print(lista)  # ListMutSeq([1, 50, 99, 3, 100])

# Deleção
del lista[2]
print(lista)  # ListMutSeq([1, 50, 3, 100])

# Pop (automático)
valor = lista.pop()
print(valor)  # 100
print(lista)  # ListMutSeq([1, 50, 3])

# Clear (automático)
lista.clear()
print(lista)  # ListMutSeq([])


# %%

# Exemplos práticos com lista normal
lista2 = [1, 2, 3, 4, 5, 6]

lista2.insert(2, 5)  # Insere 5 na posição 2
print(lista2)  # [1, 2, 5, 3, 4, 5, 6]

lista2.pop(-1)  # Remove último elemento
print(lista2)  # [1, 2, 5, 3, 4, 5]

lista2.append(8)  # Adiciona no final
print(lista2)  # [1, 2, 5, 3, 4, 5, 8]

lista2.clear()  # Limpa toda lista
print(lista2)  # []


# %%
# Vamos Começar a brincadeira?
#


class MinhaLista(MutableSequence):
    def __init__(self, lista_):
        self._data = list(lista_)

    def __getitem__(self, idx):
        return self._data[idx]

    def __len__(self):
        return len(self._data)

    def __setitem__(self, idx, val):
        self._data[idx] = val

    def __delitem__(self, idx):
        del self._data[idx]  # Estilo statement

    def insert(self, idx, val):
        self._data.insert(idx, val)

    def __repr__(self):
        return f'Sua MinhaLista {self._data}'


ex1 = MinhaLista([1, 2, 3, 4, 5])
print(ex1)  # Sua MinhaLista [1, 2, 3, 4, 5]

ex1.insert(2, 8)
print(ex1)  # Sua MinhaLista [1, 2, 8, 3, 4, 5]

ex1[2] = 6
print(ex1)  # Sua MinhaLista [1, 2, 6, 3, 4, 5]

ret1 = ex1.pop(2)  # Remove e RETORNA o valor (6)
print(ret1)  # 6
print(ex1)  # Sua MinhaLista [1, 2, 3, 4, 5]

# del(ex1[2]) # Estilo função
del ex1[2]  # Remove SEM retornar (Estilo statement)
print(ex1)  # Sua MinhaLista [1, 2, 4, 5]
