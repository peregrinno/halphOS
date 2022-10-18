class paginaVirtual:
    def __init__(self, counter, modificado, presenca, referencia, end_memoria):
        self.counter = counter
        self.modificado = modificado
        self.presenca = presenca
        self.referencia = referencia
        self.end_memoria = end_memoria

    def getCounter(self):
        return self.counter

    def setCounter(self, num):
        self.counter = num

    def getModificado(self):
        return self.modificado

    def setModificado(self, mod):
        self.modificado = mod
      
    def getPresenca(self):
        return self.presenca

    def setPresenca(self, pres):
        self.presenca = pres

    def getReferencia(self):
        return self.referencia

    def setReferencia(self,ref):
        self.referencia = ref
      
    def getEnd_memoria(self):
        return self.end_memoria

    def setEnd_memoria(self, endereco):
        self.end_memoria = endereco
