from paginaVirtual import paginaVirtual
from datetime import datetime
from LRU import LRU


#Classe que simula a interface de memoria
class Memoria:
    def __init__(self):
        self.memoriaVirtual = []
        self.fisica = ["","","","",""]
        #Espelho da memoria fisica, marca o tempo que cada endereço foi acessado, sendo leitura ou escrita
        self.ponteiroTempo = [datetime.now(),datetime.now(),datetime.now(),datetime.now(),datetime.now()]
        
    #Inicia a memoria - chamado apenas ao ligar o S.O.
    def iniciaMemorias(self):
        for i in range(10):
            self.x = paginaVirtual(0, False, False, False, i)
            self.memoriaVirtual.append(self.x)
        #print('Vamos te mostrar a paginação.')

    #Metodo só pra ver a paginação da memoria virtual, está comentado em algum lugar do codigo kkk
    def mostraPaginacao(self):
        for i in range (10):
            print(f'[MEMÓRIA] PAGINA {self.memoriaVirtual[i].getEnd_memoria()} - COUNTER: {self.memoriaVirtual[i].getCounter()} - PRESENCA: {self.memoriaVirtual[i].getPresenca()} - MODIFICADO: {self.memoriaVirtual[i].getModificado()} - REFERENCIADO {self.memoriaVirtual[i].getReferencia()}\n')

    #Operação de escrita cabulosa
    def operacaoEscrita(self, index, valor):
        self.index = index
        self.valor = int(valor)

        #Se a moldura não estiver referenciada, ele apenas grava o valor e marca essa moldura como referenciada
        if self.memoriaVirtual[self.index].getReferencia() == False:
            self.memoriaVirtual[self.index].setReferencia(True)
            self.memoriaVirtual[self.index].setEnd_memoria(self.index)
            self.fisica[self.index] = self.valor
            self.ponteiroTempo[self.index] = datetime.now()
            #Atualiza marcação de tempo relacionado a memoria
            self.memoriaVirtual[self.index].setCounter(datetime.now())

        #Se a moldura estiver marcada como referenciada é preciso saber se ela ja foi modificada ou não
        elif self.memoriaVirtual[self.index].getReferencia() == True:

            #Essa parte é bem semelhante a primeira escrita, mas com restrições envolvendo a memoria fisica
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
                self.index = self.substituicao.LRU(self.valor, self.antiga, self.ponteiroTempo)
                
        #Reporta ao log
        print("[MEMORIA] ESCRITA FEITA")

    #Metodo soft de leitura
    def operacaoLeitura(self, index):
        self.index = index
        self.end_Virtual = int(self.memoriaVirtual[self.index].getEnd_memoria())
        self.ponteiroTempo[self.end_Virtual] = datetime.now()
        print(f'[MEMÓRIA] Leitura de valor: {self.fisica[self.end_Virtual]}')
        