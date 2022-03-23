
#include <iostream>

using namespace std;

int main()
{
	string name;
	string frase = "sim";
	int res1, n1, n2, res2;

	cout << " Bem vindo Viadinho!\n Voce e uma puta foda!\n";
	cout << " Digite seu nome para nos conhecermos melhor: \n";
	cin >> name;
	fflush(stdin);
	cout << "\n Ola, " << name << ".\n";
	cout << " Esta tudo bem contigo ?\n Digite sim ou nao:\n";
	cin >> frase;

	if (frase == "sim")
	{
		cout << " Ok, " << name << " vomos proceguir.\n\n";

		cout << " Quanto e 4+9? \n";
		cin >> res1;

		if (res1 == 13)
		{
			cout << " Parabens voce e mais esperto do que imaginava.\n";

			cout << "\n Digite 2 numeros que der = ou acima de 60:\n";
			cin >> n1;
			cin >> n2;
			res2 = n1 + n2;
			if (res2 >= 60)
			{
				cout << " Parabens vc e viado inteligente!\n";
			}
			else
			{
				cout << " Voce e burro d+, tente da proxima fracacado!\n";
			}
		}
		else
		{
			cout << " Voce e burro d+, tente da proxima fracacado!\n\n";
		}
	}
	else if (frase == "nao")
	{
		cout << " Ok, Pau no seu cu " << name << ".\n\n";
	}
	else
	{
		cout << " \nVoce esta cheio de gracinha ne! Viadinho!!!\n\n";
	}

	system("pause");
	return 0;
}
