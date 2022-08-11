import time

confirmacao = True
lula = 0
bolsonaro = 0
ciro = 0
branco = 0
nulo = 0

print("Bem - Vindo as eleições 2022\n")
time.sleep(2)
print("Seu voto é secreto, escolha seu candidato !\n")
time.sleep(1)
while confirmacao == True:
    try:
        voto = int(input("Candidatos concorrendo a presidência:\n"
                         "Ciro Gomes - 14\n"
                         "Lula - 13\n"
                         "Bolsonaro - 22\n"
                         "Branco - 0\n\n"
                         "Qual candidato deseja votar ?\n"))
        if voto == 14:
            print("Candidato Selecionado:\n\nCiro Gomes\n\n14\n")
        if voto == 13:
            print("Candidato Selecionado:\n\nLuis Inácio Lula da Silva\n\n13\n")
        if voto == 22:
            print("Candidato Selecionado:\n\nJair Messias Bolsonaro\n\n22\n")
        if voto == 0:
            print("Voto em Branco !")
        elif voto != 12 and voto != 13 and voto != 22 and voto != 0:
            print("Voto NULO !")
        confirmacaot = input('Deseja confirmar seu voto ?')
        confirmacaot = confirmacaot.upper()
        if confirmacaot == "SIM":
            if voto == 12:
                ciro += 1
            elif voto == 13:
                lula += 1
            elif voto == 22:
                bolsonaro += 1
            elif voto == 0:
                branco += 1
            elif voto != 12 and voto!= 13 and voto != 22 and voto != 0:
                nulo += 1
            print("PROCESSANDO SEU VOTO....")
            time.sleep(2)
            print('...')
            time.sleep(4)
            print('....')
            time.sleep(2)
            print("Voto confirmado com sucesso !")
            time.sleep(1)
            repete = input("Deseja continuar a votação ?\n")
            repete = repete.upper()
            if repete == "SIM":
                confirmacao = True
            elif repete == "NÃO":
                confirmacao = False

        else:
            confirmacao = True
            print("Escolha novamente seu candidato !\n")
    except ValueError:
        print("Somente números !\n")
        time.sleep(1)
        print("Tente Novamente\n")
        time.sleep(1)

    if nulo > lula and nulo > bolsonaro and nulo > ciro and nulo > branco:
        print("\nA eleição foi anulada, maioria voltou NULO !\n"
                "Segue os números da votação:\n\n"
                "Bolsonaro: " + str(bolsonaro) + "\nLula: " + str(lula) +
                "\nCiro: " + str(ciro) + "\nBranco: " + str(branco) + "\n"
                                                                   "Nulo: " + str(nulo))
    elif lula > nulo and lula > bolsonaro and lula > ciro and lula > branco:
        print("\nO novo presidente do Brasil é LULA  !\n"
                "Segue os números da votação:\n\n"
                "Bolsonaro: " + str(bolsonaro) + "\nLula: " + str(lula) +
                "\nCiro: " + str(ciro) + "\nBranco: " + str(branco) + "\n"
                                                                        "Nulo: " + str(nulo))
    elif bolsonaro > nulo and bolsonaro > lula and bolsonaro > ciro and bolsonaro > branco:
        print("\nO novo presidente do Brasil é Jair Messias Bolsonaro  !\n"
                "Segue os números da votação:\n\n"
                "Bolsonaro: " + str(bolsonaro) + "\nLula: " + str(lula) +
                "\nCiro: " + str(ciro) + "\nBranco: " + str(branco) + "\n"
                                                                        "Nulo: " + str(nulo))
    elif ciro > nulo and ciro > bolsonaro and ciro > lula and ciro > branco:
        print("\nO novo presidente do Brasil é Ciro Gomes  !\n"
                "Segue os números da votação:\n\n"
                "Bolsonaro: " + str(bolsonaro) + "\nLula: " + str(lula) +
                "\nCiro: " + str(ciro) + "\nBranco: " + str(branco) + "\n"
                                                                        "Nulo: " + str(nulo))
