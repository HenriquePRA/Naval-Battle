from Escolha import Escolha
from Jogador import Jogador
from random import randint
from PosicionarFrota import Posicionar
from Embarcacao import Embarcacao

def partida(player1, player2):

    #iniciação dos tabuleiros
    player1.preencherTabuleiro()
    player2.preencherTabuleiro()

    
    tabuleiroP1 = player1.getposMatriz()
    tabuleiroP2 = player2.getposMatriz()

    #posicionamento em local aleatorio da frota
    Posicionar(player1, tabuleiroP1)
    Posicionar(player2, tabuleiroP2)

    #tabuleiro convertido para string usado no jogo
    # player1.setTab(tabVisivel(tabuleiroP1))
    # player2.setTab(tabVisivel(tabuleiroP2))


    partida = True    
    jogador_da_vez = caraCoroa(player1, player2)
    print("\nA Batalha Começa !")
    while partida:

        print("\nO próximo a jogar é:\n")
        if jogador_da_vez == player1:
            alvo = player2
            print("Player 1")
        else:
            alvo = player1
            print("Player 2")
        
        print('\n[1] = Atacar\n[2] = Pausar\n')
        op = input(">> ")
        try:
            op = int(op)
            assert op in [1,2]
        except AssertionError:
            print("\nOpção inválida !\n")
        except ValueError:
            print("\nOs valores informados devem estar entre 1 e 2 !\nTente novamente.\n")


        if  op == 1:
            print("                          Tabuleiro do alvo                       "+ alvo.getTab())
            print("\nInforme entre 0 e 9:\n")
            col = input("Linha >> ")
            lin = input("Coluna >> ")
            try:
                #estado da jogada caso a opção seja a 1
                proximoJogador = True


                col, lin = int(col), int(lin)
                assert (lin >= 0 and lin <= 9) and (col >= 0 and col <= 9)
                local = alvo.getTabuleiro()[col][lin]
                if type(local) == Embarcacao:
                    
                    if [col, lin] in local.getPosicoes():
                        local.removePosicao([col, lin])
                        local.setAtkRecebido()
                        alvo.updateTabuleiro(col, lin, "  X  ")
                        proximoJogador = False
                        print("\nFogo !\n")
                        print("                          Tabuleiro do alvo                       "+ alvo.getTab())
                else:
                    alvo.updateTabuleiro(col, lin, "-.|-")
                    print("\nÁgua !")

                if proximoJogador:
                    #Caso o jogador não acerte, a vez é do proximo
                    temp = jogador_da_vez
                    jogador_da_vez = alvo
                    alvo = temp                    
                


            except AssertionError:
                print("\nColuna ou linha inválidas !\n")
            except ValueError:
                print("\nOs valores informados devem estar entre 0 e 9 !\nTente novamente.")
        else:
            partida = False
            # aqui vai ficar a função de salvamento


def caraCoroa(player1, player2):
    if randint(0, 1) ==  0:
        return player1
    else:
        return player2
