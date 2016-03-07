import random
from Board import Board
from Player import Player
from Card import Card



def play_game(player1, player2, board):
    for i in range(5):
        a = random.randint(0,len(CARD_BANK_1)-1)
        player1.draft(CARD_BANK_1[a])
        a = random.randint(0,len(CARD_BANK_2)-1)
        player2.draft(CARD_BANK_2[a])
    for card in player1.cards:
        pass

    for card in player2.cards:
        pass

    for i in range(4):
        #print "player 1 thinking..."
        x, y, card = player1.think(board)
        board.play(x, y, card)
        player1.cards.remove(card)
        #print "player 2 thinking..."
        x, y, card = player2.think(board)
        board.play(x, y, card)
        player2.cards.remove(card)
        #print board
        #print "========={}{}{}{}{}{}{}{}{}{}==========".format(i,i,i,i,i,i,i,i,i,i)
    #Final Move
    x, y, card = player1.think(board)
    board.play(x, y, card)
    #print board
    #print "=============44444444444444444============"
    result = board.check_winner()
    p1.learn(board)
    p2.learn(board)
    #print "player {} wins!".format(result)
    return result




def count_cards(bank, pnum, rep):
    rep += 1
    print "counting_cards", rep
    p1_len = 0
    p2_len = 0
    if pnum == 1:
        for i in range(110):
            card = bank[i]
            try:
                final_dict_1[i] += bank.count(card)
            except:
                final_dict_1[i] = bank.count(card)
            p1_len += bank.count(card)
        print "p1_bank size: ", p1_len
    if pnum == 2:
        for i in range(110):
            card = bank[i]
            try:
                final_dict_2[i] += bank.count(card)
            except:
                final_dict_2[i] = bank.count(card)
            p2_len += bank.count(card)

        print "p2_bank size: ", p2_len
    return p1_len + p2_len


def set_up():
    with open("allcards.txt", 'r') as fd:
        level = 0
        for card in fd.readlines():
            if card.strip() == "-END-":
                break
            if card.strip() == "":
                continue
            if card.startswith("Level"):
                level = int(card.split()[-1])
                continue
            card_attr = card.split()
            if len(card_attr[0]) < 11: card_attr[0] += "\t"
            if len(card_attr[0]) < 7: card_attr[0] += "\t"

            try:
                CARD_BANK_1.append(Card(card_attr[0], int(card_attr[1]), int(card_attr[2]), int(card_attr[3]), int(card_attr[4]), level))
                CARD_BANK_2.append(Card(card_attr[0], int(card_attr[1]), int(card_attr[2]), int(card_attr[3]), int(card_attr[4]), level))
                ORIG_CARD_BANK.append(Card(card_attr[0], int(card_attr[1]), int(card_attr[2]), int(card_attr[3]), int(card_attr[4]), level))

            except:
                print card
                break

CARD_BANK_1 = []
CARD_BANK_2 = []
ORIG_CARD_BANK = []

final_dict_1 = {}
final_dict_2 = {}

TRIALS = 100
GAMES_PER_TRIAL = 10000

if __name__ == '__main__':
    set_up()
    p1 = Player(1, ORIG_CARD_BANK)
    p2 = Player(2, ORIG_CARD_BANK)
    board = Board()
    banked_cards = 0
    p1win = 0
    p2win = 0
    for i in range(TRIALS):
        for j in range(GAMES_PER_TRIAL):
            #print "playing game"
            #print board
            result = play_game(p1, p2, board)
            if result == 1:
                CARD_BANK_1.extend(p1.original_cards)
                p1win += 1
            elif result == 2:
                CARD_BANK_2.extend(p2.original_cards)
                p2win += 1
            board.clear()
            p1.cards = []
            p2.cards = []
            p1.original_cards = []
            p2.original_cards = []
        #Store our results thus far
        banked_cards += count_cards(CARD_BANK_1, 1, i)
        banked_cards += count_cards(CARD_BANK_2, 2, i)
        #Reset the banks
        CARD_BANK_1 = [x for x in ORIG_CARD_BANK]
        CARD_BANK_2 = [x for x in ORIG_CARD_BANK]
    for card in CARD_BANK_1:
        print "players have {} with val:\n" \
              "{}-{}\t{}-{}\t{}-{}\n" \
              "{}-{}\t{}-{}\t{}-{}\n" \
              "{}-{}\t{}-{}\t{}-{}\n"\
            .format(card.name,
                    p1.knowledge[0][0][card], p2.knowledge[0][0][card],
                    p1.knowledge[1][0][card], p2.knowledge[1][0][card],
                    p1.knowledge[2][0][card], p2.knowledge[2][0][card],
                    p1.knowledge[0][1][card], p2.knowledge[0][1][card],
                    p1.knowledge[1][1][card], p2.knowledge[1][1][card],
                    p1.knowledge[2][1][card], p2.knowledge[2][1][card],
                    p1.knowledge[0][2][card], p2.knowledge[0][2][card],
                    p1.knowledge[1][2][card], p2.knowledge[1][2][card],
                    p1.knowledge[2][2][card], p2.knowledge[2][2][card],)
    print "player 1 won ", p1win, "times in total"
    print "player 2 won ", p2win, "times in total"
    print "cards banked: {}, expected cards banked: {} wins: {}".format(banked_cards, (p1win+p2win)*5 + 220*TRIALS, p1win+p2win)
    with open ('random_card_res_by_class.txt', 'w') as fout:
        for key in final_dict_1:
            fout.write(str(final_dict_1[key])+"\n")
            fout.write(str(ORIG_CARD_BANK[key])+"\n")
            fout.write(str(final_dict_2[key])+"\n")
            fout.write(str(ORIG_CARD_BANK[key])+"\n")
            fout.write("@@@@@@@@@@@@@\n")
    with open ('random_card_res_by_value.txt', 'w') as fout:
        for i in range(10):
            limit = banked_cards*(float(i)/500)
            if i == 10:
                limit = banked_cards
            bottom_limit = banked_cards*((i-1.0)/500)
            fout.write("---{}th percentile--\n".format(i*10))
            for key in final_dict_1:
                #print final_dict_1[key]
                if bottom_limit < final_dict_1[key] < limit:
                    fout.write(str(final_dict_1[key])+"\n")
                    fout.write(str(ORIG_CARD_BANK[key])+"\n")
                    fout.write("@@@@@@@@@@@@@\n")
                if bottom_limit < final_dict_2[key] < limit:
                    fout.write(str(final_dict_2[key])+"\n")
                    fout.write(str(ORIG_CARD_BANK[key])+"\n")
                    fout.write("@@@@@@@@@@@@@\n")


