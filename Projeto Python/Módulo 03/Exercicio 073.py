from os import system

system('cls')

times = ('Corinthians', 'Palmeras', 'Atlético', 'Coritiba', 'América', 'São Paulo', 'Athletico', 'Flomengo', 'Santos', 'Botafogo', 'Fluminence', 'Avaí', 'Internacional', 'Bragantino', 'Ceará', 'Juventude', 'Goiás', 'Cuiba', 'Atlético', 'Fortaleza')

# print(f'Primeiros 5 colocados: \n{time[0:5]}')
print('Primeiros 5 colocados:')
for c in times[0:5]:
    print(c, end=', ')

print('\n\nÚltimos 4 colocados')
for c in range(3, -1, -1):
    print(times[c], end=', ')

print(f'\n\nA tabela em ordem alfabetica: \n {sorted(times)}')

print(f'\nA posição do flamengo é: {times[7]}\n\n')