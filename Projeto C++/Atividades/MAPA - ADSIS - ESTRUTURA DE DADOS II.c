#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <locale.h>

//Tipo n
typedef struct NO {
	int dado;
	struct NO *esq;
	struct NO *dir;
	struct NO *pai;
} NO;

//Tipo rvore
typedef struct ARVORE{
	NO *raiz;
}ARVORE;

//Declarao da rvore
ARVORE a;

//Prottipos das funes
void inicialRaiz(ARVORE arv);
void inicializaNo(NO* n, int val);
void insereNo(int valor);
void preOrdem(NO* raiz);

//Funo que sempre deve ser chamada ao se criar uma nova rvore
void inicialRaiz(ARVORE arv)
{
	arv.raiz = NULL;
}

//Funo utilizada para inicializar um novo n na rvore
void inicializaNo(NO* n, int val){
	if(!n)
	{
		printf("Falha de alocacao.\n");
		return;
	}
	n->pai = NULL;
	n->esq = NULL;
	n->dir = NULL;
	n->dado = val;
}

//Funo que realiza a insero de maneira ordenada
void insereNo(int valor)
{
	NO* corrente = a.raiz;
	NO* pai;

	NO* novoNo = (NO*) malloc(sizeof(NO));
	inicializaNo(novoNo, valor);
	printf("Inserindo nmero: %d ", novoNo->dado);
	
	if(corrente == NULL)
	{
		a.raiz = novoNo;
		printf("na \033[1;33mRAIZ. \033[0m\n");
		return;
	}
	
	while(corrente){
		pai = corrente;
		if(novoNo->dado < corrente->dado){
			corrente = corrente->esq;
			if(!corrente){
				printf("no N  \033[1;31mESQUERDA\033[0m do N\033[1;35m %d. \033[0m\n", pai->dado);
				pai->esq = novoNo;
				return;
			}
		}
		else{
			corrente = corrente->dir;
			if(!corrente){
				printf("no N  \033[1;32mDIREITA\033[0m do N\033[1;35m %d. \033[0m\n", pai->dado);
				pai->dir = novoNo;
				return;
			}
		}
	}
}

//Executa o caminhamento pr-ordem a partir do n indicado por "raiz"
void preOrdem(NO* raiz){
	if(raiz){
		printf("%d \t", raiz->dado);
		preOrdem(raiz->esq);
		preOrdem(raiz->dir);
	}
}

int main(){
	setlocale(LC_ALL, "Portuguese");
	system("cls");

	int num = NULL;
	printf("Informe seu RA: (9 digitos um de cada vez)");

	for (int i = 0; i < 9; i++)
	{
		printf("\nDigite o nmero sequente: ");
		scanf("%d", &num);
		insereNo(num);
	}
    
        
	printf("\nBusca pr ordem: \033[1;35m\n");
	preOrdem(a.raiz);
	printf("\n\n \033[1;31m\n");
}