import random
class Board():
    def __init__(self,row=10,column=10):
        self.board=[[0 for x in range(row)] for y in range(column)]
        self.snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
        self.ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
        self.num=100
        for i in range(10):
            for j in range(10):
                # Access and do something with each element
                self.board[i][j]=self.num
                self.num-=1

    def position(self,number,p1):
        if number in self.snakes:
            print(f"OOps {p1.name} you are revert back to {self.snakes[number]}")
            return self.snakes[number]
        elif number in self.ladders:
            print(f"WOW {p1.name} you are jump to {self.ladders[number]}")
            return self.ladders[number]
        else:
            return number



    def print_board(self,all_players):
        for i in range(10):
            for j in range(10):
                element= self.board[i][j]
                to_print= element
                if element in self.snakes:
                    to_print="🐍"
                elif element in self.ladders:
                    to_print="🏳️"
                else:
                    for player in all_players:
                        if player.position == element:
                            to_print = f"{player.name[0]}+☀︎"

                print(to_print,end=" ")

            print()


class Player(Board):
    def __init__(self,name):
        self.name=name
        self.position=0

    def roll_dice(self):
        return random.randint(1,6)

    def move(self,number):

        self.position+=number
        if self.position>100:
            print("Next time Better Luck")
            self.position -= number




def main():
    num=int(input("Enter the Number of player want to Play"))
    players=[]
    for i in range (num):
        each_player= Player(input(f"Enter the Name of {i+1}th Player"))
        players.append(each_player)

    loop=True
    while loop:
        hashMap={}
        for each_player in players:

            input(f"Hey {each_player.name} Press enter to roll a dice")
            dice_number=each_player.roll_dice()
            print(f"Hey {each_player.name} you got {dice_number}")
            each_player.move(dice_number)
            position=Board().position(each_player.position,each_player)
            each_player.position=position
            Board().print_board(players)
            if position in hashMap:
                get_player=hashMap[position]
                get_player.position=0
                print(f"Hey {get_player.name} you are cut by {each_player.name}")
            else:
                hashMap[position]=each_player
            if position==100:
                print(f"Hey {each_player.name} you are winner")
                loop=False
                break
        hashMap.clear()



main()
