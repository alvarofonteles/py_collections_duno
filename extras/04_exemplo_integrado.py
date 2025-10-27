'''
Exemplo Integrado - Todas as Collections Juntas
Material Extra - Estudos Complementares
'''

from collections import deque, namedtuple, Counter, defaultdict, ChainMap

print('=== EXEMPLO INTEGRADO - SISTEMA DE EVENTOS ===\n')

# Sistema de monitoramento de eventos
Evento = namedtuple('Evento', 'tipo usuario timestamp')

# Buffer circular de eventos recentes
eventos_recentes = deque(maxlen=5)

# Contadores por tipo de evento
contador_eventos = Counter()

# Agrupamento de eventos por usuário
eventos_por_usuario = defaultdict(list)

# Configurações em camadas
config_base = {'limite_eventos': 10000, 'retencao_dias': 30}
config_ambiente = {'limite_eventos': 5000}

config = ChainMap(config_ambiente, config_base)


def registrar_evento(tipo, usuario):
    evento = Evento(tipo, usuario, '2024-01-01 10:00:00')

    # Adiciona ao buffer
    eventos_recentes.append(evento)

    # Atualiza contadores
    contador_eventos[tipo] += 1

    # Agrupa por usuário
    eventos_por_usuario[usuario].append(evento)

    print(f'Evento registrado: {evento}')
    print(f'Eventos recentes: {len(eventos_recentes)}')
    print(f'Top eventos: {contador_eventos.most_common(3)}')
    print(f'Limite configurado: {config['limite_eventos']}')
    print('-' * 40)


# Teste
print('Registrando eventos:')
registrar_evento('login', 'joao')
registrar_evento('compra', 'maria')
registrar_evento('login', 'joao')
registrar_evento('logout', 'pedro')
registrar_evento('erro', 'sistema')
registrar_evento('consulta', 'ana')  # Vai remover o primeiro do buffer

print('\n📊 Resumo Final:')
print(f'Total de tipos de eventos: {len(contador_eventos)}')
print(f'Eventos por usuário: {dict(eventos_por_usuario)}')
print(f'Buffer atual: {list(eventos_recentes)}')
