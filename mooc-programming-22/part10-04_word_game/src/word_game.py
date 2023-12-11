# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class RockPaperScissors(WordGame):
    def __init__(self, round: int):
        super().__init__(round)

    def round_winner(self, player1_word: str, player2_word: str):
        if not self.valid_input(player1_word) and not self.valid_input(player2_word):
            return 0
        
        if self.valid_input(player1_word) == True and self.valid_input(player2_word) == False:
            return 1

        if self.valid_input(player1_word) == False and self.valid_input(player2_word) == True:
            return 2
  

        if player1_word == "rock": 
            if player2_word == "rock":
                return 0
            elif player2_word == "scissors":
                return 1
            else:
                return 2
        
        if player1_word == "scissors":
            if player2_word == "rock":
                return 2
            elif player2_word == "scissors":
                return 0
            else:
                return 1            

        if player1_word == "paper":
            if player2_word == "rock":
                return 1
            elif player2_word == "scissors":
                return 2
            else:
                return 0
    
    def valid_input(self, input: str):
        valid = ["rock", "paper", "scissors"]
        if input.lower() in valid:
            return True
        
        return False




class LongestWord(WordGame):
    def __init__(self, round: int):
        super().__init__(round)

    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):
            return 1 
        elif len(player1_word) < len(player2_word):
            return 2
        else:
            return 0


class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        vowels = "aeiouAEIOU"
        player1 = 0
        player2 = 0
        for letter in player1_word:
            if letter in vowels:
                player1 += 1
        
        for letter in player2_word:
            if letter in vowels:
                player2 += 1
        
        if player1 > player2: 
            return 1
        elif player1 < player2:
            return 2
        else:
            return 0

        

if __name__ == "__main__":
    p = RockPaperScissors(3)
    p.play()