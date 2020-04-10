from PosicionarFrota import tabVisivel

class Jogador:
    def __init__(self, frota, tipo = "player"):
        self.__frota = frota
        self.__nFrota = countFrota(self, self.__frota)
        self.__posMatriz = []   # matriz usada para posicionamento
        self.__tabuleiro = []   # matriz usada internamente no jogo
        self.__tab = ""
        self.__tipo = tipo      # bot ou player

    def getFrota(self):
        return self.__frota

    def getNFrota(self):
        return self.__nFrota

    def getTabuleiro(self):
        return self.__tabuleiro

    def getposMatriz(self):
        return self.__posMatriz

    def getTab(self):
        return self.__tab
    
    def updateFrota(self):
        """ Remove uma embarcação da frota """
        self.__nFrota -= 1

    def setTab(self, tab):
        self.__tab = tab

    def updateTabuleiro(self, coluna, linha, dado):
        self.__tabuleiro[coluna][linha] = dado
        self.setTab(tabVisivel(self, self.__tabuleiro))

    def preencherTabuleiro(self):
        for _ in range(10):
            self.__tabuleiro.append(["     "] * 10)
            self.__posMatriz.append([False] * 10)

def countFrota(jogador, frota):
    frotaTotal = 0
    for tipo in frota:
        for _ in range(len(frota[tipo])):            
            frotaTotal += 1
    return frotaTotal

