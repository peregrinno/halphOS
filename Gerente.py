from Memoria import Memoria
from Intermediador import Intermediador
from paginaVirtual import paginaVirtual
import time

class Gerente:
    def __init__(self,entrada):
        self.entrada = entrada
        
    def ligaSO(self, memoriaVirtual, memoriaFisica):
        self.paginas = []
        for i in range(len(memoriaVirtual)):
            self.paginas.append(paginaVirtual(0, False, False, False, i))
            
        memoria = Memoria(memoriaVirtual, memoriaFisica)
        print("Memoria iniciada")

    def iniciaProcesso(self):
        self.intermedio_1 = Intermediador(1)

    def gerenciaProcessos(self):
        self.intermedio_1.run(self.entrada, self.paginas)

    def mostraPaginacao(self):
        for i in range (len(self.paginas)):
            print(f'PAGINA {self.paginas[i].getEnd_memoria()} - COUNTER: {self.paginas[i].getCounter()} - PRESENCA: {self.paginas[i].getPresenca()} - MODIFICADO: {self.paginas[i].getModificado()} - REFERENCIADO {self.paginas[i].getReferencia()}\n')
        

        
        
        

            
        
    