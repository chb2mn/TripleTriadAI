import random

class Player:
    def __init__(self, color, all_cards):
        self.positive = .5
        self.negative = .15
        self.cards = []
        self.original_cards = []
        self.color = color
        self.knowledge = [[{}, {}, {}],
                          [{}, {}, {}],
                          [{}, {}, {}]]
        for i in range(3):
            for j in range(3):
                for card in all_cards:
                    self.knowledge[i][j][card] = 0

    def draft(self, card):
        card.owner = self.color
        card.color = self.color
        self.cards.append(card)
        self.original_cards.append(card)

    def think(self, board):
        max_value = 0
        max_tuple = None
        for card in self.cards:
            for pos in board.remaining_moves:
                value = self.find_best(pos[0], pos[1], card, board)
                if value > max_value:
                    max_value = value
                    max_tuple = (pos[0], pos[1], card)
        if max_value >= 2:
            self.knowledge[max_tuple[0]][max_tuple[1]][max_tuple[2]] += self.positive * 2
        if max_value == 0:
            x = random.randint(0, 2)
            y = random.randint(0, 2)
            while not board.can_play(x, y):
                x = random.randint(0, 2)
                y = random.randint(0, 2)
            return x, y, self.cards[random.randint(0, len(self.cards)-1)]
        else:
            return max_tuple[0], max_tuple[1], max_tuple[2]

    #This method should be called at the end of the game so the AI can evaluate
    #  how well each card performed in the position in the position it was played
    def learn(self, board):
        for i in range(len(board.field)):
            for j in range(len(board.field[i])):
                card = board.field[i][j]
                if card.owner == self.color:
                    condition = 0
                    # leaving flexibility for more criteria e.g. # of cards this card flipped
                    if card.color != self.color:
                        condition += self.positive
                    else:
                        condition -= self.negative
                    self.knowledge[i][j][card] += condition

    def get_value(self, card, x, y):
        return self.knowledge[x][y][card]

    def find_best(self, x, y, card, board):
        greedy_val = 0
        plus_val = []
        plus_card = []
        same = []
        if y > 0:
            top = board.field[x][y-1]
            if top.color > 0 and top.owner != card.color: #If there is a card there
                if card.n > top.s: #Standard flip
                    top.color = card.owner
                    greedy_val += 1
                elif card.n == top.s:
                    same.append(top)
                plus_val.append(card.n + top.s)
                plus_card.append(top)

        if x > 0:
            left = board.field[x-1][y]
            if left.color > 0 and left.owner != card.color:
                if card.w > left.e:
                    left.color = card.owner
                    greedy_val += 1
                elif card.w == left.e:
                    same.append(left)
                plus_val.append(card.w + left.e)
                plus_card.append(left)

        if y < 2:
            bot = board.field[x][y+1]
            if bot.color > 0 and bot.owner != card.color:
                if card.s > bot.n:
                    bot.color = card.owner
                    greedy_val += 1
                elif card.s == bot.n:
                    same.append(bot)
                plus_val.append(card.s + bot.n)
                plus_card.append(bot)

        if x < 2:
            right = board.field[x+1][y]
            if right.color > 0 and right.color != card.owner:
                if card.e > right.w:
                    right.color = card.owner
                    greedy_val += 1
                #Special Flips
                elif card.e == right.w:
                    same.append(right)
                plus_val.append(card.e + right.w)
                plus_card.append(right)

        if len(same) > 1:
            for same_card in same:
                same_card.color = card.owner
                greedy_val += len(same)

        for i in range(len(plus_val)-1):
            if plus_val.count(plus_val[i]) > 1:
                plus_card[i].color = card.owner
                greedy_val += 1

        if greedy_val > 2:
            return greedy_val

        before = greedy_val
        # Use the knowledge we have about putting this card in this position
        greedy_val += self.get_value(card, x, y)

        """
        if 0 < greedy_val+5 < before:
            print "player {} has learned that it might not be a good idea to play {} at {}, {} (before: {}, w/ know: {})"\
                .format(self.color, card.name, x, y, before, greedy_val)
        """

        return greedy_val + -1 + 5*random.random()
