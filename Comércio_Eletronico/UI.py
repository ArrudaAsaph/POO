from models.class_Cliente import Cliente, Clientes

class UI:
    @staticmethod
    def main():
        op = 0

        while (op != -1):
            op = int(UI.menu())
            match (op):
                case 1:
                    UI.cadastrar_Cliente()
                    break
                case 2:
                    UI.listar_Clientes()

    @staticmethod

    def menu():
        print("Escolha uma opção abaixo!")
        print("1 - Cadastrar Cliente, 2 - Listar Cliente")
        return int(input("Digite a opção desejada: "))
    
    @staticmethod
    def cadastrar_Cliente():
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        senha = input("Senha: ")
        novo_Cliente = Cliente(0,nome,telefone,email,senha)
        Clientes.inserir_Cliente(novo_Cliente)

    @staticmethod
    def listar_Clientes():
        clientes = Clientes.listar_Clientes()

        for x in clientes:
            print(x)

UI.main()
