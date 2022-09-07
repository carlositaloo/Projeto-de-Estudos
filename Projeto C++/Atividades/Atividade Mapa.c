#include <stdlib.h>
#include <stdio.h>
#include <locale.h>

#define max 5

//Variveis globais
int pilha[max];
int pilha2[max];
int ini = 0;
int topo = 0;
int topo2 = 0;
int y = 4;

//Prottipos das funes
void mostrar();
void empilhar();
void desempilhar();

//Programa principal
int main()
{
    setlocale(LC_ALL, "Portuguese");
    int op;
    //menu:
    do
    {
        mostrar();
        printf("\n          Menu ");
        printf("\n      1 - Empilhar");
        printf("\n      2 - Desempilhar");
        printf("\n      3 - Mostrar");
        printf("\n      0 - Exit");
        printf("\n\n    Opo: ");
        scanf("%d", &op);
        switch (op)
        {
        case 1:
            empilhar();
            break;
        case 2:
            desempilhar();
            break;
        case 3:
            mostrar();
            system("pause");
            break;
        }
    } while (op != 0);

    return 0;
    system("pause");
}

// Funes:
void empilhar()
{
    if(topo == max)
    printf("\nCheio!!");
    else
    {
        printf("\nDigite o valor da do prato: ");
        scanf("%d", &pilha[topo]);
        topo ++;
    }
}

void desempilhar()
{
    if(ini == topo)
    printf("\nCheio!!!");
    else
    {
        pilha2[topo2] = pilha[ini + y];
        y --;
        topo2 ++;
        printf("\nDesempilhado o prato: %d\n\n", pilha[topo - 1]);
        pilha[topo - 1] = 0;
        topo --;
    }
    system("pause");
}

void mostrar()
{
    system("cls");

    printf("\n\n                Cores dos Pratos\n");
    printf("1-Vermelho, 2-Verde, 3-Azul, 4-Branco, 5-Laranja\n");

    int i;
    printf("\n");
    printf("Pilha 01 - Base -> |");
    for (i = 0; i < max; i++)
    {
        printf(" %d |", pilha[i]);
    }
    printf(" <- Topo");
    int j;
    printf("\n");
    printf("Pilha 02 - Base -> |");
    for (j = 0; j < max; j++)
    {
        printf(" %d |", pilha2[j]);
    }
    printf(" <- Topo\n");
}

