"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
    Если цифра есть на карточке - она зачеркивается и игра продолжается.
    Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
    Если цифра есть на карточке - игрок проигрывает и игра завершается.
    Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87
      16 49    55 77    88
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""

import random
import sys


class Bag:
    amount = 90

    def __init__(self):
        self.gen = self.get()

    def get(self):
        lst = [x for x in range(1, self.amount + 1)]
        random.shuffle(lst)
        for i, y in enumerate(lst):
            print('{:*^30}'.format('*'))
            print(f"Новый бочонок: {y} (осталось {self.amount - (i + 1)})")
            yield y


class Cart:
    amount = 2

    def __init__(self):
        row = 3
        self.all_row = row * self.amount
        self.__set_card()

    def __set_card(self):
        num = set()
        while len(num) < self.all_row * 5:
            num.add(random.randint(1, 91))
        cards = list(num)
        random.shuffle(cards)

        while len(cards) % self.all_row != 0:
            cards.append('None')
        self.all_row = int(len(cards) / self.all_row)
        cards = [cards[i: i + self.all_row] for i in range(0, len(cards), self.all_row)]

        for i in range(len(cards)):
            cards[i].sort()
        self.card_user = cards[:3]
        self.card_comp = cards[3:]

    def get_card(self, card_player):
        print(f"{self.name:-^25}")

        print('{0[0]:>2} {0[1]:<5} {0[2]:<8} {0[3]:>5} {0[4]} '.format(card_player[0]))
        print('{0[0]:>5} {0[1]:<6} {0[2]:<4} {0[3]:<5} {0[4]} '.format(card_player[1]))
        print('{0[0]:>1} {0[1]:<6} {0[2]:<6} {0[3]:<6} {0[4]} '.format(card_player[2]))

        print('{: ^25}'.format(' '))

    def search(self, card_player, num_cask):
        for i, n in enumerate(card_player):
            if num_cask in n:
                card_player[i][n.index(num_cask)] = '-'
                self.score += 1
                if self.score == 15:
                    print(f"{self.name} Победила!")
                    sys.exit(1)
                return True
        return False


class Player(Cart):

    def __init__(self, name):
        self.name = name
        self.score = 0


class Game:

    @staticmethod
    def start():
        cart = Cart()
        bag = Bag()
        player = Player('Карточка игрока')
        computer = Player('Карточка компьютера')

        while True:
            num_bag = next(bag.gen)
            player.get_card(cart.card_user)
            computer.get_card(cart.card_comp)

            inp_user = input('Зачеркнуть цифру? (y/n)')

            if inp_user != 'n' and inp_user != 'y':
                print('Введите y or n')
                continue

            if inp_user == 'y':
                if player.search(cart.card_user, num_bag):
                    continue
                else:
                    print('Game Over')
                    sys.exit(1)
            if inp_user == 'n':
                if player.search(cart.card_user, num_bag):
                    print('Game Over')
                    sys.exit(1)
                elif computer.search(cart.card_comp, num_bag):
                    continue


# Запускаем игру
Game.start()
