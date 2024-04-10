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
        if Televisao.mudo == False:
            Televisao.mudo = True
        else:
            Televisao.mudo = False

    def trocarCanal(self, canalDesejado):
        Televisao.canal = canalDesejado

    def mudarVolume(self, novoVolume):
        Televisao.volume = novoVolume

    def informacoes(self):
        if Televisao.mudo == False:
            print("Canal", Televisao.canal, "//", "Volume",
                  Televisao.volume, "//", "mudo off")
        else:
            print("Canal", Televisao.canal, "//", "Volume",
                  Televisao.volume, "//", "mudo on")


Televisao.__init__(Televisao, 26, 2, False, False, str)
print(Televisao.botaoLigarDesligar)
Televisao.ligarDesligarTv(Televisao)
print(Televisao.botaoLigarDesligar)
print(Televisao.canal)
Televisao.trocarCanal(Televisao, 52)
print(Televisao.canal)
print(Televisao.volume)
Televisao.mudarVolume(Televisao, 50)
print(Televisao.volume)
Televisao.informacoes(Televisao)
