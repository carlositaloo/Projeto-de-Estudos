# 045: Crie um programa que faça o computador jogar Jokenpô com você.

from os import system
from rich import print
from emoji import emojize
from random import randint, choice
from time import sleep
import pygame

pygame.init()
pygame.mixer.music.load('D:/Users/Carlos_Italo/Desktop/Github/Projeto-Estudos/Projeto Python/Arquivos/Music-8bit-game.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.01)

system('cls')
sair = ''


def inicio():
    print(f'[bold red]#[/bold red]' * 59)
    print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
    print(
        f"[bold red]##[bold yellow]{'JOKENPÔ':^55}[/bold yellow]##[/bold red]")
    print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
    print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
    print(emojize(
        f"[bold red]##{':fist: [bold blue]1[/bold blue] Pedra    :raised_hand: [bold blue]2[/bold blue] Papel    :v: [bold blue]3[/bold blue] Tesoura':^141}##[/bold red]"))
    print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
    print(f'[bold red]#[/bold red]' * 59)
def carregamento():
    system('cls')
    print(f'[bold red]#[/bold red]' * 59)
    print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
    print(
        f"[bold red]##[bold yellow]{'JOKENPÔ':^55}[/bold yellow]##[/bold red]")
    print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
    print(f"[bold red]##{'Carregando...':^55}##[/bold red]")
    print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
    print(f'[bold red]##[/bold red]        ♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢        [bold red]##[/bold red]')
    print(f'[bold red]#[/bold red]' * 59)
    sleep(0.3)
    system('cls')

    print(f'[bold red]#[/bold red]' * 59)
    print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
    print(
        f"[bold red]##[bold yellow]{'JOKENPÔ':^55}[/bold yellow]##[/bold red]")
    print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
    print(f"[bold red]##{'Carregando...':^55}##[/bold red]")
    print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
    print(f'[bold red]##[/bold red]        [bold yellow]♦♦♦[/bold yellow]♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢        [bold red]##[/bold red]')
    print(f'[bold red]#[/bold red]' * 59)
    sleep(0.5)
    system('cls')

    print(f'[bold red]#[/bold red]' * 59)
    print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
    print(
        f"[bold red]##[bold yellow]{'JOKENPÔ':^55}[/bold yellow]##[/bold red]")
    print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
    print(f"[bold red]##{'Carregando...':^55}##[/bold red]")
    print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
    print(f'[bold red]##[/bold red]        [bold yellow]♦♦♦♦♦♦♦[/bold yellow]♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢        [bold red]##[/bold red]')
    print(f'[bold red]#[/bold red]' * 59)
    sleep(0.1)
    system('cls')

    print(f'[bold red]#[/bold red]' * 59)
    print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
    print(
        f"[bold red]##[bold yellow]{'JOKENPÔ':^55}[/bold yellow]##[/bold red]")
    print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
    print(f"[bold red]##{'Carregando...':^55}##[/bold red]")
    print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
    print(f'[bold red]##[/bold red]        [bold yellow]♦♦♦♦♦♦♦♦♦♦♦♦[/bold yellow]♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢        [bold red]##[/bold red]')
    print(f'[bold red]#[/bold red]' * 59)
    sleep(0.7)
    system('cls')

    print(f'[bold red]#[/bold red]' * 59)
    print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
    print(
        f"[bold red]##[bold yellow]{'JOKENPÔ':^55}[/bold yellow]##[/bold red]")
    print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
    print(f"[bold red]##{'Carregando...':^55}##[/bold red]")
    print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
    print(f'[bold red]##[/bold red]        [bold yellow]♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦[/bold yellow]♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢        [bold red]##[/bold red]')
    print(f'[bold red]#[/bold red]' * 59)
    sleep(0.9)
    system('cls')

    print(f'[bold red]#[/bold red]' * 59)
    print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
    print(
        f"[bold red]##[bold yellow]{'JOKENPÔ':^55}[/bold yellow]##[/bold red]")
    print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
    print(f"[bold red]##{'Carregando...':^55}##[/bold red]")
    print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
    print(f'[bold red]##[/bold red]        [bold yellow]♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦[/bold yellow]♢♢♢♢        [bold red]##[/bold red]')
    print(f'[bold red]#[/bold red]' * 59)
    sleep(0.5)
    system('cls')

    print(f'[bold red]#[/bold red]' * 59)
    print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
    print(
        f"[bold red]##[bold yellow]{'JOKENPÔ':^55}[/bold yellow]##[/bold red]")
    print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
    print(f"[bold red]##{'Carregando...':^55}##[/bold red]")
    print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
    print(f'[bold red]##[/bold red]        [bold yellow]♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦[/bold yellow]        [bold red]##[/bold red]')
    print(f'[bold red]#[/bold red]' * 59)
    sleep(1)
    system('cls')
def resultado():
    if voce == '1':
        if maquina == 1:
            print(f'[bold red]#[/bold red]' * 59)
            print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
            print(
                f"[bold red]##[bold yellow]{'JOKENPÔ':^55}[/bold yellow]##[/bold red]")
            print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
            print(
                f"[bold red]##[bold blue]{'Você                      Maquina':^55}[/bold blue]##[/bold red]")
            print(emojize(
                f"[bold red]##[/bold red]{':fist:Pedra                     :fist:Pedra  ':^63}[bold red]##[/bold red]"))
            print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
            print(f'[bold red]#[/bold red]' * 59)
            print(f"\n[bold yellow]{'EMPATE!':^59}\n\n")

        elif maquina == 2:
            print(f'[bold red]#[/bold red]' * 59)
            print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
            print(
                f"[bold red]##[bold yellow]{'JOKENPÔ':^55}[/bold yellow]##[/bold red]")
            print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
            print(
                f"[bold red]##[bold blue]{'Você                      Maquina':^55}[/bold blue]##[/bold red]")
            print(emojize(
                f"[bold red]##[/bold red]{':fist:Pedra                     :raised_hand:Papel  ':^70}[bold red]##[/bold red]"))
            print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
            print(f'[bold red]#[/bold red]' * 59)
            print(f"\n[bold red]{'VOCÊ PERDEU!':^59}\n\n")

        elif maquina == 3:
            print(f'[bold red]#[/bold red]' * 59)
            print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
            print(
                f"[bold red]##[bold yellow]{'JOKENPÔ':^55}[/bold yellow]##[/bold red]")
            print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
            print(
                f"[bold red]##[bold blue]{'Você                      Maquina':^55}[/bold blue]##[/bold red]")
            print(emojize(
                f"[bold red]##[/bold red]{'   :fist:Pedra                    :v: Tesoura   ':^61}[bold red]##[/bold red]"))
            print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
            print(f'[bold red]#[/bold red]' * 59)
            print(f"\n[bold green]{'VOCÊ GANHOU!':^59}\n\n")
    elif voce == '2':
        if maquina == 1:
            print(f'[bold red]#[/bold red]' * 59)
            print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
            print(
                f"[bold red]##[bold yellow]{'JOKENPÔ':^55}[/bold yellow]##[/bold red]")
            print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
            print(
                f"[bold red]##[bold blue]{'Você                      Maquina':^55}[/bold blue]##[/bold red]")
            print(emojize(
                f"[bold red]##[/bold red]{':raised_hand:Papel                     :fist:Pedra  ':^70}[bold red]##[/bold red]"))
            print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
            print(f'[bold red]#[/bold red]' * 59)
            print(f"\n[bold green]{'VOCÊ GANHOU!':^59}\n\n")

        elif maquina == 2:
            print(f'[bold red]#[/bold red]' * 59)
            print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
            print(
                f"[bold red]##[bold yellow]{'JOKENPÔ':^55}[/bold yellow]##[/bold red]")
            print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
            print(
                f"[bold red]##[bold blue]{'Você                      Maquina':^55}[/bold blue]##[/bold red]")
            print(emojize(
                f"[bold red]##[/bold red]{':raised_hand:Papel                     :raised_hand:Papel  ':^77}[bold red]##[/bold red]"))
            print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
            print(f'[bold red]#[/bold red]' * 59)
            print(f"\n[bold yellow]{'EMPATE!':^59}\n\n")

        elif maquina == 3:
            print(f'[bold red]#[/bold red]' * 59)
            print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
            print(
                f"[bold red]##[bold yellow]{'JOKENPÔ':^55}[/bold yellow]##[/bold red]")
            print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
            print(
                f"[bold red]##[bold blue]{'Você                      Maquina':^55}[/bold blue]##[/bold red]")
            print(emojize(
                f"[bold red]##[/bold red]{'   :raised_hand:Papel                    :v: Tesoura   ':^68}[bold red]##[/bold red]"))
            print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
            print(f'[bold red]#[/bold red]' * 59)
            print(f"\n[bold red]{'VOCÊ PERDEU!':^59}\n\n")
    elif voce == '3':
        if maquina == 1:
            print(f'[bold red]#[/bold red]' * 59)
            print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
            print(
                f"[bold red]##[bold yellow]{'JOKENPÔ':^55}[/bold yellow]##[/bold red]")
            print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
            print(
                f"[bold red]##[bold blue]{'Você                      Maquina':^55}[/bold blue]##[/bold red]")
            print(emojize(
                f"[bold red]##[/bold red]{':v: Tesoura                    :fist:Pedra  ':^61}[bold red]##[/bold red]"))
            print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
            print(f'[bold red]#[/bold red]' * 59)
            print(f"\n[bold red]{'VOCÊ PERDEU!':^59}\n\n")

        elif maquina == 2:
            print(f'[bold red]#[/bold red]' * 59)
            print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
            print(
                f"[bold red]##[bold yellow]{'JOKENPÔ':^55}[/bold yellow]##[/bold red]")
            print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
            print(
                f"[bold red]##[bold blue]{'Você                      Maquina':^55}[/bold blue]##[/bold red]")
            print(emojize(
                f"[bold red]##[/bold red]{':v: Tesoura                   :raised_hand:Papel  ':^68}[bold red]##[/bold red]"))
            print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
            print(f'[bold red]#[/bold red]' * 59)
            print(f"\n[bold green]{'VOCÊ GANHOU!':^59}\n\n")

        elif maquina == 3:
            print(f'[bold red]#[/bold red]' * 59)
            print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
            print(
                f"[bold red]##[bold yellow]{'JOKENPÔ':^55}[/bold yellow]##[/bold red]")
            print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
            print(
                f"[bold red]##[bold blue]{'Você                      Maquina':^55}[/bold blue]##[/bold red]")
            print(emojize(
                f"[bold red]##[/bold red]{':v: Tesoura                   :v: Tesoura ':^59}[bold red]##[/bold red]"))
            print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
            print(f'[bold red]#[/bold red]' * 59)
            print(f"\n[bold yellow]{'EMPATE!':^59}\n\n")
    else:
        print(f'[bold red]#[/bold red]' * 59)
        print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
        print(
            f"[bold red]##[bold yellow]{'JOKENPÔ':^55}[/bold yellow]##[/bold red]")
        print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
        print(f"[bold red]##[bold blue]{'':^55}[/bold blue]##[/bold red]")
        print(
            emojize(f"[bold red]##[/bold red]{'ERRO!!!':^55}[bold red]##[/bold red]"))
        print(f'[bold red]##[/bold red]', ' ' * 53, '[bold red]##[/bold red]')
        print(f'[bold red]#[/bold red]' * 59)

while sair == '':
    inicio()
    voce = str(input(f"{'Opção: ':>33}"))
    if voce == '0' or voce == '':
        voce = choice(['1', '2', '3'])
        

    carregamento()
    maquina = randint(1, 3)

    resultado()
    sair = input(f"{'Pressione Enter para jogar novamente: ':>48}")
    system('cls')
