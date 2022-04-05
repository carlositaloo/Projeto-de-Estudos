f1 = 0
f2 = 1
f3 = f1 + f2
c = 0
num = int(input("Digite a quantidade de termos da sequência de fibonacci vc quer ver: "))
while c < num:
    print(f1)
    f1 = f2
    f2 = f3
    f3 = f1 + f2
    c += 1