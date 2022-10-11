import time

ultimosAcessados = [0,0,0,0,0,0,0,0,0,0]

def iniciaMemoria(MEMORIA):
    print('Iniciando memória, aguarde...')
    #Tratemos o espaço como uma lista com dois valores [Valor, Tamanho]
    # EX: ESPACO = [0,1]
    for i in range(500):
        ESPACO = 2*(i*2)
        MEMORIA.append(['0',ESPACO])

    time.sleep(2)
    print('Memória operacional.')

def mostraMemoria(MEMORIA):
    for i in range(len(MEMORIA)):
        TAM = MEMORIA[i][1]
        VL = MEMORIA[i][0]
        print(f'Endereço: {i+1} - Tamanho: {TAM} - Valor: {VL}')

def acessoMemoriaLRU(tipo, tam, ):
    