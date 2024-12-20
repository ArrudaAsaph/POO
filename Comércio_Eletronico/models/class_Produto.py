import json

class Produto:
    def __init__(self,id,descricao,preco,estoque,id_categoria):
        self.id = id
        self.descricao = descricao
        self.preco = preco
        self.estoque = estoque
        self.id_categoria  = id_categoria

    def __str__(self):
        return f"id: {self.id} - descricao: {self.descricao} - Preço R${self.preco} - Estoque: {self.estoque} - IdCategoria: {self.id_categoria}"

class Produtos:
    lista_Produtos = []

    @classmethod
    def inserir_Prod(cls,obj):
        cls.abrir_Prod()

        id = 0
        for x in cls.lista_Produtos:
            if x.id > id: id = x.id

        obj.id = id + 1
        cls.lista_Produtos.append(obj)
        cls.salvar_Prod()
    
    @classmethod
    def listar_Prod(cls):
        cls.abrir_Prod()
        return cls.lista_Produtos
    
    @classmethod
    def listar_Id(cls,id):
        cls.abrir_Prod()
        for x in cls.lista_Produtos:
            if x.id == id: return x
        return None
    
    @classmethod
    def atualizar_Prod(cls,obj):
        x = cls.listar_Id(obj.id)   
        if (x != None):
            cls.lista_Produtos.remove(x)
            cls.lista_Produtos.append(obj)
            cls.salvar_Prod()

    @classmethod
    def excluir_Prod(cls,obj):
        x = cls.listar_Id(obj.id)
        if (x != None):
            cls.lista_Produtos.remove(x)
            cls.salvar_Prod()
        
    
    @classmethod
    def salvar_Prod(cls):
        with open("produtos.json", mode="w") as arquivo:
            json.dump(cls.lista_Produtos,arquivo, default=vars)

    @classmethod
    def abrir_Prod(cls):
        cls.lista_Produtos = []

        try:
            with open("produtos.json", mode = "r") as arquivo:
                Produtos_json = json.load(arquivo)
                for obj in Produtos_json:
                    c = Produto(obj["id"],obj["descricao"],obj["preco"],obj["estoque"],obj["id_categoria"])
                    cls.lista_Produtos.append(c)
                
        except FileNotFoundError:
            pass
