from controle import Controle

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
                # case 4:
                #     UI.remover_Cliente()
                # case 5:
                #     UI.cadastrar_Categoria()
                # case 6:
                #     UI.listar_Categoria()
                # case 7:
                #     UI.atualizar_Categorias()
                # case 8:
                #     UI.remover_Categoria()
                # case 9:
                #     UI.cadastrar_Produto()
                # case 10:
                #     UI.listar_Produto()
                # case 11:
                #     UI.atualizar_Produtos()
                # case 12:
                #     UI.remover_Produto()

    @staticmethod

    def menu():
        print("Escolha uma opção abaixo!")
        print("1 - Cadastrar Cliente, 2 - Listar Cliente, 3 - Atualizar, 4 - Excluir")
        print("5 - Cadastrar Categoria, 6 - Listar Categoria, 7 - Atualizar, 8 - Excluir")
        print("9 - Cadastrar Produto, 10 - Listar Produto, 11 - Atualizar, 12 - Excluir")
        return int(input("Digite a opção desejada: "))
    
    @classmethod
    def cadastrar_Cliente(cls):
        nome = input("Informe o nome: ")
        nome = Controle.Cliente_Validation_Name(nome)
    
        telefone = input("Informe o telefone: ")
        while True:
            telefone = Controle.Cliente_Validation_Phone(telefone)
            if (telefone == None):
                print("----------------------------")
                print("Número de telefone inválido!")
                print("Ex: DDD + XXXXXXXXX (84981311523)")
                telefone = input("Informe o um número de telefone válido: ")
                print("----------------------------")
            else:
                break

        email = input("Informe o email: ")
        while True:
            email = Controle.Cliente_Validation_Email(email)
            if (email == None):
                print("----------------------------")
                print("Número de email inválido!")
                print("Ex: xxxxx@xxxx.com (azulvermelho@gmail.com))")
                email = input("Informe o um número de email válido: ")
                print("----------------------------")
            else:
                break

        senha = input("Informe o senha: ")
        Controle.Cliente_Validation(nome,telefone,email,senha)


    @classmethod
    def listar_Clientes(cls):
        clientes = Controle.Cliente_Listar()
        if (len(clientes) == 0):
            print("Não há nenhum cliente cadastrado!")
        else:
            print("------------" * 10)
            for x in clientes:
                print(x)
            print("------------" * 10)

    @classmethod
    def atualizar_Cliente(cls):
        cls.listar_Clientes()
        id = int(input("Informe o id do cliente a ser alterado: "))
        print(" ")
        nome = input("Informe o novo nome: ")
        nome = Controle.Cliente_Validation_Name(nome)
        telefone = input("Informe o novo fone: ")
        while True:
            telefone = Controle.Cliente_Validation_Phone(telefone)
            if (telefone == None):
                print("----------------------------")
                print("Número de telefone inválido!")
                print("Ex: DDD + XXXXXXXXX (84981311523)")
                telefone = input("Informe o um número de telefone válido: ")
                print("----------------------------")
            else:
                break
        email = input("Informe o novo email: ")
        while True:
            email = Controle.Cliente_Validation_Email(email)
            if (email == None):
                print("----------------------------")
                print("Número de email inválido!")
                print("Ex: xxxxx@xxxx.com (azulvermelho@gmail.com))")
                email = input("Informe o um número de email válido: ")
                print("----------------------------")
            else:
                break

        senha = input("Informe a senha: ")

        Controle.Cliente_Atualizar(id,nome,telefone,email,senha)


    @classmethod
    def remover_Cliente(cls):
        cls.listar_Clientes()

        id = int(input("Informe o id do cliente a ser removido: "))
        # cliente_excluido = Cliente(id,"","","","")
        id
        Clientes.excluir_Cliente(cliente_excluido)

    # @classmethod
    # def cadastrar_Categoria(cls):
    #     descricao = input("Insira a descrição: ")
    #     nova_Categoria = Categoria(0,descricao)
    #     Categorias.inserir_Categoria(nova_Categoria)

    # @classmethod
    # def listar_Categoria(cls):
    #     categoria = Categorias.listar_Categoria()

    #     for x in categoria:
    #         print(x)

    # @classmethod
    # def atualizar_Categorias(cls):
    #     cls.listar_Categoria()

    #     id = int(input("Informe o id da categoria a ser alterado: "))
    #     descricao = input("Informe a nova descrição: ")
    #     categoria_atualizada = Categoria(id,descricao)
    #     Categorias.atualizar_Categoria(categoria_atualizada)
    
    # @classmethod
    # def remover_Categoria(cls):
    #     cls.listar_Categoria()

    #     id = int(input("Informe o id do cliente a ser removido: "))
    #     categoria_excluido = Categoria(id,"")
    #     Categorias.excluir_Categoria(categoria_excluido)

    # @classmethod
    # def cadastrar_Produto(cls):
    #     descricao = input("Informe a descrição do Produto: ")
    #     preco = input("Informe a preco do Produto: R$")
    #     quantidade = input("Informe a quantidade do Produto: ")
        
    #     cls.listar_Categoria()
    #     id_Categoria = input("Informe o id da Categoria: ")

    #     novo_Produto = Produto(0,descricao,preco,quantidade,id_Categoria)
    #     Produtos.inserir_Produtos(novo_Produto)
    
    # @classmethod
    # def listar_Produto(cls):
    #     lista_produto = Produtos.listar_Produtos()

    #     for x in lista_produto:
    #         print(x)
    # # descricao,preco,estoque,id_categoria
    # @classmethod
    # def atualizar_Produtos(cls):
    #     cls.listar_Produto()
    #     id = int(input("Informe o id dos produtos a ser alterado: "))
    #     descricao = input("Informe a nova descrição: ")
    #     preco = float(input("Informe o novo valor: "))
    #     estoque = int(input("Informe o novo estoque: "))

    #     cls.listar_Categoria()
    #     id_categoria = int(input("Informe o id da categoria: "))
    #     produto_atualizada = Produtos(id,descricao,preco,estoque,id_categoria)
    #     Produtos.atualizar_Produtos(produto_atualizada)

    # @classmethod
    # def remover_Produto(cls):
    #     cls.listar_Produto()

    #     id = int(input("Informe o id do cliente a ser removido: "))
    #     produto_excluido = Produto(id,"")
    #     Produtos.excluir_Produtos(produto_excluido)


        
        
UI.main()
