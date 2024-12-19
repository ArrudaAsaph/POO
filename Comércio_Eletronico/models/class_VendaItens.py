import json

class VendaItem:
    def __init__(self, id, nome, qtd, preco, id_venda, id_produto):
        self.id = 0
        self.nome = ""
        self.qtd = 0
        self.preco = 0.0
        self.id_venda = 0
        self.id_produto = 0
        self.set_id(id)
        self.set_nome(nome)
        self.set_qtd(qtd)
        self.set_preco(preco)
        self.set_id_venda(id_venda)
        self.set_id_produto(id_produto)

    def set_id(self, id):
        if id >= 0:
            self.id = id
        else:
            raise ValueError("Id inválido")

    def set_nome(self, nome):
        if len(nome) > 0:
            self.nome = nome
        else:
            raise ValueError("Nome inválido")

    def set_qtd(self, qtd):
        if qtd >= 0:
            self.qtd = qtd
        else:
            raise ValueError("Quantidade inválida")

    def set_preco(self, preco):
        if preco >= 0:
            self.preco = preco
        else:
            raise ValueError("Preço inválido")

    def set_id_venda(self, id_venda):
        self.id_venda = id_venda

    def set_id_produto(self, id_produto):
        self.id_produto = id_produto

    def __str__(self):
        return f"Id: {self.id} - Nome: {self.nome} - Quantidade: {self.qtd} - Preço: R${self.preco} - Id Venda: {self.id_venda} - Id Produto: {self.id_produto}"

class VendasItems:
    lista_VendasItems = []

    @classmethod
    def inserir_VendaItem(cls,obj):
        cls.abrir_VendaItem()

        id = -1
        for x in cls.lista_VendasItems:
            if x.id > id: id = x.id
        obj.id = id + 1
        cls.lista_VendasItems.append(obj)
        cls.salvar_VendaItem()
    
    @classmethod
    def listar_VendaItem(cls):
        cls.abrir_VendaItem()
        return cls.lista_VendasItems
    
    @classmethod
    def listar_Id(cls,id):
        cls.abrir_VendaItem()
        for x in cls.lista_VendasItems:
            if x.id == id: return x
        return None
    
    @classmethod
    def atualizar_VendaItem(cls,obj):
        x = cls.listar_Id(obj.id)   
        if (x != None):
            cls.lista_VendasItems.remove(x)
            cls.lista_VendasItems.append(obj)
            cls.salvar_VendaItem()

    @classmethod
    def excluir_VendaItem(cls,obj):
        x = cls.listar_Id(obj.id)
        if (x != None):
            cls.lista_VendasItems.remove(x)
            cls.salvar_VendaItem()
        
    
    @classmethod
    def salvar_VendaItem(cls):
        with open("VendasItems.json", mode="w") as arquivo:
            json.dump(cls.lista_VendasItems,arquivo, default=vars)

    @classmethod
    def abrir_VendaItem(cls):
        cls.lista_VendasItems = []

        try:
            with open("VendasItems.json", mode = "r") as arquivo:
                VendasItems_json = json.load(arquivo)
                for obj in VendasItems_json:
                    c = VendaItem(obj["id"],obj["nome"],obj["qtd"],obj["preco"],obj["id_venda"],obj["id_produto"])
                    # (self, id, nome, qtd, preco, id_venda, id_produto)
                    cls.lista_VendasItems.append(c)
                
        except FileNotFoundError:
            pass