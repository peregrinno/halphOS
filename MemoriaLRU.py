import time, random


def iniciaMemoria(HD, TAM_HD, TAM_memoriaFisica, TAM_memoriaVirtual, memoriaFisica, memoriaVirtual):
    print('Iniciando memória, aguarde...')
    #Tratemos o espaço como uma lista com dois valores [Valor, Tamanho]
    # EX: ESPACO = [0,1]
    for i in range(TAM_HD):
        VALOR = random.randint(1,9)
        HD.append([i,VALOR])

    for i in range(TAM_memoriaFisica):
        memoriaFisica.append(['', 0])
        memoriaVirtual.append('')
        memoriaVirtual.append('')

        
    time.sleep(2)
    print('Memória operacional.')

def mostraMemoria(MEMORIA, memoriaFisica, memoriaVirtual):
    for i in range(len(MEMORIA)):
        print(f'Endereço: {i} Valor: {MEMORIA[i][1]}')
    print(f'Memória Fisica: {memoriaFisica} \nMemória Virtual: {memoriaVirtual}')


'''
def acessoMemoriaLRU(tipo, end, valor):
    if tipo == 'W':
        if memoriaFisica[end] == '':
            memoriaFisica[end] = valor
        else: 
       
''' 



    