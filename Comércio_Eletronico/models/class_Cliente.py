class Cliente:
    def __init__(self, id, nome, telefone, email, senha):
        self.__id = 0
        self.__nome = ""
        self.__telefone = ""
        self.__email = ""
        self.__senha = ""
        self.set_id(id)
        self.set_nome(nome)
        self.set_telefone(telefone)
        self.set_email(email)
        self.set_senha(senha)

    def set_id(self, id):
        self.__id = id
    
    def set_nome(self,nome):
       self.__nome = nome

    def set_telefone(self,telefone):
        self.__telefone = telefone
    
    def set_email(self,email):
        self.__email = email

    def set_senha(self,senha):
        self.__senha = senha
    
    def get_id(self):
        return self.__id
    
    def get_nome(self):
        return self.__nome
    
    def get_telefone(self):
        return self.__telefone
    
    def get_email(self):
        return self.__email
    
    def get_senha(self):
        return self.__senha
    
    def __str__(self):
        return f"id: {self.get_id()} - Nome: {self.get_nome()} - Telefone: {self.get_telefone()} - Email: {self.get_email()}"
    
    