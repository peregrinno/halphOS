class paginaVirtual:
    def __init__(self, counter, modificado, presenca, referencia, end_memoria):
        self.counter = counter
        self.modificado = modificado
        self.presenca = presenca
        self.referencia = referencia
        self.end_memoria = end_memoria

    def getPagina(self):
        return paginaVirtual