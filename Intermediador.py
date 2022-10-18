import threading 
import time

class Intermediador:

    def __init__ (self, num):
        self.lock = threading.Lock()
        self.num = num    

    def run(self, ent):
        while True:
            
            if len(ent) > 1:
                self.lock.acquire()
                time.sleep(1)
                print (f'Intermediador {self.num} iniciado')
                self.entrada = ent[0].split("-")
                self.paginaAtual = ent[0]
                del(ent[0])
                
                self.endereco = self.entrada[0]
                self.tipo = self.entrada[1]
                if self.tipo == "R":
                    print(f'[INTERMEDIADOR] #{self.num} : PEGOU A ENTRADA [{self.paginaAtual}] - ENDEREÇO: {self.endereco} | TIPO: LEITURA')
                else:
                    self.valor = self.entrada[2]
                    print(f'[INTERMEDIADOR] #{self.num} : PEGOU A ENTRADA [{self.paginaAtual}] - ENDEREÇO: {self.endereco} | TIPO: ESCRITA | VALOR: {self.valor}')
                self.lock.release()
