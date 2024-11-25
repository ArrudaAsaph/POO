from class_Categoria import Categoria

class Produto:
    def __init__(self,descricao) -> None:
        self.__idPRODUTO = 0
        self.__descricaoPRODUTO  = ""
        self.__precoPRODUTO  = 0.0
        self.__estoquePRODUTO  = 0
        self.__idCATEGORIA = 0

        self.set_descricao(descricao)
    
    def set_descricao(self,descricao):
        if (type(descricao) == str):
            self.__descricaoPRODUTO = descricao
        else:
            raise ValueError("Descrição errada")
        
    def __str__(self):
        return f"Id: {self.__idPRODUTO} - Descricao: {self.__descricaoPRODUTO} - Preço R$: {self.__precoPRODUTO} - Estoque: {self.__estoquePRODUTO} - ID_Categoria: {self.__idCATEGORIA}"
