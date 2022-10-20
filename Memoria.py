from paginaVirtual import paginaVirtual

class Memoria:
    def __init__(self):
        self.memoriaVirtual = []
        self.fisica = ["","","","","","","",""]
        self.hd = ["","","","","","","","","","","","","","","",""]

    def iniciaMemorias(self):
        for i in range(16):
            self.x = paginaVirtual(0, False, False, False, i)
            self.memoriaVirtual.append(self.x)
        #print('Vamos te mostrar a paginação.')


    def mostraPaginacao(self):
        for i in range (16):
            print(f'PAGINA {self.memoriaVirtual[i].getEnd_memoria()} - COUNTER: {self.memoriaVirtual[i].getCounter()} - PRESENCA: {self.memoriaVirtual[i].getPresenca()} - MODIFICADO: {self.memoriaVirtual[i].getModificado()} - REFERENCIADO {self.memoriaVirtual[i].getReferencia()}\n')