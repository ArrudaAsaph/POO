import math
class EquacaoII:
    def __init__(self,a,b,c):
        self.__a = 0
        self.__b = 0
        self.__c = 0

        self.set_A(a)
        self.set_B(b)
        self.set_C(c)

    def set_A(self,a):
        if a != 0: self.__a = a
        else: raise ValueError("Não é possível o A ser igual a zero")
    
    def set_B(self,b):
        self.__b = b
    
    def set_C(self,c):
        self.__c = c
        
    
    def get_A(self):
        return self.__a

    def get_B(self):
        return self.__b

    def get_C(self):
        return self.__c
    
    def calc_Delta(self):
        return self.__b ** 2 - (4 * self.__a * self.__c)
    
    def calc_Baskara(self):
        if self.calc_Delta() >= 0: 
            x1 = ((self.__b * -1) - math.sqrt(self.calc_Delta())) / 2 * self.__a
            x2 = ((self.__b * -1) + math.sqrt(self.calc_Delta())) / 2 * self.__a
            return x1, x2
        return None, None
    
# a = int(input())
# b = int(input())
# c = int(input())

# e = EquacaoII(a,b,c)
# print("A = ",e.get_A())
# print("B = ",e.get_B())
# print("C = ",e.get_C())
# print(e.calc_Delta())
# print(e.calc_Baskara())