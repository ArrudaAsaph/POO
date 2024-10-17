# Introdução a Programação Orientada a Objetos.

# Imagine o mundo real, onde temos tiver objetos, como Garrafa, Carro, Casa, Prédio, tudo isso são objetos.

# Objetos nada mais são que coisas que existem no mundo real.

# Mas vamos pensar um pouco, aqui em cima falamos sobre Casa, Prédio.

# Casa e Prédio possuem um coisa em comum, genérica, que é que ambos servem para moradia, ou seja, podemos dizer que casa e prédio são objetos de uma moradia.

# Ou sejam temos uma Classe Moradia, onde falam tudo, as funções (Deixar as pessoas seguras, Ter cozinha);

# Isso mostra que objetos são uma coisa meio que parecida um com os outros, pois, são da mesma clase.

# CLASSE TRIANGULO
class Triangulo:
    
    # CONSTRUTOR
    def __init__(self):
        self.base = 0
        self.altura = 0 
    
    def calculoArea(self):
        area = self.base * self.altura / 2
        print(f"A area do seu Triangulo com base {self.base} e altura {self.altura} = {area}")
        return area


a = Triangulo()

a.base , a.altura = map(int,input("Digire a BASE e a ALUTRA do seu Triangulo: ").split())

print(a.calculoArea())