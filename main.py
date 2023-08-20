# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

from gtn import guess_the_number
from rps import rock_paper_scissors
from wordle import Wordle
while True:
    txt = """ Mini Games!!
    -Guess The Number(1)
    -Rock,Paper,Scissors(2)
    -Wordle(3)
    -ConnectFour(4)
    -Tic Tac Toe(5)
Select a game(press number or 'q' to quit):        
    """
    value = input(txt)
    if value == "1":
        guess_the_number(1000)
    elif value == "2":
        rock_paper_scissors()
    elif value == "3":
        game = Wordle()
        game.play()
    elif value == "4":
        pass
    elif value == "5":
        pass
    elif value == "q":
        break

