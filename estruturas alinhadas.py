minutos=int(input("Quantos minutos voce ultilizou este mes:"))
if minutos <200:
    preço = 0.20
    else:
    if minutos <400:
    preço = 0.18
    else:
    preço = 0.15
                
    print("Voce vai pagar este mes: R$6.2f" % (minutos * preço))