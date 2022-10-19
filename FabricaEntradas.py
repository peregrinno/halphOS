import random

class FabricaEntradas:
    def __init__(self, tam):
        self.tam = tam
        self.entrada = []
        self.tipo = ["W","R"]

    def entrada(self):
        for i in range(self.tam):
            self.endereco = random.randint(0,9)
            self.valor = random.randint(0,99)
            if self.tipo.choice() == "W":
                indice = str(self.endereco) + "-W-" + str()