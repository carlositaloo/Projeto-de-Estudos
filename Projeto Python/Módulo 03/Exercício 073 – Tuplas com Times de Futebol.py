# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

from os import system

system('cls')

times = ('Corinthians', 'Palmeiras', 'Atlético', 'Coritiba', 'América', 'São Paulo', 'Club Athletico', 'Flamengo', 'Santos', 'Botafogo', 'Fluminense', 'Avaí', 'Internacional', 'Bragantino', 'Ceará', 'Juventude', 'Goiás', 'Cuiba', 'Atlético', 'Fortaleza')

print('\n')
print('-=' * 28)
print('Tabela de times:\n')
for c in times:
    print(c, end=', ')

print('\n')
print('-=' * 28)
# print(f'Primeiros 5 colocados: \n{time[0:5]}')
print('Primeiros 5 colocados:\n')
for c in times[0:5]:
    print(c, end=', ')

print('\n')
print('-=' * 28)
print('Primeiros 5 colocados de trás pra frente:\n')
for c in range(4, -1, -1):
    print(times[c], end=', ')

print('\n')
print('-=' * 28)
print('Os últimos 4 colocados:\n')
for c in times[-4:]:
    print(c, end=', ')

print('\n')
print('-=' * 28)
# print(f'\nA tabela em ordem alfabética: \n {sorted(times)}')
print('Tabela de times:\n')
for c in sorted(times):
    print(c, end=', ')

print('\n')
print('-=' * 28)
print(f'A posição do Flamengo é:\n\nÉ a {times.index("Flamengo")}ª posição')
print('')
print('-=' * 28)
