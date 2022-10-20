class Moderador:
    def __init__(self, entrada):
        self.estado = "Liberado"
        self.entrada = entrada

    def proximo(self, solicitante):
        self.destino = solicitante
        self.instrucao = self.entrada[0]
        del(self.entrada[0])
        print(f'[MODERADOR] Enviando instrução [ {self.instrucao} ] para o intermediador [ {self.destino} ]')
        return self.instrucao

    def verificaOferta(self):
        if len(self.entrada) > 0:
            return True
        else:
            return False

    def verificaEstado(self):
        return self.estado

    def controlaDistribuicao(self, estado):
        self.estado = estado
        
        