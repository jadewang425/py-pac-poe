
board = { 
        'A1': " ",
        'A2': " ",
        'A3': " ",
        'B1': " ",
        'B2': " ",
        'B3': " ",
        'C1': " ",
        'C2': " ",
        'C3': " "
    }
board_view = f"""
    A   B   C
    
1)  {board['A1']} | {board['B1']} | {board['C1']} 
    -----------
2)  {board['A2']} | {board['B2']} | {board['C2']} 
    -----------
3)  {board['A3']} | {board['B3']} | {board['C3']} 
"""

opening_msg = """
----------------------
Let's play Py-Pac-Poe!
----------------------
"""
print(opening_msg)
print(board_view)

cur_player = 'X'
winner = False

#check win or tie function to be called in render_game
def check_win_or_tie():
    if board['A1'] == board['A2'] == board['A3'] or board['B1'] == board['B2'] == board['B3'] or board['C1'] == board['C2'] == board['C3'] or board['A1'] == board['B1'] == board['C1'] or board['A2'] == board['B2'] == board['C2'] or board['A3'] == board['B3'] == board['C3'] or board['A1'] == board['B2'] == board['C3'] or board['A3'] == board['B2'] == board['C1']:
        return winner == cur_player
    else:
        board_values = list(board.values())
        if " " not in board_values:
            return winner == 'T'
# a function that should keep running until there's a winner or tie
def render_game():
    cur_input = input(f"Player {cur_player}'s Move (example B2): ").upper()
    if board[cur_input] != " ":
        print(f"{board[cur_input]} is already in here!")
    else:
        board[cur_input] = cur_player
        print(board_view)
        #check winner or tie
        check_win_or_tie()
        if winner:
            if winner == 'T':
                print("Cats game!")
            else:
                print(f"{cur_player} wins!")
        else:
            if cur_player == 'X':
                cur_player =='O'
            else:
                cur_player = 'X'
            render_game()


render_game()