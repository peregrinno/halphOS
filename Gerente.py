from Memoria import Memoria
from Intermediador import Intermediador
import time

class Gerente:
    def __init__(self,entrada):
        self.entrada = entrada
        
    def ligaSO(self, memoriaVirtual, memoriaFisica):
        memoria = Memoria(memoriaVirtual, memoriaFisica)
        print("Memoria iniciada")

    def iniciaProcesso(self):
        self.intermedio_1 = Intermediador(1)
        self.intermedio_2 = Intermediador(2)
        self.intermedio_3 = Intermediador(3)

    def gerenciaProcessos(self):
        self.intermedio_1.run(self.entrada)
        time.sleep(1)
        self.intermedio_2.run(self.entrada)
        time.sleep(1)
        self.intermedio_3.run(self.entrada)
        
        
        

            
        
    