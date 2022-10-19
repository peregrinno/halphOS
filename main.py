from Gerente import Gerente

entrada = ['4-R', '5-R', '10-W-7','4-W-2', '1-R', '5-W-4', '2-R', '2-W-6']

for i in range(len(entrada)):
    ent = entrada[i].split("-")
    if ent[1] == "R":
        endereco = ent[0]
        tipo = ent[1]
        print(endereco, tipo)
    else:
        endereco = ent[0]
        tipo = ent[1]
        valor = ent[2]
        print(endereco, tipo, valor)

gerencia = Gerente(entrada)