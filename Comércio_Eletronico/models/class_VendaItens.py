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

    
class VendaItens:
    lista_venda_itens = []

    @classmethod
    def inserir_VendaIt(cls, obj):
        cls.abrir_VendaIt()

        id = 0
        for item in cls.lista_venda_itens:
            if item.id > id:
                id = item.id
        obj.set_id(id + 1)

        cls.lista_venda_itens.append(obj)

        cls.salvar_VendaIt()

    @classmethod
    def listar_VendaIt(cls):
        cls.abrir_VendaIt()
        return cls.lista_venda_itens

    @classmethod
    def listar_id(cls, id):
        cls.abrir_VendaIt()

        for item in cls.lista_venda_itens:
            if item.id == id:
                return item
        return None

    @classmethod
    def atualizar_VendaIt(cls, obj):
        item = cls.listar_id(obj.id)
        if item is not None:
            item.set_nome(obj.nome)
            item.set_qtd(obj.qtd)
            item.set_preco(obj.preco)
            item.set_id_venda(obj.id_venda)
            item.set_id_produto(obj.id_produto)
            cls.salvar()

    @classmethod
    def excluir_VendaIt(cls, obj):
        item = cls.listar_id(obj.id)
        if item is not None:
            cls.lista_venda_itens.remove(item)
            cls.salvar_VendaIt()

    @classmethod
    def salvar_VendaIt(cls):
        with open("Vendaitens.json", mode="w") as arquivo:
            json.dump(cls.lista_venda_itens, arquivo, default=vars)

    @classmethod
    def abrir_VendaIt(cls):
        cls.lista_venda_itens = []
        try:
            with open("vendaitens.json", mode="r") as arquivo:
                itens_json = json.load(arquivo)
                for obj in itens_json:
                    item = VendaItem(
                        obj["id"],
                        obj["nome"],
                        obj["qtd"],
                        obj["preco"],
                        obj["id_venda"],
                        obj["id_produto"]
                    )
                    cls.lista_venda_itens.append(item)
        except FileNotFoundError:
            pass
