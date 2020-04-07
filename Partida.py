from Escolha import Escolha
from Jogador import Jogador
from PosicionarFrota import Posicionar

def partida(player1, player2):

    #iniciação dos tabuleiros
    player1.preencherTabuleiro()
    player2.preencherTabuleiro()

    #posicionamento aleatorio dos navios
    tabuleiroP1 = player1.getposMatriz()
    tabuleiroP2 = player2.getposMatriz()

    # é necessario pegar toda frota de cada jogador e realizar tentativas (while) de posicionar 
    # essa embarcação no seu devido tabuleiro uma vez que uma embarcacao é posicionada a sua
    # posicao 
    Posicionar(player1, tabuleiroP1)



p1 = Jogador(Escolha(True), "bot")
p2 = Jogador(Escolha(True), "bot")

partida(p1, p2)