from class_Cliente import Cliente
import json

class Clientes:
  
    clientes_lista = []

    @classmethod
    def inserir(cls,obj):
        cls.abrir()
        cls.clientes_lista.append(obj)
        cls.salvar()


    @classmethod 
    def salvar(cls):

        # open - cria e abre o arquivo clientes.json
        # vars - converte um objeto em um dicionário
        # dump - pega a lista de objetos e salva no arquivo

        with open("clientes.json", mode= "w") as arquivo:
            json.dump(cls.clientes_lista, arquivo, default = vars)
    
    @classmethod 
    #serve para poder usar qualquer varivel dentro da class
    def abrir(cls):
        cls.clientes_lista = []

        try:
            with open("clientes.json", mode = "r") as arquivo:
                clientes_json = json.load(arquivo)

                for obj in clientes_json:
                    c = Cliente(obj["id"], obj["nome"], obj["email"], obj["telefone"])

                    cls.clientes_lista.append(c)

        except FileNotFoundError:
            pass
    


    
            
teste = Clientes()
teste.inserir("Asaph","asapharruda@gmail.com",8495123456)
teste.inserir("Akasknask","akasknaskarruda@gmail.com",8495123456)
teste.inserir("Asapasasash","asaphAsasasarruda@gmail.com",8495123456)
teste.listar_Clientes()
teste.remove_Cliente(1)
print("")
teste.listar_Clientes()

