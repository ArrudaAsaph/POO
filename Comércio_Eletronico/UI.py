from controle import Controle

class UI:
    @staticmethod
    def main():
        op = 0

        Controle.Admin()

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
                case 5:
                    UI.cadastrar_Categoria()
                case 6:
                    UI.listar_Categorias()
                case 7:
                    UI.atualizar_Categorias()
                case 8:
                    UI.remover_Categoria()
                case 9:
                    UI.cadastrar_Produto()
                case 10:
                    UI.listar_Produto()
                case 11:
                    UI.atualizar_Produtos()
                case 12:
                    UI.remover_Produto()

# =================================================================================================================================
# MENU 
    
    
    @staticmethod
    def menu():
        print("Escolha uma opção abaixo!")
        print("1 - Cadastrar Cliente, 2 - Listar Cliente, 3 - Atualizar, 4 - Excluir")
        print("5 - Cadastrar Categoria, 6 - Listar Categoria, 7 - Atualizar, 8 - Excluir")
        print("9 - Cadastrar Produto, 10 - Listar Produto, 11 - Atualizar, 12 - Excluir")
        return int(input("Digite a opção desejada: "))

# ================================== CLIENTES ==============================================================================================
# CADASTRAR
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

# LISTAR
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

# ATUALIZAR
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


# REMOVER
    @classmethod
    def remover_Cliente(cls):
        cls.listar_Clientes()

        id = int(input("Informe o id do cliente a ser removido: "))
        # cliente_excluido = Cliente(id,"","","","")
        Controle.Cliente_Excluir(id)
# ================================== CATEGORIAS ==============================================================================================
# CADASTRAR
    @classmethod
    def cadastrar_Categoria(cls):
        descricao = input("Insira a descrição: ")
        # nova_Categoria = Categoria(0,descricao)
        # Categorias.inserir_Categoria(nova_Categoria)
        Controle.Categoria_Validation_Description(descricao)

# LISTAR
    @classmethod
    def listar_Categorias(cls):
        categorias = Controle.Categoria_Listar()
        if (len(categorias) == 0):
            print("Não há nenhum cliente cadastrado!")
        else:
            print("------------" * 10)
            for x in categorias:
                print(x)
            print("------------" * 10)

# ATUALIZAR
    @classmethod
    def atualizar_Categorias(cls):
        cls.listar_Categorias()

        id = int(input("Informe o id da categoria a ser alterado: "))
        descricao = input("Informe a nova descrição: ")
        Controle.Categoria_Atualizar(id,descricao)

# REMOVER    
    @classmethod
    def remover_Categoria(cls):
        cls.listar_Categorias()

        id = int(input("Informe o id do cliente a ser removido: "))
        # categoria_excluido = Categoria(id,"")
        # Categorias.excluir_Categoria(categoria_excluido)
        Controle.Categoria_Excluir(id)
    
# ================================== PRODUTOS ==============================================================================================
# CADASTRAR

    @classmethod
    def cadastrar_Produto(cls):
        descricao = input("Informe a descrição do Produto: ")
        preco = input("Informe a preco do Produto: R$")
        quantidade = input("Informe a quantidade do Produto: ")
        
        cls.listar_Categorias()
        id_Categoria = int(input("Informe o id da Categoria: "))
        while True:
            print(f"Id cat antes{id_Categoria}")
            id_Categoria = Controle.Produto_Validation_IdCatogoria(id_Categoria)
            print(f"Id cat dps{id_Categoria}")

            if id_Categoria == None:
                print("Categoria invalida")
                id_Categoria = int(input("Informe uma categoria válida: "))
            else:
                break
        
        Controle.Produto_Validation(descricao,preco,quantidade,id_Categoria)


        # novo_Produto = Produto(0,descricao,preco,quantidade,id_Categoria)
        # Produtos.inserir_Produtos(novo_Produto)
    
    @classmethod
    def listar_Produto(cls):
        produtos = Controle.Produto_Listar()
        if (len(produtos) == 0):
            print("Não há nenhum cliente cadastrado!")
        else:
            print("------------" * 10)
            for x in produtos:
                print(x)
            print("------------" * 10)
   
    @classmethod
    def atualizar_Produtos(cls):
        cls.listar_Produto()
        id = int(input("Informe o id dos produtos a ser alterado: "))
        descricao = input("Informe a nova descrição: ")
        preco = float(input("Informe o novo valor: "))
        estoque = int(input("Informe o novo estoque: "))

        cls.listar_Categorias()
        id_Categoria = int(input("Informe o id da Categoria: "))
        while True:
            id_Categoria = Controle.Produto_Validation_IdCatogoria(id_Categoria)

            if id_Categoria == None:
                print("Categoria invalida")
                id_Categoria = int(input("Informe uma categoria válida: "))
            else:
                break
        
        Controle.Produto_Atualizar(id,descricao,preco,estoque,id_Categoria)

    @classmethod
    def remover_Produto(cls):
        cls.listar_Produto()

        id = int(input("Informe o id do cliente a ser removido: "))
        Controle.Produto_Excluir(id)

        ''
        
UI.main()
