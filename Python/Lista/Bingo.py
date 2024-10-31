# 1. Um Bingo
# Escrever a classe Bingo, utilizada para realizar um jogo de bingo, de acordo com o diagrama UML apresentado.
# • Os atributos numBolas e bolas representam o número de bolas do bingo e as bolas de uma partida;
# • O método construtor inicia uma partida, definindo o número de bolas do jogo;
# • O método Próximo sorteia uma bola, retornando o seu número (deve ser um valor entre um e o número de bolas
# ou menos um, caso todas as bolas já tenham sido sorteadas);
# • O método Sorteados retorna uma lista com todas as bolas já sorteadas;
# • Insira outros atributos e métodos nas classes, caso necessário.
import random

class Bingo:
    def __init__(self,numBolas):
        self.__numBolas = 0
        self.__bolas = []
        
        self.set_numBolas(numBolas)
    
    def set_numBolas(self, v):
        if v > 0:
            self.__numBolas = v
        else:
            raise ValueError("O número de bolas não pode ser menor ou igual a 0!")
    
    def proximo(self):
        if len(self.__bolas) == self.__numBolas:
            return -1
        else:
            sorteado = random.randint(1,self.__numBolas)
            if (len(self.__bolas) == 0):
                self.__bolas.append(sorteado)
            else:
                if sorteado not in self.__bolas:
                    self.__bolas.append(sorteado)
                else:
                    while sorteado in self.__bolas:
                        sorteado = random.randint(1,self.__numBolas)
                    self.__bolas.append(sorteado)
                    
            return sorteado
    
    def get_lista_Sorteada(self):
        return self.__bolas.sort()



a = Bingo(10)
c = 0
while c != 10:
    print(f"{a.proximo()} ", end=" ")
    c += 1