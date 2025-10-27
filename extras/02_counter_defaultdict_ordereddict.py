'''
Collections Avançadas - Counter, defaultdict e OrderedDict
Material Extra - Estudos Complementares
'''

from collections import Counter, defaultdict, OrderedDict

print('=== COUNTER, DEFAULTDICT E ORDEREDDICT ===\n')

from collections import Counter, defaultdict

# Counter
print('1. COUNTER - Contagem eficiente')
texto = 'python é uma linguagem poderosa e python é divertida'
palavras = texto.split()

contador: Counter[str] = Counter(palavras)
print(f'Contagem de palavras: {contador}')

# Métodos mais comuns
print(f'Python aparece {contador['python']} vezes')
print(f'3 mais comuns: {contador.most_common(3)}')

# Operações matemáticas
contador2: Counter[str] = Counter(['python', 'java', 'python'])
print(f'Soma: {contador + contador2}')
print(f'Subtração: {contador - contador2}')

# Exemplo prático: Análise de vendas
vendas = ['apple', 'samsung', 'apple', 'xiaomi', 'samsung', 'apple']
contador_vendas = Counter(vendas)
print(f'Produto mais vendido: {contador_vendas.most_common(1)}')

# defaultdict
print('\n2. DEFAULTDICT - Dicionário com valor padrão')

# Lista como factory
grupos = defaultdict(list)
grupos['frutas'].append('maçã')
grupos['frutas'].append('banana')
grupos['verduras'].append('alface')

print(f'Grupos: {dict(grupos)}')

# Int como factory (útil para contagens)
contador_letras = defaultdict(int)  # VARIÁVEL DIFERENTE
for letra in 'abracadabra':
    contador_letras[letra] += 1

print(f'Contagem letras: {dict(contador_letras)}')

# Lambda como factory
config = defaultdict(lambda: 'valor_padrao')
config['host'] = 'localhost'
print(f'Host: {config['host']}')
print(f'Porta (padrão): {config['porta']}')  # Usa o lambda

# Exemplo prático: Agrupamento
pessoas = [
    ('João', 'Engenharia'),
    ('Maria', 'Medicina'),
    ('Pedro', 'Engenharia'),
    ('Ana', 'Direito'),
]

departamentos = defaultdict(list)
for nome, depto in pessoas:
    departamentos[depto].append(nome)

print(f'Agrupamento: {dict(departamentos)}')

# OrderedDict
print('\n3. ORDEREDDICT - Controle total sobre ordem')

dicionario_ordenado = OrderedDict()
dicionario_ordenado['z'] = 1
dicionario_ordenado['a'] = 2
dicionario_ordenado['m'] = 3

print(f'OrderedDict: {dicionario_ordenado}')

# Reordenando
dicionario_ordenado.move_to_end('z')  # Move para o final
dicionario_ordenado.move_to_end('a', last=False)  # Move para o início

print(f'Reordenado: {dicionario_ordenado}')

# Útil para LRU Cache
cache = OrderedDict()


def acessar_cache(chave):
    if chave in cache:
        cache.move_to_end(chave)  # Marca como recentemente usado
        return cache[chave]
    # Simula cache miss
    cache[chave] = f'valor_{chave}'
    if len(cache) > 3:  # Limite do cache
        cache.popitem(last=False)  # Remove o menos recente
    return cache[chave]


# Teste do cache
print('Testando cache LRU:')
for i in [1, 2, 1, 3, 4, 2, 5]:
    print(f'Acessando {i}: {acessar_cache(i)}, Cache: {list(cache.keys())}')
