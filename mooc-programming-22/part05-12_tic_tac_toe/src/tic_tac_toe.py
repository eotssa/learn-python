# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str):
    # checks valid coordinates
    if not ((x >= 0 and x < 3) and (y >= 0 and y < 3)):
        return False

    # checks empty spot, y-coord is column
    if not game_board[y][x] == "": 
        return False
    
    game_board[y][x] = piece

    return True




if __name__ == "__main__":
    game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(play_turn(game_board, 2, 0, "X"))
    print(game_board)   

    