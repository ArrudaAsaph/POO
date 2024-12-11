class Cliente:
    def __init__(self, id, nome, telefone, email, senha):
        self.__id = 0
        self.__nome = ""
        self.__telefone = ""
        self.__email = ""
        self.__senha = ""
    
    def set_id(self, id):
        if (type(id) == int): self.__id = id
        else: raise ValueError("O id precisa ser um inteiro")
    
    def set_nome(self,nome):
        nome = nome.split()
        upperName = " "
        for name in nome:
            name.capitalize()
            name += 
        self.__nome = 