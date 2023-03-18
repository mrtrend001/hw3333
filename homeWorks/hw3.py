class Bank:
    def __init__(self, name, balanse):
        self._name = name
        self._balanse = balanse

    def moneyX(self):
        ad = input(f'сколько добавишь к своим {self._balanse} введи сумму: ')
        print(self._balanse + int(ad))

    def _kill(self):
        if self._balanse > 0:
            print('теперь у тебя все наличкой')
            return self._balanse - self._balanse
        else:
            print('ты и так бомж, на счету нету денег')
            return self._balanse

    def __jackpot(self):
        self._balanse *= 10

    def get_jeckp(self):
        print(self.__jackpot())

    def _copyy(self, other):
        print(f'ваш сложенный баланс {self._balanse + other._balanse}\n'
              f'было{self._balanse}')


class GS(Bank):
    def __init__(self, name, balanse,):
        super().__init__(name, balanse)

    #сеттеры
    def name(self):
        return self._name

    def balance(self):
        return self._balanse

    #геттеры
    def name(self, a):
        self._name = a

    def balance(self, a):
        self._balanse = a


class Prop(Bank):
    def __init__(self, name, balanse):
        super().__init__(name, balanse)


    #проперти
    @property
    def gotname(self):
        return f'I\'m {self._name}'

    @property
    def gotbalanse(self):
        return f'balanse: {self._balanse}'


a = Prop("fdg", 200)
b = GS("ahmad", 12)
print(a.gotbalanse)
print(a.gotname)