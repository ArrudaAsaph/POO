import json

class Cliente:
    def __init__(self, id, nome, telefone, email, senha):
        self.id = 0
        self.nome = ""
        self.telefone = ""
        self.email = ""
        self.senha = ""
        self.set_id(id)
        self.set_nome(nome)
        self.set_telefone(telefone)
        self.set_email(email)
        self.set_senha(senha)

    def set_id(self, id):
        self.id = id
    
    def set_nome(self,nome):
       self.nome = nome

    def set_telefone(self,telefone):
        self.telefone = telefone
    
    def set_email(self,email):
        self.email = email

    def set_senha(self,senha):
        self.senha = senha
    
    def get_id(self):
        return self.id
    
    def get_nome(self):
        return self.nome
    
    def get_telefone(self):
        return self.telefone
    
    def get_email(self):
        return self.email
    
    def get_senha(self):
        return self.senha
    
    def to_dict(self): return { "id": self.id, "nome": self.nome, "telefone": self.telefone, "email": self.email, "senha": self.senha }

    def __str__(self):
        return f"id: {self.get_id()} - Nome: {self.get_nome()} - Telefone: {self.get_telefone()} - Email: {self.get_email()}"
    
class Clientes:
    lista_Clientes = []

    @classmethod
    def inserir_Clien(cls,obj):
        cls.abrir_Clien()

        id = 0
        for x in cls.lista_Clientes:
            if x.id > id: id = x.id
        obj.id = id + 1
        cls.lista_Clientes.append(obj)
        cls.salvar_Clien()
    
    @classmethod
    def listar_Clien(cls):
        cls.abrir_Clien()
        return cls.lista_Clientes
    
    @classmethod
    def listar_Id(cls,id):
        cls.abrir_Clien()
        for x in cls.lista_Clientes:
            if x.id == id: return x
        return None
    
    @classmethod
    def atualizar_Clien(cls,obj):
        x = cls.listar_Id(obj.id)   
        if (x != None):
            cls.lista_Clientes.remove(x)
            cls.lista_Clientes.append(obj)
            cls.salvar_Clien()

    @classmethod
    def excluir_Clien(cls,obj):
        x = cls.listar_Id(obj.id)
        if (x != None):
            cls.lista_Clientes.remove(x)
            cls.salvar_Clien()
        
    
    @classmethod
    def salvar_Clien(cls):
        with open("clientes.json", mode="w") as arquivo:
            json.dump(cls.lista_Clientes,arquivo, default=vars)

    @classmethod
    def abrir_Clien(cls):
        cls.lista_Clientes = []

        try:
            with open("clientes.json", mode = "r") as arquivo:
                clientes_json = json.load(arquivo)
                for obj in clientes_json:
                    c = Cliente(obj["id"],obj["nome"],obj["telefone"],obj["email"],obj["senha"])
                    cls.lista_Clientes.append(c)
                
        except FileNotFoundError:
            pass