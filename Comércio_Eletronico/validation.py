from views import Views

class Validation:
    @classmethod
    def Cliente_Validation(cls,nome,telefone,email,senha):
        nome = cls.Cliente_Validation_Name(nome)
        email = cls.Cliente_Validation_Email(email)
        telefone = cls.Cliente_Validation_Phone(telefone)
        Views.adicionar_Cliente(nome,telefone,email,senha)
    #8498143
    @classmethod
    def Cliente_Validation_Name(cls,nome):
        nome = nome.split()
        print(nome)
        space = " "
        for name in nome:
            name = name.capitalize()
            if (name == nome[0].capitalize()):
                upperName = name
                
                upperName += space
            else:
                upperName += name
                upperName += space
        return upperName
    
    @classmethod
    def Cliente_Validation_Email(cls,email):
        if ('@' in email): 
            return email
        else:   
            raise ValueError("Email inválido!")

    @classmethod
    def Cliente_Validation_Phone(cls,telefone):
        if (len(telefone) > 15 or len(telefone) < 11 ):
            # raise ValueError("Número inválido!")
            return cls.Cliente_Validation_Phone(input("Digite um número válido: "))
           

        else:
            number = "("
            parenthenses = ")"
            for i in range(1,len(telefone)):
                if (i == 1):
                    number += telefone[i-1]
                    number += telefone[i]
                    number += parenthenses
                    number += " "
                elif (i == 7) :
                    number += "-"
                    number += telefone[i]
                else:
                    number += telefone[i]
            return number


