a = str(input('Digite uma frase: '))
a1 = ((a.split())[0:])
a2 = (''.join(a1))
if a2 == (a2[::-1]):
    print('{} é um palindromo!'.format(a))
else:
    print('( {} )não é a mesma coisa ao contrario ( {} ) então não é um palindromo.'.format(a2, (a2[::-1])))