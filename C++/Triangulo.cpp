#include <iostream>

using namespace std;

class Triangulo {
    public: // controla visibiliade dos membros
    double base = 0, altura = 0;

    double calculaArea(){ // criação de Methods
        return base * altura / 2;
    }
};


int main (){
    Triangulo x;

    cout << x.base << " " << x.altura << endl;
     // cout (Leitura) << valor de x.base << " " << x.altura << quebra de linha;
    cout << "Informe o valor da base: ";
    cin >> x.base; // cin (ENTRADA);
    cout << "Informe o valor da Altura: ";
    cin >> x.altura;
    cout << "Area = " << x.calculaArea() << endl;
    return 0;
}