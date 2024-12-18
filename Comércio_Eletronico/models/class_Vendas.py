import json
from datetime import datetime

class Venda:
    def __init__ (self, id, data, carrinho, total, id_Cliente):
        self.id = 0
        self.data = 0
        self.carrinho = 0
        self.total = 0.0
        self.id_Cliente = 0
        self.set_Id(id)
        self.set_Data(data)
        self.set_Carrinho(carrinho)
        self.set_Total(total)
        self.set_Id_Cliente(id_Cliente)

    def set_Id (self, id):
        if id >= 0:
            self.id = id
        else:
            raise ValueError ("Id invalido")
    
    def set_Data (self, data):
        if data != None:
            self.data = data
        else:
            dia = datetime.today()
            self.data = dia.isoformat()


    def set_Carrinho (self, carrinho):
        if type(carrinho) == bool:
            self.carrinho = carrinho
        else:
            raise ValueError ("Carrinho invalido")

    def set_Total (self, total):
        if total >= 0:
            self.total = total
        else:
            raise ValueError ("Total invalido")

    def set_Id_Cliente (self, id_Cliente):
        self.id_Cliente = id_Cliente

        
    def __str__ (self):
        return f"Id: {self.id} - Data: {self.data} - Carrinho: {self.carrinho} - Total: R${self.total} - Id_Cliente: {self.id_Cliente}"
    
class Vendas:
    lista_Vendas = []

    @classmethod
    def inseri_Vend(cls,obj):
        cls.abri_Vend()

        id = 0
        for x in cls.lista_Vendas:
            if x.id > id: id = x.id
        obj.id = id + 1
        cls.lista_Vendas.append(obj)
        cls.salva_Vend()
    
    @classmethod
    def lista_Vend(cls):
        cls.abri_Vend()
        return cls.lista_Vendas
    
    @classmethod
    def listar_Id(cls,id):
        cls.abri_Vend()
        for x in cls.lista_Vendas:
            if x.id == id: return x
        return None
    
    @classmethod
    def atualiza_Vend(cls,obj):
        x = cls.listar_Id(obj.id)   
        if (x != None):
            cls.lista_Vendas.remove(x)
            cls.lista_Vendas.append(obj)
            cls.salva_Vend()

    @classmethod
    def exclui_Vend(cls,obj):
        x = cls.listar_Id(obj.id)
        if (x != None):
            cls.lista_Vendas.remove(x)
            cls.salva_Vend()
        
    
    @classmethod
    def salva_Vend(cls):
        with open("Vendas.json", mode="w") as arquivo:
            json.dump(cls.lista_Vendas,arquivo, default=vars)

    @classmethod
    def abri_Vend(cls):
        cls.lista_Vendas = []

        try:
            with open("Vendas.json", mode = "r") as arquivo:
                Vendas_json = json.load(arquivo)
                for obj in Vendas_json:
                    # self, id, data, carrinho, total, id_Cliente
                    c = Venda(obj["id"],obj["data"],obj["carrinho"],obj["total"],obj["id_Cliente"])
                    cls.lista_Vendas.append(c)
                
        except FileNotFoundError:
            pass