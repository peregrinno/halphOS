'''
Esse é o halphOS - Um Sistema Operacional arquitetado em python usando o paradigma orientado a objetos.

++++ Sistemas Operacionais ++++ 
+  Universidade de Pernambuco +
+  Profº Jorge Fonseca        +
+        Projeto Final        +
+++++++++++++++++++++++++++++++

####### SQUAD #######
# Luan Araujo       #
# Anna Beatriz      #
# Henrique Medeiros #
# Hydelbranda Melo  # <-> Foi de base
#    5º P - UPE     #
#####################
'''

#Vamos primeiramente chamar a classe Gerente para a main.py
from Gerente import Gerente


#Instanciando um novo objeto gerente
gerencia = Gerente()

#O gerente liga o sistema operacional
gerencia.ligaSO()

#O gerente "invoca" uma nova entrada de dados para ser processada
gerencia.recebeEntrada()

#O gerente pega a entrada criada e inicia o processamento de leitura e escrita
gerencia.iniciaProcessamento()

