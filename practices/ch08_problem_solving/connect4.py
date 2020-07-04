def show_header():
    print("---------------------------")
    print("       Connect 4 Game")
    print("---------------------------")


def main():
    show_header()

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
    players = ["Daniel", "Computer"]
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
            continue

        # TOGGLE ACTIVE PLAYER
        active_player_index = (active_player_index + 1) % len(players)

    print()
    print(f"GAME OVER! {player} has won with the board: ")
    show_board(board)
    print()


def choose_location(board, symbol):
    column = int(input("Choose which column: "))
    column -= 1

    if column < 0 or column >= len(board[0]):
        return False

    if board[0][column]:
        return False

    row = len(board)
    while True:
        row -= 1
        cell = board[row][column]
        if cell is None:
            break

    board[row][column] = symbol
    return True


def show_board(board):
    for row in board:
        print("| ", end='')
        for cell in row:
            symbol = cell if cell is not None else "_"
            print(symbol, end=" | ")
        print()


def announce_turn(player):
    print()
    print(f"It's {player}'s turn. Here's the board:")
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
