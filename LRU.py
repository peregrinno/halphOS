class LRU:
    def __init__(self):
        print("\n[LRU] MEMÓRIA CHEIA! LRU ACIONADO\n")
               
    def LRU(self, visaoFisica, valorNovo, valorAntigo, marcadoresTemporais):
        self.visaoFisica = visaoFisica
        self.novo = valorNovo
        self.antigo = valorAntigo
        self.tempos = marcadoresTemporais

        self.maisAntigo = self.tempos[0]
        
        for i in range(len(self.tempos)):
            if self.maisAntigo > self.tempos[i]:
                self.indexer = i


        HD = open("HD.txt","a")
        HD.write(f'{self.antigo}\n')
        HD.close()

        print(f'[LRU] SUBSTITUIÇÃO FEITA: NOVO VALOR: {self.novo} - ANTIGO VALOR: {self.antigo} foi para o HD    \n')
        
        return self.novo
    