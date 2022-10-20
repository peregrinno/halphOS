from paginaVirtual import paginaVirtual
from datetime import datetime

class Memoria:
    def __init__(self):
        self.memoriaVirtual = []
        self.fisica = ["","","","",""]
        self.hd = ["","","","","","","","","",""]

    def iniciaMemorias(self):
        for i in range(10):
            self.x = paginaVirtual(0, False, False, False, i)
            self.memoriaVirtual.append(self.x)
        #print('Vamos te mostrar a paginação.')

    def mostraPaginacao(self):
        for i in range (10):
            print(f'PAGINA {self.memoriaVirtual[i].getEnd_memoria()} - COUNTER: {self.memoriaVirtual[i].getCounter()} - PRESENCA: {self.memoriaVirtual[i].getPresenca()} - MODIFICADO: {self.memoriaVirtual[i].getModificado()} - REFERENCIADO {self.memoriaVirtual[i].getReferencia()}\n')

    def operacaoEscrita(self, index, valor):
        self.index = index
        self.valor = int(valor)
        
        if self.memoriaVirtual[index].getReferencia() == False:
            self.memoriaVirtual[index].setReferencia(True)
            self.memoriaVirtual[index].setEnd_memoria(index)
            self.fisica[index] = self.valor
            self.memoriaVirtual[index].setCounter(datetime.now())
            
        elif self.memoriaVirtual[index].getReferencia() == True:
            
            if self.memoriaVirtual[index].getModificado() == False:
                self.memoriaVirtual[index].setReferencia(True)
                self.memoriaVirtual[index].setEnd_memoria(index)
                self.fisica[index] = self.valor
                self.memoriaVirtual[index].setModificado(True)
                self.memoriaVirtual[index].setCounter(datetime.now())

            elif self.memoriaVirtual[index].getModificado() == True:
                print("CHAMA O LRU AI MEU PATRÃO!!")

        print("ESCRITA FEITA")

    def operacaoLeitura(self, index):
        self.index = index
        self.end_Virtual = int(self.memoriaVirtual[self.index].getEnd_memoria())
        print(f'Lendo o valor {self.fisica[self.end_Virtual]}')
        