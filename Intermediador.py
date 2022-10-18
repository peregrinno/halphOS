import threading 
import time


class Intermediador:

    def __init__ (self, num):
        threading.Thread.__init__(self)
        threading.Condition.__init__(self)
        self.lock = threading.Lock()
        self.num = num    

    def run(self, ent, paginas):
        print (f'Intermediador {self.num} iniciado')
        while True:
            if len(ent) > 1:
                time.sleep(1)
                self.entrada = ent[0].split("-")
                self.paginaAtual = ent[0]
                del(ent[0])
                
                self.endereco = self.entrada[0]
                self.tipo = self.entrada[1]
                
                if self.tipo == "R":
                    print(f'[INTERMEDIADOR] #{self.num } : PEGOU A ENTRADA [{self.paginaAtual :>6}] - ENDEREÇO: {self.endereco :>2} | TIPO: LEITURA')
                else:
                    self.valor = self.entrada[2]
                    print(f'[INTERMEDIADOR] #{self.num} : PEGOU A ENTRADA [{self.paginaAtual :>6}] - ENDEREÇO: {self.endereco :>2} | TIPO: ESCRITA | VALOR: {self.valor}')

            
