import random

class Board():
    def __init__(self,size=100):
        self.size=size
        self.snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
        self.ladders={1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}


    def check_ladder_snake(self,position):
        if position in self.snakes:
            print(f"OOps Snake at {position} you are revert back to {self.snakes[position]}")
            return self.snakes[position]
        elif position in self.ladders:
            print(f"Wow Ladder at{position} climb at {self.ladders[position]}")
            return self.ladders[position]
        else :
            return position

    def display_board(self, player1, player2):
        print(f"Player 1 ({player1.name}) is at position {player1.position}")
        print(f"Player 2 ({player2.name}) is at position {player2.position}")



class Player():
    def __init__(self,name):
        self.name=name
        self.position=1

    def roll_dice(self):
        return random.randint(1,6)

    def move(self,step):

        self.position+=step
        if self.position>100:
            print("Not Greater than 100")
            self.position-=step

def main():
    board=Board()
    p1=Player("Albert")
    p2=Player("BOB")

    while True:
        input(" Press Enter to roll the dice")

        dice_number=p1.roll_dice()
        print(f"Hey {p1.name} you got {dice_number}")
        p1.move(dice_number)
        p1.position=board.check_ladder_snake(p1.position)
        board.display_board(p1, p2)

        if p1.position == 100:
            print(f"Hey {p1.name} Win")
            break

        dice_number = p2.roll_dice()
        print(f"Hey {p2.name} you got {dice_number}")
        p2.move(dice_number)
        p2.position = board.check_ladder_snake(p2.position)
        board.display_board(p1, p2)

        if p2.position == 100:
            print(f"Hey {p2.name} Win")
            break

main()