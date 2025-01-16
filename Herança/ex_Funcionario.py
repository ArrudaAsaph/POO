class Funcionario:
    def __init__(self,nome,salario_Base):
        self.__nome = nome
        self._salario_base = salario_Base
    def getNome(self):
        return self.__nome
    def getSalario(self):
        return self._salario_base
    def __str__(self):
        return "Nome: " + str(self.getNome()) + " - Salário: " + str(self.getSalario())
    
class Gerente(Funcionario):
    def __init__(self, nome, salario_Base, gratificacao):
        super().__init__(nome, salario_Base)
        self.__gratificacao = gratificacao
    
    def getSalario(self):
        return super().getSalario() + self.__gratificacao
    
    

funcionario = Funcionario("Pedro Gustavo", 4500)
gerente = Gerente("Asaph", 4500, 2500)

print(funcionario)
print(gerente)