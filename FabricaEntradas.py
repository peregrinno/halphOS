#importanto biblioteca randomica 
import random

#Essa classe irá criar a entrada de dados
class FabricaEntradas:
    #Cronstrutor da classe, ela recebe um tamanho que significa o tamanho da entrada
    def __init__(self, tam):
        #Self funciona semelhante ao this do Java
        self.tam = tam
        #Atributo entrada começa como uma lista vazia
        self.entrada = []
        #Esse lista determina se um elemento da entrada vai ser de leitura ou escrita
        self.tipo = ["W","R"]

    #Metodo de criação da entrada
    def getEntrada(self):
        #Nesse laço, aparece um endereço aleatorio, um valor aleatorio (se for escrita)
        for i in range(self.tam):
            self.endereco = random.randint(0,4)
            self.valor = random.randint(0,99)
            if random.choice(self.tipo) == "W":
                indice = str(self.endereco) + "-W-" + str(self.valor)
            else:
                indice = str(self.endereco) + "-R"
            self.entrada.append(indice)
        #Retorna a lista de entradas
        return self.entrada