'''
Collections Avançadas - ChainMap
Material Extra - Estudos Complementares
'''

from collections import ChainMap

print('=== CHAINMAP - Múltiplos dicionários em uma view ===\n')

# Agrupa múltiplos dicionários em uma única view
config_padrao = {'host': 'localhost', 'porta': '8080'}  # ✅ String
config_usuario = {'porta': '9000', 'debug': 'True'}  # ✅ String
config_temporaria = {'timeout': '30'}  # ✅ String

# ChainMap busca na ordem: temporaria → usuario → padrao
config = ChainMap(config_temporaria, config_usuario, config_padrao)

print(f'Host: {config['host']}')  # Busca no config_padrao
print(f'Porta: {config['porta']}')  # Busca no config_usuario (primeira ocorrência)
print(f'Debug: {config['debug']}')  # Busca no config_usuario
print(f'Timeout: {config['timeout']}')  # Busca no config_temporaria

# Atualizações afetam apenas o primeiro mapeamento
config['porta'] = '9999'  # Altera config_temporaria
print(f'Config temporária após update: {config_temporaria}')

# Adicionando novo contexto
novo_contexto = {'database': 'meudb'}
config = config.new_child(novo_contexto)
print(f'Com novo contexto: {dict(config)}')

# Exemplo prático: Sistema de configurações
config_sistema = {'log_level': 'INFO', 'max_connections': '100'}  # ✅ String
config_aplicacao = {'log_level': 'DEBUG', 'database': 'app_db'}
config_sessao = {'user': 'admin'}

settings = ChainMap(config_sessao, config_aplicacao, config_sistema)

print('\nConfigurações finais:')
for chave, valor in settings.items():
    print(f'  {chave}: {valor}')

# Listando todos os maps
print(f'\nTodos os maps: {list(settings.maps)}')
