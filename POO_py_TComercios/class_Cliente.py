class Cliente:
    def __init__(self,nome,email,telefone):
        self.__id = 0
        self.__nome = ""
        self.__email = ""
        self.__telefone = 0

        self.set_nome(nome)
        self.set_email(email)
        self.set_telefone(telefone)

    def set_nome(self,nome):
        if (type(nome) == str):
            self.__nome = nome
        else:
            raise ValueError("Nome errado")

    def set_email(self,email):
        if (type(email) == str):
            self.__email = email
        else:
            raise ValueError("Email errado")

    def set_telefone(self,telefone):
        if (type(telefone) == int):
            self.__telefone = telefone
        else:
            raise ValueError("Telefone errado")

    def __str__(self):
        return f"Nome: {self.__nome} - Email: {self.__email} - Telefone: {self.__telefone}"
        