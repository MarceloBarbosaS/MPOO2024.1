class Televisao:
    volume = 25
    canal = 1
    botaoLigarDesligar = False
    mudo = False
    info = str

    def __init__(self, volume, canal, botaoLigarDesligar, mudo, info):
        self.volume = volume
        self.canal = canal
        self.botaoLigarDesligar = botaoLigarDesligar
        self.mudo = mudo
        self.info = info

    def ligarDesligarTv(self):
        if Televisao.botaoLigarDesligar == False:
            Televisao.botaoLigarDesligar = True
        else:
            Televisao.botaoLigarDesligar = False

    def mutar(self):
        if Televisao.botaoLigarDesligar == True:
            if Televisao.mudo == False:
                Televisao.mudo = True
            else:
                Televisao.mudo = False
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
            if Televisao.mudo == False:
                print("Canal", Televisao.canal, "//", "Volume",
                      Televisao.volume, "//", "mudo off")
            else:
                print("Canal", Televisao.canal, "//", "Volume",
                      Televisao.volume, "//", "mudo on")
        else:
            print("TV desligada")


Televisao.__init__(Televisao, 26, 2, False, False, str)
# print(Televisao.botaoLigarDesligar)
# # Televisao.ligarDesligarTv(Televisao)
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
