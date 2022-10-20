from paginaVirtual import paginaVirtual
from datetime import datetime
from LRU import LRU

class Memoria:
    def __init__(self):
        self.memoriaVirtual = []
        self.fisica = ["","","","",""]
        self.ponteiroTempo = [datetime.now(),datetime.now(),datetime.now(),datetime.now(),datetime.now()]
        

    def iniciaMemorias(self):
        for i in range(10):
            self.x = paginaVirtual(0, False, False, False, i)
            self.memoriaVirtual.append(self.x)
        #print('Vamos te mostrar a paginação.')

    def mostraPaginacao(self):
        for i in range (10):
            print(f'[MEMÓRIA] PAGINA {self.memoriaVirtual[i].getEnd_memoria()} - COUNTER: {self.memoriaVirtual[i].getCounter()} - PRESENCA: {self.memoriaVirtual[i].getPresenca()} - MODIFICADO: {self.memoriaVirtual[i].getModificado()} - REFERENCIADO {self.memoriaVirtual[i].getReferencia()}\n')

    def operacaoEscrita(self, index, valor):
        self.index = index
        self.valor = int(valor)
        
        if self.memoriaVirtual[self.index].getReferencia() == False:
            self.memoriaVirtual[self.index].setReferencia(True)
            self.memoriaVirtual[self.index].setEnd_memoria(self.index)
            self.fisica[self.index] = self.valor
            self.ponteiroTempo[self.index] = datetime.now()
            self.memoriaVirtual[self.index].setCounter(datetime.now())
            
        elif self.memoriaVirtual[self.index].getReferencia() == True:
            
            if self.memoriaVirtual[self.index].getModificado() == False:
                self.memoriaVirtual[self.index].setReferencia(True)
                self.memoriaVirtual[self.index].setEnd_memoria(self.index)
                self.fisica[self.index] = self.valor
                self.ponteiroTempo[self.index] = datetime.now()
                self.memoriaVirtual[self.index].setModificado(True)
                self.memoriaVirtual[self.index].setCounter(datetime.now())

            elif self.memoriaVirtual[self.index].getModificado() == True:
                self.substituicao = LRU()
                self.end_Virtual = int(self.memoriaVirtual[self.index].getEnd_memoria())
                self.antiga = self.fisica[self.end_Virtual]
                self.fisica[self.index] = self.valor
                self.ponteiroTempo[self.index] = datetime.now()
                #CHAMADA A LRU
                self.index = self.substituicao.LRU(self.fisica, self.valor, self.antiga, self.ponteiroTempo)
                

        print("[MEMORIA] ESCRITA FEITA")

    def operacaoLeitura(self, index):
        self.index = index
        self.end_Virtual = int(self.memoriaVirtual[self.index].getEnd_memoria())
        self.ponteiroTempo[self.end_Virtual] = datetime.now()
        print(f'[MEMÓRIA] Lendo o valor {self.fisica[self.end_Virtual]}')
        