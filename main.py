from Gerente import Gerente
import MemoriaLRU
import time

MEMORIA = []
entrada = ['4-R', '5-R', '0-R','4-W-2', '1-R', '5-W-4', '2-R', '2-W-6']

print('Olá! Esse é o halphOS!')
time.sleep(1)
print('Vamos começar...')

MemoriaLRU.iniciaMemoria(MEMORIA)
#MemoriaLRU.mostraMemoria(MEMORIA)

#gerente = Gerente(entrada)


