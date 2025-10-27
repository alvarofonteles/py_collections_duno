'''
Collections Avançadas - Deque e Namedtuple
Material Extra - Estudos Complementares
'''

from collections import deque, namedtuple

print('=== DEQUE E NAMEDTUPLE ===\n')

# Deque (Double-Ended Queue)
print('1. DEQUE - Filas de duas extremidades')
fila = deque(['a', 'b', 'c'])

# Operações eficientes nas duas pontas
fila.append('d')  # Adiciona no final → ['a', 'b', 'c', 'd']
fila.appendleft('z')  # Adiciona no início → ['z', 'a', 'b', 'c', 'd']
ultimo = fila.pop()  # Remove do final → 'd'
primeiro = fila.popleft()  # Remove do início → 'z'

print(f'Deque: {fila}')
print(f'Tamanho: {len(fila)}')

# Rotação (útil para problemas circulares)
fila.rotate(1)  # Rotaciona para direita → ['c', 'a', 'b']
fila.rotate(-1)  # Rotaciona para esquerda → ['a', 'b', 'c']

# Exemplo prático: Histórico de navegação
historico = deque(maxlen=3)  # Tamanho máximo
historico.extend(['página1', 'página2', 'página3'])
historico.append('página4')  # Remove automaticamente o mais antigo
print(f'Histórico: {historico}')  # ['página2', 'página3', 'página4']

# Namedtuple
print('\n2. NAMEDTUPLE - Tuplas com campos nomeados')

# Cria uma classe simples com campos nomeados
Ponto = namedtuple('Ponto', ['x', 'y'])
Cor = namedtuple('Cor', 'red green blue')  # Também aceita string

# Uso muito mais legível
p1 = Ponto(10, 20)
p2 = Ponto(x=5, y=15)

print(f'Ponto 1: ({p1.x}, {p1.y})')
print(f'Ponto 2: {p2}')

# Acesso por índice ainda funciona
print(f'P1 X: {p1[0]}, Y: {p1[1]}')

# Métodos úteis
print(f'Campos: {Ponto._fields}')
print(f'Como dicionário: {p1._asdict()}')
print(f'Substituição: {p1._replace(x=100)}')

# Exemplo prático: Sistema de coordenadas
Coordenada = namedtuple('Coordenada', 'latitude longitude altitude')
casa = Coordenada(-23.5505, -46.6333, 760)
print(f'Localização: Lat {casa.latitude}, Long {casa.longitude}')
