#TECNICA DE SUBSTITUIÇAÕ DE VALOR EM CASO DE FALTA DE PAGINA
class LRU:
    #Construtor que só faz a indicação ao log de que o LRU foi acionado
    def __init__(self):
        print("\n[LRU] MEMÓRIA CHEIA! LRU ACIONADO\n")
    
    #metodo que forma a tecnica LRU
    def LRU(self, valorNovo, valorAntigo, marcadoresTemporais):
        self.novo = valorNovo
        self.antigo = valorAntigo
        #marcador de tempo é uma lista de "datetimes" que é espelho da memoria fisica, ele determina qual for a memoria mais antiga a ser acessada
        self.tempos = marcadoresTemporais

        #Aqui é uma adaptação tecnia kkkk pra inicar um valor como o mais antigo, mas ainda não é o mais antigo de fato
        self.maisAntigo = self.tempos[0]

        #Esse laço sim, determina qual o endereço mais antigo onde o valor novo substituirá o valor antigo
        for i in range(len(self.tempos)):
            if self.maisAntigo > self.tempos[i]:
                self.indexer = i

        #Envia o valor antigo para o HD, nesse caso um arquvo txt
        HD = open("HD.txt","a")
        HD.write(f'{self.antigo}\n')
        HD.close()

        #reporta ao log o acontecimento
        print(f'[LRU] SUBSTITUIÇÃO FEITA | NOVO VALOR: {self.novo} - ANTIGO VALOR: {self.antigo} foi para o HD |    \n')

        #retorno valor novo a ser colcoado
        return self.novo
    