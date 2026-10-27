import random
win_conditions = [
    [1,2,3],[4,5,6],[7,8,9],
    [1,4,7],[2,5,8],[3,6,9],
    [3,5,7],[1,5,9]
]
 
# random.randint(a, b)	Random integer	Inclusive of both a and b.


# Board list (index 0 is unused, 1-9 represent the positions)
board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

player_1_list = []
player_2_list = []

def print_board():
    print(f" {board[0]}  | {board[1]}  | {board[2]} ")
    print("-----------")
    print(f" {board[3]}  | {board[4]}  | {board[5]} ")
    print("-----------")
    print(f" {board[6]}  | {board[7]}  | {board[8]} ")

def position_input(y, player_symbol):
    board[y] = player_symbol


def player_vs_bot():
    while True:
        print_board()
        winner_found = "no"
        
        # Player 1 input
        try:
            player1 = int(input("Player 1, enter your position (1-9): "))
            if player1 < 1 or player1 > 9:
                print("Invalid position. Please enter a number between 1 and 9.")
                continue
            if player1 in player_1_list or player1 in player_2_list:
                print("Position already taken. Please choose a different position.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue

        player_1_list.append(player1)
        position_input(player1 - 1 , 'X')
        
        # Check win condition for Player 1
        for i in win_conditions:
            if player_1_list == i:
                winner_found = "yes"
                break
        if winner_found == "yes":
            print_board()
            print("Player 1 wins!")

            break
        print_board()

        if winner_found == "no" and len(player_1_list) + len(player_2_list) == 9:
            print_board()
            print("It's a draw!")
            print("wana play again? ")
            break

        # Player 2 input
        try:
            player2 = random.randint(1, 9)
            print("BOT is playing its move .....}")
            if player2 < 1 or player2 > 9:
                print("Invalid position. Please enter a number between 1 and 9.")
                continue
            if player2 in player_1_list or player2 in player_2_list:
                print("Position already taken. Please choose a different position.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue
    
        player_2_list.append(player2)
        position_input(player2 - 1 , 'O')
    
        for i in win_conditions:
            if player_2_list == i:
                winner_found = "yes"
                break
        
        if winner_found == "yes":
            print_board()
            print("Player 2 wins!")
            break
        
def player_vs_player():
    while True:
        print_board()
        winner_found = "no"
        
        # Player 1 input
        try:
            player1 = int(input("Player 1, enter your position (1-9): "))
            if player1 < 1 or player1 > 9:
                print("Invalid position. Please enter a number between 1 and 9.")
                continue
            if player1 in player_1_list or player1 in player_2_list:
                print("Position already taken. Please choose a different position.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue

        player_1_list.append(player1)
        position_input(player1 - 1 , 'X')
        
        for i in win_conditions:
            if player_1_list == i:
                winner_found = "yes"
                break        
        if winner_found == "yes":
            print_board()
            print("Player 1 wins!")
            break

        print_board()

        if winner_found == "no" and len(player_1_list) + len(player_2_list) == 9:
            print_board()
            print("It's a draw!")
            print("you won this time, but next time i will beat you! 🫤")
            break
    # Player 2 input
        try:
            player2 = int(input("Player 2, enter your position (1-9): "))
            if player2 < 1 or player2 > 9:
                print("Invalid position. Please enter a number between 1 and 9.")
                continue
            if player2 in player_1_list or player2 in player_2_list:
                print("Position already taken. Please choose a different position.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue
    
        player_2_list.append(player2)
        position_input(player2 - 1 , 'O')
    
        for i in win_conditions:
            if player_2_list == i:
                winner_found = "yes"
                break        
        if winner_found == "yes" :
            print_board()
            print("bot wins!")
            print("I won haha 🤣2, better luck next time")
            break
option_1 = " player vs player"
option_2 = " player vs bot"
print("Choose a mode:")
print(f"1. {option_1}")
print(f"2. {option_2}")        
user_input = input("Choose a mode (option_1 or option_2): ")
if user_input == "1":
    print("You have chosen player vs player mode.")
    player_vs_player()  
elif user_input == "2":
    print("You have chosen player vs bot mode.")
    player_vs_bot()     
else:
    print("Invalid choice. Please restart and choose a valid mode.")
        