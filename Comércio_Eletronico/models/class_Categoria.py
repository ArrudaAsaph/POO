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
    def inserir_Categoria(cls,obj):
        cls.abrir_Categoria()

        id = 0
        for x in cls.lista_Categorias:
            if x.id > id: id = x.id
        obj.id = id + 1
        cls.lista_Categorias.append(obj)
        cls.salvar_Categoria()
    
    @classmethod
    def listar_Categoria(cls):
        cls.abrir_Categoria()
        return cls.lista_Categorias
    
    @classmethod
    def listar_Id(cls,id):
        cls.abrir_Categoria()
        for x in cls.lista_Categorias:
            if x.id == id: return x
        return None
    
    @classmethod
    def atualizar_Categoria(cls,obj):
        x = cls.listar_Id(obj.id)   
        if (x != None):
            cls.lista_Categorias.remove(x)
            cls.lista_Categorias.append(obj)
            cls.salvar_Categoria()

    @classmethod
    def excluir_Categoria(cls,obj):
        x = cls.listar_Id(obj.id)
        if (x != None):
            cls.lista_Categorias.remove(x)
            cls.salvar_Categoria()
        
    
    @classmethod
    def salvar_Categoria(cls):
        with open("categorias.json", mode="w") as arquivo:
            json.dump(cls.lista_Categorias,arquivo, default=vars)

    @classmethod
    def abrir_Categoria(cls):
        cls.lista_Categorias = []

        try:
            with open("categorias.json", mode = "r") as arquivo:
                Categorias_json = json.load(arquivo)
                for obj in Categorias_json:
                    c = Categoria(obj["id"],obj["descricao"])
                    cls.lista_Categorias.append(c)
                
        except FileNotFoundError:
            pass