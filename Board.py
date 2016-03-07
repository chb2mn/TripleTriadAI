from Card import Card

class Board:
    def __init__(self):
        self.field = [[Card(), Card(), Card()],[Card(), Card(), Card()],[Card(), Card(), Card()]]
        self.remaining_moves = [(0,0),(1,0),(2,0),
                                (0,1),(1,1),(2,1),
                                (0,2),(1,2),(2,2)]

    def __str__(self):
        return "|-----------||----------||----------|\n" \
               "|{}||{}||{}|\n" \
               "|Owner: {}\t||Owner: {}\t||Owner: {}\t|\n" \
               "|Color: {}\t||Color: {}\t||Color: {}\t|\n" \
               "|N: {}\t\t||N: {}\t\t||N: {}\t\t|\n" \
               "|E: {}\t\t||E: {}\t\t||E: {}\t\t|\n" \
               "|S: {}\t\t||S: {}\t\t||S: {}\t\t|\n" \
               "|W: {}\t\t||W: {}\t\t||W: {}\t\t|\n" \
               "|-----------||----------||----------|\n"\
               "|-----------||----------||----------|\n" \
               "|{}||{}||{}|\n" \
               "|Owner: {}\t||Owner: {}\t||Owner: {}\t|\n"\
               "|Color: {}\t||Color: {}\t||Color: {}\t|\n" \
               "|N: {}\t\t||N: {}\t\t||N: {}\t\t|\n" \
               "|E: {}\t\t||E: {}\t\t||E: {}\t\t|\n" \
               "|S: {}\t\t||S: {}\t\t||S: {}\t\t|\n" \
               "|W: {}\t\t||W: {}\t\t||W: {}\t\t|\n" \
               "|-----------||----------||----------|\n"\
               "|-----------||----------||----------|\n" \
               "|{}||{}||{}|\n" \
               "|Owner: {}\t||Owner: {}\t||Owner: {}\t|\n"\
               "|Color: {}\t||Color: {}\t||Color: {}\t|\n" \
               "|N: {}\t\t||N: {}\t\t||N: {}\t\t|\n" \
               "|E: {}\t\t||E: {}\t\t||E: {}\t\t|\n" \
               "|S: {}\t\t||S: {}\t\t||S: {}\t\t|\n" \
               "|W: {}\t\t||W: {}\t\t||W: {}\t\t|\n" \
               "|-----------||----------||----------|"\
                           "".format(
            self.field[0][0].name,  self.field[1][0].name,  self.field[2][0].name,
            self.field[0][0].owner, self.field[1][0].owner, self.field[2][0].owner,
            self.field[0][0].color, self.field[1][0].color, self.field[2][0].color,
            self.field[0][0].n,     self.field[1][0].n,     self.field[2][0].n,
            self.field[0][0].e,     self.field[1][0].e,     self.field[2][0].e,
            self.field[0][0].s,     self.field[1][0].s,     self.field[2][0].s,
            self.field[0][0].w,     self.field[1][0].w,     self.field[2][0].w,
            self.field[0][1].name,  self.field[1][1].name,  self.field[2][1].name,
            self.field[0][1].owner, self.field[1][1].owner, self.field[2][1].owner,
            self.field[0][1].color, self.field[1][1].color, self.field[2][1].color,
            self.field[0][1].n,     self.field[1][1].n,     self.field[2][1].n,
            self.field[0][1].e,     self.field[1][1].e,     self.field[2][1].e,
            self.field[0][1].s,     self.field[1][1].s,     self.field[2][1].s,
            self.field[0][1].w,     self.field[1][1].w,     self.field[2][1].w,
            self.field[0][2].name,  self.field[1][2].name,  self.field[2][2].name,
            self.field[0][2].owner, self.field[1][2].owner, self.field[2][2].owner,
            self.field[0][2].color, self.field[1][2].color, self.field[2][2].color,
            self.field[0][2].n,     self.field[1][2].n,     self.field[2][2].n,
            self.field[0][2].e,     self.field[1][2].e,     self.field[2][2].e,
            self.field[0][2].s,     self.field[1][2].s,     self.field[2][2].s,
            self.field[0][2].w,     self.field[1][2].w,     self.field[2][2].w,
            )

    def check_winner(self):
        p1 = 0
        p2 = 1 #p1 always goes first so p2 has an extra card in their hand
        for i in range(3):
            for j in range(3):
                if self.field[i][j].color==1:
                    p1 += 1
                else:
                    p2 += 1
        if p1 > p2:
            return 1
        elif p2 > p1:
            return 2
        else:
            return 0

    def clear(self):
        for i in range(3):
            for j in range(3):
                self.field[i][j]=Card()
        self.remaining_moves = [(0,0),(1,0),(2,0),
                                (0,1),(1,1),(2,1),
                                (0,2),(1,2),(2,2)]

    def can_play(self, x, y):
        if self.field[x][y].color == 0:
            return True
        else:
            return False

    def play(self, x, y, card):
        if self.field[x][y].color != 0:
            print "cannot play card at", x, y
            return False
        self.field[x][y] = card
        self.remaining_moves.remove((x,y))
        plus_val = []
        plus_pos = []
        same = []
        if y > 0:
            top = self.field[x][y-1]
            if top.color > 0 and top.owner != card.color: #If there is a card there
                if card.n > top.s: #Standard flip
                    top.color = card.owner
                elif card.n == top.s:
                    same.append((x,y-1))
                plus_val.append(card.n + top.s)
                plus_pos.append((x,y-1))

        if x > 0:
            left = self.field[x-1][y]
            if left.color > 0 and left.owner != card.color:
                if card.w > left.e:
                    left.color = card.owner
                elif card.w == left.e:
                    same.append((x-1,y))
                plus_val.append(card.w + left.e)
                plus_pos.append((x-1,y))

        if y < 2:
            bot = self.field[x][y+1]
            if bot.color > 0 and bot.owner != card.color:
                if card.s > bot.n:
                    bot.color = card.owner
                elif card.s == bot.n:
                    same.append((x,y+1))
                plus_val.append(card.s + bot.n)
                plus_pos.append((x,y+1))


        if x < 2:
            right = self.field[x+1][y]
            if right.color > 0 and right.color != card.owner:
                if card.e > right.w:
                    right.color = card.owner
                #Special Flips
                elif card.e == right.w:
                    same.append((x+1,y))
                plus_val.append(card.e + right.w)
                plus_pos.append((x+1,y))

        if len(same) > 1:
            for pos in same:
                #same_card.color = card.owner
                self.field[pos[0]][pos[1]].color = card.owner
                #print"--SAME APPLIED!!--"
                #print same

        for i in range(len(plus_val)):
            if plus_val.count(plus_val[i]) > 1:
                self.field[plus_pos[i][0]][plus_pos[i][1]].color = card.owner
                #print "--PLUS APPLIED!!--"
                #print plus_val
