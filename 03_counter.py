'''Trabalhando com Counter()'''

# %%
from collections import Counter

# em textos
txt = 'Senhor, muito obrigado, por cada dia que estou Contigo, Pai tudo é teu, e no Seu tempo, as coisa irão vir até a mim.'

print(txt.count('b'))  # 1
print(txt.count('a'))  # 9

conta_tudo = Counter(txt)
print(
    conta_tudo
)  # Counter({' ': 23, 'o': 13, 'i': 9, 'a': 9, 'e': 7, 't': 7, 'u': 6, 'r': 5, ',': 5, 'm': 4, 'd': 4, 'n': 3, 's': 3, 'S': 2, 'g': 2, 'p': 2, 'c': 2, 'é': 2, 'h': 1, 'b': 1, 'q': 1, 'C': 1, 'P': 1, 'ã': 1, 'v': 1, '.': 1})


# em listas
lista = [1, 2, 3, 5, 5, 69, 4, 25, 5, 21, 2, 994, 4, 57, 5]
print(lista.count(5))  # 4

conta_lista = Counter(lista)
print(
    conta_lista
)  # Counter({5: 4, 2: 2, 4: 2, 1: 1, 3: 1, 69: 1, 25: 1, 21: 1, 994: 1, 57: 1})

# %%
tabacaria = 'Álvaro de Campos\nTABACARIA\n\nNão sou nada.\nNunca serei nada.\nNão posso querer ser nada.\nÀ parte isso, tenho em mim todos os sonhos do mundo.\n\nJanelas do meu quarto,\nDo meu quarto de um dos milhões do mundo que ninguém sabe quem é\n\n(E se soubessem quem é, o que saberiam?),\nDais para o mistério de uma rua cruzada constantemente por gente,\n\nPara uma rua inacessível a todos os pensamentos,\nReal, impossivelmente real, certa, desconhecidamente certa,\n\nCom o mistério das coisas por baixo das pedras e dos seres,\n\nCom a morte a pôr humidade nas paredes e cabelos brancos nos homens,\n\nCom o Destino a conduzir a carroça de tudo pela estrada de nada.\n\n...'

tab_total = Counter(tabacaria)
# Counter por letras e caracteres
print(
    tab_total
)  # Counter({' ': 100, 'e': 60, 'a': 58, 'o': 54, 's': 50, 'r': 31, 'd': 30, 'm': 30, 'n': 28, 'u': 24, '\n': 23, 't': 21, 'i': 20, 'c': 13, 'p': 12, ',': 12, 'l': 9, '.': 8, 'q': 7, 'h': 6, 'b': 6, 'C': 5, 'é': 5, 'A': 4, 'v': 3, 'N': 3, 'D': 3, 'R': 2, 'ã': 2, 'g': 2, 'z': 2, 'Á': 1, 'T': 1, 'B': 1, 'I': 1, 'À': 1, 'J': 1, 'õ': 1, '(': 1, 'E': 1, '?': 1, ')': 1, 'P': 1, 'í': 1, 'x': 1, 'ô': 1, 'ç': 1})

# separado por palavras
print(
    tabacaria.split()
)  # ['Álvaro', 'de', 'Campos', 'TABACARIA', 'Não', 'sou', 'nada.', 'Nunca', 'serei', 'nada.', 'Não', 'posso', 'querer', 'ser', 'nada.', 'À', 'parte', 'isso,', 'tenho', 'em', 'mim', 'todos', 'os', 'sonhos', 'do', 'mundo.', 'Janelas', 'do', 'meu', 'quarto,', 'Do', 'meu', 'quarto', 'de', 'um', 'dos', 'milhões', 'do', 'mundo', 'que', 'ninguém', 'sabe', 'quem', 'é', '(E', 'se', 'soubessem', 'quem', 'é,', 'o', 'que', 'saberiam?),', 'Dais', 'para', 'o', 'mistério', 'de', 'uma', 'rua', 'cruzada', 'constantemente', 'por', 'gente,', 'Para', 'uma', 'rua', 'inacessível', 'a', 'todos', 'os', 'pensamentos,', 'Real,', 'impossivelmente', 'real,', 'certa,', 'desconhecidamente', 'certa,', 'Com', 'o', 'mistério', 'das', 'coisas', 'por', 'baixo', 'das', 'pedras', 'e', 'dos', 'seres,', 'Com', 'a', 'morte', 'a', 'pôr', 'humidade', 'nas', 'paredes', 'e', 'cabelos', 'brancos', 'nos', 'homens,', 'Com', 'o', 'Destino', 'a', 'conduzir', 'a', 'carroça', 'de', 'tudo', 'pela', 'estrada', 'de', 'nada.', '...']

tab_palavras1 = Counter(tabacaria.split())
# Counter separado por palavras
print(
    tab_palavras1
)  # Counter({'de': 5, 'a': 5, 'nada.': 4, 'o': 4, 'do': 3, 'Com': 3, 'Não': 2, 'todos': 2, 'os': 2, 'meu': 2, 'dos': 2, 'que': 2, 'quem': 2, 'mistério': 2, 'uma': 2, 'rua': 2, 'por': 2, 'certa,': 2, 'das': 2, 'e': 2, 'Álvaro': 1, 'Campos': 1, 'TABACARIA': 1, 'sou': 1, 'Nunca': 1, 'serei': 1, 'posso': 1, 'querer': 1, 'ser': 1, 'À': 1, 'parte': 1, 'isso,': 1, 'tenho': 1, 'em': 1, 'mim': 1, 'sonhos': 1, 'mundo.': 1, 'Janelas': 1, 'quarto,': 1, 'Do': 1, 'quarto': 1, 'um': 1, 'milhões': 1, 'mundo': 1, 'ninguém': 1, 'sabe': 1, 'é': 1, '(E': 1, 'se': 1, 'soubessem': 1, 'é,': 1, 'saberiam?),': 1, 'Dais': 1, 'para': 1, 'cruzada': 1, 'constantemente': 1, 'gente,': 1, 'Para': 1, 'inacessível': 1, 'pensamentos,': 1, 'Real,': 1, 'impossivelmente': 1, 'real,': 1, 'desconhecidamente': 1, 'coisas': 1, 'baixo': 1, 'pedras': 1, 'seres,': 1, 'morte': 1, 'pôr': 1, 'humidade': 1, 'nas': 1, 'paredes': 1, 'cabelos': 1, 'brancos': 1, 'nos': 1, 'homens,': 1, 'Destino': 1, 'conduzir': 1, 'carroça': 1, 'tudo': 1, 'pela': 1, 'estrada': 1, '...': 1})

tab_palavras1 = Counter(tabacaria.split())
# Counter de todas as palavras mais comuns
print(
    tab_palavras1.most_common()
)  # [('de', 5), ('a', 5), ('nada.', 4), ('o', 4), ('do', 3), ('Com', 3), ('Não', 2), ('todos', 2), ('os', 2), ('meu', 2), ('dos', 2), ('que', 2), ('quem', 2), ('mistério', 2), ('uma', 2), ('rua', 2), ('por', 2), ('certa,', 2), ('das', 2), ('e', 2), ('Álvaro', 1), ('Campos', 1), ('TABACARIA', 1), ('sou', 1), ('Nunca', 1), ('serei', 1), ('posso', 1), ('querer', 1), ('ser', 1), ('À', 1), ('parte', 1), ('isso,', 1), ('tenho', 1), ('em', 1), ('mim', 1), ('sonhos', 1), ('mundo.', 1), ('Janelas', 1), ('quarto,', 1), ('Do', 1), ('quarto', 1), ('um', 1), ('milhões', 1), ('mundo', 1), ('ninguém', 1), ('sabe', 1), ('é', 1), ('(E', 1), ('se', 1), ('soubessem', 1), ('é,', 1), ('saberiam?),', 1), ('Dais', 1), ('para', 1), ('cruzada', 1), ('constantemente', 1), ('gente,', 1), ('Para', 1), ('inacessível', 1), ('pensamentos,', 1), ('Real,', 1), ('impossivelmente', 1), ('real,', 1), ('desconhecidamente', 1), ('coisas', 1), ('baixo', 1), ('pedras', 1), ('seres,', 1), ('morte', 1), ('pôr', 1), ('humidade', 1), ('nas', 1), ('paredes', 1), ('cabelos', 1), ('brancos', 1), ('nos', 1), ('homens,', 1), ('Destino', 1), ('conduzir', 1), ('carroça', 1), ('tudo', 1), ('pela', 1), ('estrada', 1), ('...', 1)]

# Counter das 10 palavras mais comuns
print(
    tab_palavras1.most_common(10)
)  # [('de', 5), ('a', 5), ('nada.', 4), ('o', 4), ('do', 3), ('Com', 3), ('Não', 2), ('todos', 2), ('os', 2), ('meu', 2)]

# Todo o Texto
# print(tabacaria)

# %%
'''
Álvaro de Campos
TABACARIA

Não sou nada.
Nunca serei nada.
Não posso querer ser nada.
À parte isso, tenho em mim todos os sonhos do mundo.

Janelas do meu quarto,
Do meu quarto de um dos milhões do mundo que ninguém sabe quem é

(E se soubessem quem é, o que saberiam?),
Dais para o mistério de uma rua cruzada constantemente por gente,

Para uma rua inacessível a todos os pensamentos,
Real, impossivelmente real, certa, desconhecidamente certa,

Com o mistério das coisas por baixo das pedras e dos seres,

Com a morte a pôr humidade nas paredes e cabelos brancos nos homens,

Com o Destino a conduzir a carroça de tudo pela estrada de nada.

...
'''
