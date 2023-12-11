# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str):
    # checks valid coordinates
    if not (x >= 0 and x < 3) and (y >=