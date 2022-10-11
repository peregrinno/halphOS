from Gerente import Gerente
import MemoriaLRU
import time

HD = []
TAM_HD = 50
memoriaFisica = [S]
TAM_memoriaFisica = TAM_HD // 10
memoriaVirtual = []
TAM_memoriaVirtual = TAM_memoriaFisica * 2

entrada = ['4-R', '5-R', '0-R','4-W-2', '1-R', '5-W-4', '2-R', '2-W-6']

print('Olá! Esse é o halphOS!')
time.sleep(1)
print('Vamos começar...')

MemoriaLRU.iniciaMemoria(HD, TAM_HD, TAM_memoriaFisica, TAM_memoriaVirtual, memoriaFisica, memoriaVirtual)
#MemoriaLRU.mostraMemoria(HD, memoriaFisica, memoriaVirtual)

#gerente = Gerente(entrada)


