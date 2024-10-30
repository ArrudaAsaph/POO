import math

class Retangulo:
    def __init__(self,base, altura):
        self.__altura = 0
        self.__base   = 0

        self.set_base(base)
        self.set_altura(altura)

    def set_altura(self, v):
        if (v > 0):
            self.__altura = v
        else:
            raise ValueError()

    def set_base(self,v):
        if (v > 0):
            self.__base = v
        else:
            raise ValueError()

    def get_altura(self):
        return self.__altura

    def get_base(self):
        return self.__base

    def calc_Area(self):
        area = self.__altura * self.__base
        return f"A área do retângulo é igual a {area} m²."

    def calc_Diagonal(self):
        diagonal = math.sqrt(self.__altura ** 2 + self.__base ** 2)
        return f"A diagonal do retângulo é igual a {diagonal:.2f} metros."



b = float(input("Informe o valor da base do retângulo: "))
h = float(input("Inform o valor da altura do retângulo: "))
x = Retangulo(b,h)
print(x.calc_Area())
print(x.calc_Diagonal())

