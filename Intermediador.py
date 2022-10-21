#Importanto a biblioteca thread para simular uma thread
from threading import Thread
import time

#Classe Thread de intermediação, ela ira pegar uma entrada e manipular ela na região critica.
class Intermediador(Thread):
    #Construtor, chamamos a identificação da Thread, o objeto moderador e memoria que ja foram instanciados.
    def __init__ (self, num, moderacao, memoria):
        Thread.__init__(self)
        self.num = num
        self.moderacao = moderacao
        self.memoria = memoria

    #Metodo de contrução da Thread
    def run(self):
        print(f'[INTERMEDIADOR] Intermediador #{self.num} iniciado.')
        #Laço de procecssamento de entradas dentro da Thread
        while True:
            #Obviamente, não existe processamento sem oferta de entradas, logo, é preciso uma condicional que diga se ainda existem entradas para serem processadas.
            if self.moderacao.verificaOferta() == True:
                #Existindo entradas, é preciso saber se o acessoa a memoria esta liberado para a manipulação
                if self.moderacao.verificaEstado() == "Liberado":
                    #Estando liberando, a thread bloquea o acesso para que exista controle de concorrencia
                    self.moderacao.controlaDistribuicao("Bloqueado")
                    #Esse comando pega a lista de entradas criadas, tira uma entrada para se tornar a proxima instrução e simultaneamente apaga essa entrada das lista de entradas, ja que ela será processada. 
                    #self.instrução recebe a entrada assim: ['<ENDEREÇÕ>','<TIPO>','<VALOR>'(SE FOR ESCRITA)]
                    self.instrucao = self.moderacao.proximo(self.num).split("-")
                    #BLOCO DE USO DA MEMORIA - REGIAO CRITICA!!!
                    #Primeiro se olha para o tipo da entrada, pra saber se será de leitura ou de escrita
                    if self.instrucao[1] == "W":
                        #Sendo de escrita, faz sentido olhar para o indice [2] de self.instrucao já que a mesma só existe se for escrita 
                        self.endereco = int(self.instrucao[0])
                        self.tipo = self.instrucao[1]
                        self.valor = self.instrucao[2]
                        #Mostra no log o que esta acontecento
                        print(f'[INTERMEDIADOR] Intermediador #{self.num} recebeu a instrução {self.instrucao}. ENDERECO: {self.endereco} - TIPO: {self.tipo} - VALOR: {self.valor}')
                        #CHAMADA CAVERNOSA DE ESCRITA NA MEMORIA ◕‿◕ ◕‿◕ ◕‿◕ ◕‿◕ - só envia o endereço que haverá a escrita e o valor
                        self.memoria.operacaoEscrita(self.endereco, self.valor)
                    else:
                        #Essa parte é de leitura, é bem mais simples então não precisamos explicar muito
                        self.endereco = int(self.instrucao[0])
                        self.tipo = self.instrucao[1]
                        print(f'[INTERMEDIADOR] Intermediador #{self.num} recebeu a instrução {self.instrucao}. ENDERECO: {self.endereco} - TIPO: {self.tipo}')
                        self.memoria.operacaoLeitura(self.endereco)
                        
                    #FIM DO BLOCO DE USO DA MEMORIA - REGIAO CRITICA!!!
                    #Usada a memoria, mandamos o sinal de liberação para as demais Threads
                    self.moderacao.controlaDistribuicao("Liberado")
                else:
                    #Caso a memoria esteja sendo usada por outra thread, apenas essa sinal é disparado e a thread fica em loop até encontrar a memoria liberada
                    print(f'[INTERMEDIADOR] Controle de entrada está bloqueando o Intermediador #{self.num}')
            else:
                break
            time.sleep(1)
