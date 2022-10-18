from Gerente import Gerente
import LRU
import time

memoriaVirtual = ["","","","","","","","","","","","","","","",""]
memoriaFisica = ["","","","","","","",""]

entrada = ['4-R', '5-R', '0-R','4-W-2', '1-R', '5-W-4', '2-R', '2-W-6']

print('Olá! Esse é o halphOS!')
time.sleep(1)
print('Vamos começar...')


gerente = Gerente(entrada)
time.sleep(1)
gerente.ligaSO(memoriaVirtual, memoriaFisica)
time.sleep(2)
gerente.iniciaProcesso()
time.sleep(2)
gerente.gerenciaProcessos()


