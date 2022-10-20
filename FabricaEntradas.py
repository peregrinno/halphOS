import random

class FabricaEntradas:
    def __init__(self, tam):
        self.tam = tam
        self.entrada = []
        self.tipo = ["W","R"]

    def getEntrada(self):
        for i in range(self.tam):
            self.endereco = random.randint(0,9)
            self.valor = random.randint(0,99)
            if random.choice(self.tipo) == "W":
                indice = str(self.endereco) + "-W-" + str(self.valor)
            else:
                indice = str(self.endereco) + "-R"
            self.entrada.append(indice)
        return self.entrada