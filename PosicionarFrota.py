from random import randint

def Posicionar(player, tabuleiro):
    for tipo in player.getFrota():
        for embarcacao in player.getFrota()[tipo]:
            while embarcacao.getPosicionado() == False:
                localinicial = randint(0, (len(tabuleiro) * len(tabuleiro[0]) - 1))
                tamanhoEmbarcacao = embarcacao.getTamanho()
                orientacao = 0 #randint(0, 1)

                #posicionamento da embarcação é vertical
                if orientacao == 0:
                    # variaveis que receberão todos os locais afetados pelo posicionamento da embarcacao
                    cord_menos, cord, cord_mais, pontas = [],[],[],[]
                    if (((localinicial + ((tamanhoEmbarcacao) * 10)) > 99)):
                        cord_menos, cord, cord_mais, pontas = gerarPosicoes(tamanhoEmbarcacao,  localinicial, "baixo-cima")

                    else:
                        cord_menos, cord, cord_mais, pontas = gerarPosicoes(tamanhoEmbarcacao,  localinicial, "cima-baixo")

                    #checa se existe algum True no tabuleiro (indicando que o local para o posicionamento é inadequado)
                    checkresult = checagem(cord_menos, cord, cord_mais, pontas, tabuleiro)
                    if checkresult:
                        insertMatriz(cord_menos, cord, cord_mais, pontas, tabuleiro)
                        insertGameMatriz(cord, player, embarcacao)
                        embarcacao.setPosicionado(True)

                #posicionamento da embarcação é horizontal
                elif orientacao == 1:
                    cord_menos, cord, cord_mais, pontas = [],[],[],[]

def gerarPosicoes(tamanhoEmbarcacao, localinicial, sentido):
    """ Função que retorna todas as cordenadas que podem estar em uso caso já exista uma embarcação
    a partir de uma detarminada posição, sentido e tamanho de embarcação. """

    cord_menos = []
    cord = []
    cord_mais = []
    pontas = []

    for i in range(0, tamanhoEmbarcacao):
        temp_cord_menos = []
        temp_cord = []
        temp_cord_mais = []

        if sentido == "baixo-cima":
            if ((localinicial % 10) != 0): 
                for item in list(str(localinicial + (10*(-i)) - 1)):
                    temp_cord_menos.append(int(item))

            for item in list(str(localinicial + (10*(-i)))):
                temp_cord.append(int(item))

            if list(str(localinicial))[1] != "9":
                for item in list(str(localinicial + (10*(-i)) + 1)):
                    temp_cord_mais.append(int(item))

        elif sentido == "cima-baixo":
            t = list(str(localinicial + (10*(+i)) - 1))
            if len(t) == 1:
                t.insert(0, 0)
            if localinicial != 0 and ((localinicial % 10) != 0):
                for item in t:
                    temp_cord_menos.append(int(item))
            
            t = list(str(localinicial + (10*(+i))))
            if len(t) == 1:
                t.insert(0, 0)
            for item in t:
                temp_cord.append(int(item))

            t = list(str(localinicial + (10*(+i)) + 1))
            if len(t) == 1:
                t.insert(0, 0)
                if localinicial != 9:
                    for item in t:
                        temp_cord_mais.append(int(item))
            elif len(t) > 1 and temp_cord[1] != 9:
                for item in t:
                    temp_cord_mais.append(int(item))
        
        if temp_cord_menos != []:
            cord_menos.append(temp_cord_menos)
        if temp_cord != []:
            cord.append(temp_cord)
        if temp_cord_mais != []:
            cord_mais.append(temp_cord_mais)

    if sentido == "cima-baixo":
        if cord[0][0] != 0 :
            pontas.append([cord[0][0] - 1, cord[0][1]])
        pontas.append([tamanhoEmbarcacao + cord[0][0], cord[0][1]])
    if sentido == "baixo-cima":
        if cord[0][0] != 9:
            pontas.append([cord[0][0] + 1, cord[0][1]])
        pontas.append([cord[0][0] - tamanhoEmbarcacao, cord[0][1]])

    return cord_menos, cord, cord_mais, pontas


def checagem(cord_menos, cord, cord_mais, pontas, tabuleiro):
    """ Recebe um grupo de coordenadas e um tabuleiro, transfere todos os dados do tabuleiro 
    referente as coordenadas para um vetor, todas as posições vazias devem ter False, caso
    não encontre algum item no vetor igual a True retorna False indicando que todas as pos """

    truecheck = []
    for item in cord_menos:
        truecheck.append(tabuleiro[item[0]][item[1]])
    for item in cord:
        truecheck.append(tabuleiro[item[0]][item[1]])
    for item in cord_mais:
        truecheck.append(tabuleiro[item[0]][item[1]])
    for item in pontas:
        truecheck.append(tabuleiro[item[0]][item[1]])
    if not(True in truecheck):
        return True
    return False


def insertMatriz(cord_menos, cord, cord_mais, pontas, tabuleiro):
    """ Recebe um tabuleiro e um grupo de coordenadas existentes nesse tabuleiro, nas posições
    das coordenadas marca como True informando que ali há é espaço ocupado por uma embarcação.  """

    for item in cord_menos:
        tabuleiro[item[0]][item[1]] = True
    for item in cord:
        tabuleiro[item[0]][item[1]] = True
    for item in cord_mais:
        tabuleiro[item[0]][item[1]] = True
    for item in pontas:
        tabuleiro[item[0]][item[1]] = True


def insertGameMatriz(cord, player, embarcacao):
    """ Insere uma embarcação no tabuleiro visível ao jogador, fazendo com que os locais onde está a embarcação
    referenciem a mesma."""
    try:
        assert embarcacao.getPosicionado() == False
        for item in cord:
            player.updateTabuleiro(item[0], item[1], " * ")
    except AssertionError:
        print("Aviso: Erro ao posicionar a embarvação")
