class Televisao:
    volume = 20
    canal = 1
    botaoLigarDesligar = False
    botaoMudo = False

    def __init__(self, volume, canal, botaoLigarDesligar, botaoMudo):
        self.volume = volume
        self.canal = canal
        self.botaoLigarDesligar = botaoLigarDesligar
        self.botaoMudo = botaoMudo

    def ligarDesligarTv(self):
        if Televisao.botaoLigarDesligar == False:
            Televisao.botaoLigarDesligar = True
        else:
            Televisao.botaoLigarDesligar = False

    def mutar(self):
        if Televisao.botaoLigarDesligar == True:
            if Televisao.botaoMudo == False:
                Televisao.botaoMudo = True
            else:
                Televisao.botaoMudo = False
        else:
            print("TV desligada")

    def trocarCanal(self, canalDesejado):
        if Televisao.botaoLigarDesligar == True:
            Televisao.canal = canalDesejado
        else:
            print("TV desligada")

    def mudarVolume(self, novoVolume):
        if Televisao.botaoLigarDesligar == True:
            Televisao.volume = novoVolume
        else:
            print("TV desligada")

    def informacoes(self):
        if Televisao.botaoLigarDesligar == True:
            if Televisao.botaoMudo == False:
                print("Canal", Televisao.canal, "//", "Volume",
                      Televisao.volume, "//", "mudo off")
            else:
                print("Canal", Televisao.canal, "//", "Volume",
                      Televisao.volume, "//", "mudo on")
        else:
            print("TV desligada")


Televisao.__init__(Televisao, 26, 2, False, False)
# print(Televisao.botaoLigarDesligar)
# Televisao.ligarDesligarTv(Televisao)
# print(Televisao.botaoLigarDesligar)
# print(Televisao.canal)
# Televisao.trocarCanal(Televisao, 52)
# print(Televisao.canal)
# print(Televisao.volume)
# Televisao.mudarVolume(Televisao, 50)
# print(Televisao.volume)
# Televisao.informacoes(Televisao)
# Televisao.ligarDesligarTv(Televisao)
# print(Televisao.canal)
# Televisao.trocarCanal(Televisao, 15)
# print(Televisao.canal)
