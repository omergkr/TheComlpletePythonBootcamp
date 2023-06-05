import random


def display_board(board):
    print("\n" * 100)
    print("| " + board[7] + " | " + board[8] + " | " + board[9] + " |")
    print("-------------")
    print("| " + board[4] + " | " + board[5] + " | " + board[6] + " |")
    print("-------------")
    print("| " + board[1] + " | " + board[2] + " | " + board[3] + " |")


def user_choice():
    acceptable_range = range(0, 10)
    within_range = False

    choice = "Wrong"
    while not choice.isdigit() or not within_range:
        choice = input("Please enter a number (1-9): ")
        if not choice.isdigit():
            print("Sorry that is not a digit! please make a correct entry")
        if choice.isdigit():
            if int(choice) in acceptable_range:
                within_range = True
            else:
                within_range = False
                print("Sorry that is not in range! please make a correct entry")
    return int(choice)


def player_input():
    marker = ""
    while marker != "X" and marker != "O":
        marker = input("Player 1, choose X or O: ")

    player_1 = marker

    if player_1 == "X":
        player_2 = "O"
    else:
        player_2 = "X"

    return player_1, player_2


def place_marker(board, marker, position):
    board[position] = marker


def replacement_choice(gameList, new_position):
    user_placement = input("Type a string to place at the position O or X")
    gameList[new_position] = user_placement
    return game_list


def game_on_choice():
    choice = "wrong"
    while choice not in ["Y", "N"]:
        choice = input("Please enter a number (Y or N): ")
        if choice not in ["Y", "N"]:
            print("Sorry that is not valid! please choose Y or N")

    if choice == "Y":
        return True
    else:
        return False


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal


def choose_first():
    flip = random.randint(0, 1)
    if flip == 0:
        return "Player 1"
    else:
        return "Player 2"


def space_check(board, position):
    return board[position] == " "


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input("Choose a position: (1-9) "))
    return position


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


print('Welcome to Tic Tac Toe!')
while True:
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    play_game = input('Are you ready to play? Enter Yes or No.')
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    while game_on:
        if turn == 'Player 1':
            # Player1's turn.

            display_board(theBoard)
            print("turn player 1")
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations Player 1! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.

            display_board(theBoard)
            print("turn player 2")
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break


