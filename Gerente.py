#Chamando todas as classes envolvidadas
from FabricaEntradas import FabricaEntradas
from Intermediador import Intermediador
from Memoria import Memoria
from Moderador import Moderador
import time

#classe de gerenciamento de Threads e importação de entradas para o SO
class Gerente:
    #Construtor
    def __init__(self):
        #Instancia um novo objeto para criar a entrada
        self.fabrica = FabricaEntradas(30)

    #Metodo para chamar a entrada da Fabrica de entradas
    def recebeEntrada(self):
        self.entrada = self.fabrica.getEntrada()
        print("[GERENTE] Entrada recebida!\nENTRADA:")
        
        for i in range(len(self.entrada)):
            print(f'| {self.entrada[i]: <6} |')

        print("\n")
            
    #Metodo para ligar o Sistema Operacional
    def ligaSO(self):
        print("[GERENTE] Iniciando SO")
        print("[GERENTE] Iniciando memória")
        #Instancia uma interface de memoria
        self.memoria = Memoria()
        self.memoria.iniciaMemorias()
        #memoria.mostraPaginacao()
        time.sleep(2)
        print("[GERENTE] Memória iniciada")

    #Metodo para iniciar as Threads que irão receber as entradas e moderação
    def iniciaProcessamento(self):
        #Instancia um novo moderador, o moderador irá realizar verificações pertinentes
        moderacao = Moderador(self.entrada)

        #Serão 3 Threads, o primeiro parametro é a identificação da Thread os demais são o mesmo objeto de moderação e memoria que precisa ser compartilhado entre as threads
        intermedia_1 = Intermediador(1, moderacao, self.memoria)
        intermedia_1.start()
        intermedia_2 = Intermediador(2, moderacao, self.memoria)
        intermedia_2.start()
        intermedia_3 = Intermediador(3, moderacao, self.memoria)
        intermedia_3.start()
        

