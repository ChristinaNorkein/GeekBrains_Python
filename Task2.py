class Clothes:

    def __init__(self, atr):
        self.atr = atr


class Coat(Clothes):

    @property
    def consum(self):
        return f'Расход ткани на пальто - {self.atr / 63.5 + 0.5:.1f}'


class Suit(Clothes):

    @property
    def consum(self):
        return f'Расход ткани на костюм - {self.atr * 2  + 0.3}'


order_coat = Coat(48)
order_suit = Suit(172)

print(order_coat.consum)
print(order_suit.consum)
