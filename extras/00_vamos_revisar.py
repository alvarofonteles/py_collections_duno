'''
Coleções Python - Vamos Revisar!
Material Extra - Estudos Complementares
'''

print('=== COLECÕES BÁSICAS DO PYTHON ===\n')

# 1. Listas (Lists)
print('1. LISTAS - Mutáveis e ordenadas')
frutas = ['maçã', 'banana', 'laranja']
numeros = [1, 2, 3, 4, 5]

# Operações com listas
frutas.append('uva')  # Adiciona no final
frutas.insert(1, 'manga')  # Insere na posição
frutas.remove('banana')  # Remove elemento
ultimo = frutas.pop()  # Remove e retorna o último

print(f'Lista de frutas: {frutas}')
print(f'Primeira fruta: {frutas[0]}')
print(f'Última fruta: {frutas[-1]}')

# 2. Tuplas (Tuples)
print('\n2. TUPLAS - Imutáveis e ordenadas')
coordenadas = (10, 20)
cores_rgb = ('vermelho', 'verde', 'azul')

# Acesso similar às listas
print(f'Coordenada X: {coordenadas[0]}')
print(f'Coordenada Y: {coordenadas[1]}')

# Desempacotamento
x, y = coordenadas
print(f'X: {x}, Y: {y}')

# 3. Conjuntos (Sets)
print('\n3. CONJUNTOS - Não ordenados e sem duplicados')
numeros_set = {1, 2, 3, 4, 5}
vogais = set(['a', 'e', 'i', 'o', 'u'])

# Operações com conjuntos
numeros_set.add(6)  # Adiciona elemento
numeros_set.remove(3)  # Remove elemento
uniao = numeros_set | {7, 8}  # União
intersecao = numeros_set & {4, 5, 9}  # Interseção

print(f'Conjunto números: {numeros_set}')
print(f'União: {uniao}')
print(f'Interseção: {intersecao}')

# 4. Dicionários (Dictionaries)
print('\n4. DICIONÁRIOS - Pares chave-valor')
pessoa = {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}

# Operações com dicionários
pessoa['profissao'] = 'Engenheiro'  # Adiciona chave
idade = pessoa.get('idade')  # Acesso seguro
chaves = pessoa.keys()  # Lista de chaves
valores = pessoa.values()  # Lista de valores

print(f'Dicionário: {pessoa}')
print(f'Nome: {pessoa['nome']}')
print(f'Chaves: {list(chaves)}')

# 5. Operações Comuns
print('\n5. OPERAÇÕES COMUNS')

# Compreensão de listas
quadrados = [x**2 for x in range(1, 6)]
print(f'Quadrados: {quadrados}')

# Compreensão de dicionários
quadrados_dict = {x: x**2 for x in range(1, 6)}
print(f'Quadrados dict: {quadrados_dict}')

# Iteração
print('Iteração com enumerate:')
for indice, fruta in enumerate(frutas):
    print(f'  Índice {indice}: {fruta}')

# Ordenação
numeros_desordenados = [3, 1, 4, 1, 5, 9, 2]
numeros_ordenados = sorted(numeros_desordenados)
print(f'Ordenados: {numeros_ordenados}')

# 6. Exemplo Prático
print('\n6. EXEMPLO PRÁTICO - Sistema de Estoque')

# Sistema simples de estoque
estoque = {'maçã': 50, 'banana': 30, 'laranja': 20}


def adicionar_produto(produto, quantidade):
    estoque[produto] = estoque.get(produto, 0) + quantidade
    print(f'✅ Adicionado {quantidade} {produto}(s)')


def vender_produto(produto, quantidade):
    if produto in estoque and estoque[produto] >= quantidade:
        estoque[produto] -= quantidade
        print(f'✅ Vendido {quantidade} {produto}(s)')
        return True
    print(f'❌ Estoque insuficiente de {produto}')
    return False


# Testando
adicionar_produto('uva', 25)
vender_produto('maçã', 10)

print('\nEstoque atual:')
for produto, quantidade in estoque.items():
    print(f'  {produto}: {quantidade} unidades')

print('\n🎯 Revisão concluída!')
