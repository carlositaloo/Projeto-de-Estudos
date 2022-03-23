from os import system
from random import sample
from rich import print


def clear():
    system('cls')


clear()
m = sample(range(1, 61), k=6)

print(
    f"\n\n{'Numeros da Sorte Mega-Sena!':^59}\n\n"
    f"		  {m}\n\n"
    f"{'09 de março 2022':^59}\n\n\n"
)
