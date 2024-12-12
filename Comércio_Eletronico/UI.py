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
                case 2:
                    UI.listar_Clientes()
                case 3:
                    UI.atualizar_Cliente()
                case 4:
                    UI.remover_Cliente()

    @staticmethod

    def menu():
        print("Escolha uma opção abaixo!")
        print("1 - Cadastrar Cliente, 2 - Listar Cliente, 3 - Atualizar, 4 - Excluir")
        return int(input("Digite a opção desejada: "))
    
    @classmethod
    def cadastrar_Cliente(cls):
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        senha = input("Senha: ")
        novo_Cliente = Cliente(0,nome,telefone,email,senha)
        Clientes.inserir_Cliente(novo_Cliente)

    @classmethod
    def listar_Clientes(cls):
        clientes = Clientes.listar_Clientes()

        for x in clientes:
            print(x)

    @classmethod
    def atualizar_Cliente(cls):
        cls.listar_Clientes()guit

        id = int(input("Informe o id do cliente a ser alterado: "))
        nome = input("Informe o novo nome: ")
        telefone = input("Informe o novo fone: ")
        email = input("Informe o novo email: ")
        senha = input("Informe a senha: ")

        cliente_atualizado = Cliente(id,nome,telefone,email,senha)
        Clientes.atualizar_Cliente(cliente_atualizado)

    @classmethod
    def remover_Cliente(cls):
        cls.listar_Clientes()

        id = int(input("Informe o id do cliente a ser removido: "))
        cliente_excluido = Cliente(id,"","","","")
        Clientes.excluir_Cliente(cliente_excluido)
UI.main()
