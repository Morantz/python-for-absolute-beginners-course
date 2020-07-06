import datetime
import json
import os
from colorama import Fore


def show_header():
    set_green()
    print("---------------------------")
    print("       Connect 4 Game")
    print("   Error Handling Edition")
    print("---------------------------")
    set_white()


def set_white():
    print(Fore.WHITE)


def set_green():
    print(Fore.GREEN)


def set_yellow():
    print(Fore.YELLOW)


def set_cyan():
    print(Fore.CYAN)


def set_purple():
    print(Fore.MAGENTA)


def main():
    show_header()
    show_leaderboard()

    # CREATE THE BOARD:
    # Board is a list of rows
    # Rows are a list of cells
    board = [
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
    ]

    # CHOOSE INITIAL PLAYER
    active_player_index = 0
    player1, player2 = get_players()
    players = [player1, player2]
    log(players)
    symbols = ["X", "O"]
    player = players[active_player_index]

    # UNTIL SOMEONE WINS
    while not find_winner(board):
        # SHOW THE BOARD
        player = players[active_player_index]
        symbol = symbols[active_player_index]

        announce_turn(player)
        show_board(board)
        if not choose_location(board, symbol):
            print("That isn't an option, try again.")
            log(f"{player} tried an invalid option!")
            continue

        # TOGGLE ACTIVE PLAYER
        active_player_index = (active_player_index + 1) % len(players)

    print()
    set_purple()
    print(f"GAME OVER! {player} has won with the board: ")
    set_white()
    record_win(player)
    show_board(board)
    print()
    log(f"GAME OVER! {player} has won the Game!!")


def choose_location(board, symbol):
    column = int(input("Choose which column: "))
    column -= 1

    if column < 0 or column >= len(board[0]):
        log(f'ERROR - Invalid Column {column} was selected by player {symbol}')
        return False

    if board[0][column]:
        log(f'ERROR - Full Column {column} was selected by player {symbol}')
        return False

    log(f'Column {column} was selected by player {symbol}')

    row = len(board)
    while True:
        row -= 1
        cell = board[row][column]
        if cell is None:
            break

    board[row][column] = symbol
    return True


def get_players():
    p1 = input("Player 1, what is your name? ")
    p2 = "Computer"

    return p1, p2


def show_board(board):
    set_yellow()
    for row in board:
        print("| ", end='')
        for cell in row:
            symbol = cell if cell is not None else "_"
            print(symbol, end=" | ")
        print()
    set_white()


def show_leaderboard():
    leaders = load_leaders()
    log(leaders)

    sorted_leaders = list(leaders.items())
    sorted_leaders.sort(key=lambda l: l[1], reverse=True)

    print()
    print("---------------------------")
    print("LEADERS:")
    for name, wins in sorted_leaders[0:5]:
        print(f"{wins:,} -- {name}")
    print("---------------------------")
    print()


def load_leaders():
    directory = os.path.dirname(__file__)
    filename = os.path.join(directory, 'leaderboard.json')

    if not os.path.exists(filename):
        return {}

    with open(filename, 'r', encoding='utf-8') as fin:
        return json.load(fin)


def record_win(winner_name):
    leaders = load_leaders()

    if winner_name in leaders:
        leaders[winner_name] += 1
    else:
        leaders[winner_name] = 1

    directory = os.path.dirname(__file__)
    filename = os.path.join(directory, 'leaderboard.json')

    with open(filename, 'w', encoding='utf-8') as fout:
        json.dump(leaders, fout)


def log(msg):
    directory = os.path.dirname(__file__)
    filename = os.path.join(directory, 'connect4.log')

    with open(filename, 'a', encoding='utf-8') as fout:
        fout.write(f"[{datetime.datetime.now().date().isoformat()}] ")
        fout.write(str(msg))
        fout.write('\n')


def announce_turn(player):
    print()
    msg = str("It's " + Fore.BLUE + player + "'s " + Fore.WHITE + "turn. Here's the board:")
    print(msg)
    print()


def find_winner(board):
    sequences = get_winning_sequences(board)

    for cells in sequences:
        symbol1 = cells[0]
        if symbol1 and all(symbol1 == cell for cell in cells):
            return True

    return False


def get_winning_sequences(brd):
    sequences = []
    rows = len(brd)
    cols = len(brd[0])

    # Win by rows
    for r_idx in range(0, rows):
        for c_idx in range(0, cols - 3):
            row = [
                brd[r_idx][c_idx + 0], brd[r_idx][c_idx + 1], brd[r_idx][c_idx + 2], brd[r_idx][c_idx + 3]
            ]
            sequences.append(row)

    # Win by columns
    for c_idx in range(0, cols):
        for r_idx in range(0, (rows - 3)):
            col = [
                brd[r_idx + 0][c_idx],
                brd[r_idx + 1][c_idx],
                brd[r_idx + 2][c_idx],
                brd[r_idx + 3][c_idx]
            ]
            sequences.append(col)

    # Win by diagonals
    for r_idx in range(0, rows - 3):
        for c_idx in range(0, cols - 3):
            diagonals = [
                [brd[r_idx + 0][c_idx + 0], brd[r_idx + 1][c_idx + 1], brd[r_idx + 2][c_idx + 2], brd[r_idx + 3][c_idx + 3]],
                [brd[r_idx + 0][c_idx + 3], brd[r_idx + 1][c_idx + 2], brd[r_idx + 2][c_idx + 1], brd[r_idx + 3][c_idx + 0]]
            ]
            sequences.extend(diagonals)

    return sequences


if __name__ == '__main__':
    main()
