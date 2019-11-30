import random

class Cards:

    def __init__(self):
        self.piki = ['A','2','3','4','5','6','7','8','9','1', 'J', 'Q', 'K']
        self.bubi = ['A','2','3','4','5','6','7','8','9','1', 'J', 'Q', 'K']
        self.chervi = ['A','2','3','4','5','6','7','8','9','1', 'J', 'Q', 'K']
        self.kresti = ['A','2','3','4','5','6','7','8','9','1', 'J', 'Q', 'K']
        self.koloda = self.piki + self.bubi + self.chervi + self.kresti


class Deck_of_Cards(Cards):

    def __init__(self):
        Cards.__init__(self)
        self.mast = ''
        self.karta = ''

    def deal(self, mast, karta):
        
        # print('hi')
        if mast == 'kresti':
            self.kresti.remove(karta)
            self.koloda = self.piki + self.bubi + self.chervi + self.kresti

        elif mast == 'bubi':   
            self.bubi.remove(karta)
            self.koloda = self.piki + self.bubi + self.chervi + self.kresti

        elif mast == 'chervi':
            print(karta)
            self.chervi.remove(karta)
            self.koloda = self.piki + self.bubi + self.chervi + self.kresti

        else:
            self.piki.remove(karta)
            self.koloda = self.piki + self.bubi + self.chervi + self.kresti
    
    def mix(self):

        self.koloda = random.shuffle(self.koloda)
        return self.koloda





    #     return mix

    # def mix():
    #     pass



        


karty = Deck_of_Cards()
karty.deal(input('Kакая Масть(ВЫберите из: piki, bubi, kresti, chervi):  '), input('Kакая карта: '))
karty.deal(input('Kакая Масть(ВЫберите из: piki, bubi, kresti, chervi):  '), input('Kакая карта: '))
karty.deal(input('Kакая Масть(ВЫберите из: piki, bubi, kresti, chervi):  '), input('Kакая карта: '))
karty.deal(input('Kакая Масть(ВЫберите из: piki, bubi, kresti, chervi):  '), input('Kакая карта: '))
karty.mix()