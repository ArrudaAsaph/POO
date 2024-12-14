import json
class Categoria:
    def __init__(self,id,descricao):
        self.id = id
        self.descricao = descricao
    
    def __str__(self):
        return f"Id: {self.id} - Descrição: {self.descricao}"


class Categorias:
    lista_Categorias = []

    @classmethod
    def inserir_Categ(cls,obj):
        cls.abrir_Categ()

        id = 0
        for x in cls.lista_Categorias:
            if x.id > id: id = x.id
        obj.id = id + 1
        cls.lista_Categorias.append(obj)
        cls.salvar_Categ()
    
    @classmethod
    def listar_Categ(cls):
        cls.abrir_Categ()
        return cls.lista_Categorias
    
    @classmethod
    def listar_Id(cls,id):
        cls.abrir_Categ()
        for x in cls.lista_Categorias:
            if x.id == id: return x
        return None
    
    @classmethod
    def atualizar_Categ(cls,obj):
        x = cls.listar_Id(obj.id)   
        if (x != None):
            cls.lista_Categorias.remove(x)
            cls.lista_Categorias.append(obj)
            cls.salvar_Categ()

    @classmethod
    def excluir_Categ(cls,obj):
        x = cls.listar_Id(obj.id)
        if (x != None):
            cls.lista_Categorias.remove(x)
            cls.salvar_Categ()
        
    
    @classmethod
    def salvar_Categ(cls):
        with open("categorias.json", mode="w") as arquivo:
            json.dump(cls.lista_Categorias,arquivo, default=vars)

    @classmethod
    def abrir_Categ(cls):
        cls.lista_Categorias = []

        try:
            with open("categorias.json", mode = "r") as arquivo:
                Categorias_json = json.load(arquivo)
                for obj in Categorias_json:
                    c = Categoria(obj["id"],obj["descricao"])
                    cls.lista_Categorias.append(c)
                
        except FileNotFoundError:
            pass