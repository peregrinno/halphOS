from FabricaEntradas import FabricaEntradas
from Intermediador import Intermediador
from Memoria import Memoria
from Moderador import Moderador
import time

class Gerente:
    def __init__(self):
        self.fabrica = FabricaEntradas(30)
        
    def recebeEntrada(self):
        self.entrada = self.fabrica.getEntrada()
        print("[GERENTE] Entrada recebida!")
        print(f'{self.entrada}')

    def ligaSO(self):
        print("[GERENTE] Iniciando SO")
        print("[GERENTE] Iniciando memória")
        self.memoria = Memoria()
        self.memoria.iniciaMemorias()
        #memoria.mostraPaginacao()
        time.sleep(2)
        print("[GERENTE] Memória iniciada")

    def iniciaProcessamento(self):
        moderacao = Moderador(self.entrada)
        intermedia_1 = Intermediador(1, moderacao, self.memoria)
        intermedia_1.start()
        intermedia_2 = Intermediador(2, moderacao, self.memoria)
        intermedia_2.start()
        intermedia_3 = Intermediador(3, moderacao, self.memoria)
        intermedia_3.start()
        

