class Categoria:
    def __init__(self,descricao):
        self.__id = 0
        self.__descricao = ""

        self.set_descricao(descricao)

    def set_descricao(self,descricao):
        if (type(descricao) == str):
            self.__descricao = descricao
        else:
            raise ValueError("Descrição errada")


    def __str__(self):
        return f"Id: {self.__id} - Descricao: {self.__descricao}"
    
    def get_idCATEGORIA(self):
        return self.__id