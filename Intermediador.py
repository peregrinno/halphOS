from threading import Thread
import threading
import time

class Intermediador(Thread):
    def __init__ (self, num, moderacao, memoria):
        Thread.__init__(self)
        self.lock = threading.Lock()
        self.num = num
        self.moderacao = moderacao
        self.memoria = memoria

    def run(self):
        print(f'[INTERMEDIADOR] Intermediador #{self.num} iniciado.')
        while True:
            if self.moderacao.verificaOferta() == True:
                if self.moderacao.verificaEstado() == "Liberado":
                    self.moderacao.controlaDistribuicao("Bloqueado")
                    self.instrucao = self.moderacao.proximo(self.num).split("-")
                    #BLOCO DE USO DA MEMORIA
                    if self.instrucao[1] == "W":
                        self.endereco = int(self.instrucao[0])
                        self.tipo = self.instrucao[1]
                        self.valor = self.instrucao[2]
                        print(f'[INTERMEDIADOR] Intermediador #{self.num} recebeu a instrução {self.instrucao}. ENDERECO: {self.endereco} - TIPO: {self.tipo} - VALOR: {self.valor}')
                        self.memoria.operacaoEscrita(self.endereco, self.valor)
                    else:
                        self.endereco = int(self.instrucao[0])
                        self.tipo = self.instrucao[1]
                        print(f'[INTERMEDIADOR] Intermediador #{self.num} recebeu a instrução {self.instrucao}. ENDERECO: {self.endereco} - TIPO: {self.tipo}')
                        self.memoria.operacaoLeitura(self.endereco)
                        
                    #FIM DO BLOCO DE USO DA MEMORIA
                    self.moderacao.controlaDistribuicao("Liberado")
                else:
                    print(f'[INTERMEDIADOR] Controle de entrada está bloqueando o Intermediador #{self.num}')
            else:
                break
            time.sleep(1)
