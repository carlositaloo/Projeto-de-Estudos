#include <stdio.h>
#include <locale.h>

int main()
{
    setlocale(LC_ALL, "portuguese");

    float salario, soma;
#define ajuste 1.075

    printf("------------------------------------------\n");
    printf("| \t   Empresa: Prustinik \t\t |\n");
    printf("| \t   RA:      21148217-5 \t\t |\n");
    printf("| \t   Nome:    Carlos ùtalo  \t |\n");
    printf("------------------------------------------\n");

    printf("Insira o valor do seu salario liquido:\nR$");
    scanf("%f", &salario);
    soma = ajuste * salario;

    if (soma < 1750)
    {
        soma = soma + 150;
    }

    printf("Seu salario atual ù:R$%0.2f\n", salario);
    printf("Seu salario ja com o reajuste ù:R$%0.2f\n", soma);

    return 0;
}