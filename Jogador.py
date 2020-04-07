
class Jogador:
    def __init__(self, frota, tipo = "player"):
        self.__frota = frota
        self.__posMatriz = []   # matriz usado para posicionamento
        self.__tabuleiro = []   # matriz usado para exibição do jogo
        self.__tipo = tipo      # bot ou player

    def getFrota(self):
        return self.__frota

    def getTabuleiro(self):
        return self.__tabuleiro

    def getposMatriz(self):
        return self.__posMatriz

    def updateTabuleiro(self, coluna, linha, dado):
        self.__tabuleiro[coluna][linha] = dado

    def preencherTabuleiro(self):
        for _ in range(10):
            self.__tabuleiro.append(["   "] * 10)
            self.__posMatriz.append([False] * 10)