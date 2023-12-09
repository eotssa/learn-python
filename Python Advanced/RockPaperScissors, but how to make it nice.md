# Version 1
```
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
        

if __name__ == "__main__":
    p = RockPaperScissors(3)
    p.play()
```

# Improved Version 
```import random
 
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
 
class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
 
    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player2_word) > len(player1_word):
            return 2
        else:
            # Any number can be returned for tie according to
            # definition
            return 0
 
class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
 
    #  Help method for calculating the vowels
    def count_vowels(self, word: str):
        vok = "aeiouyåöäö"
        vowels = 0
        for character in word:
            if character in vok:
                vowels += 1
        return vowels
 
 
    def round_winner(self, player1_word: str, player2_word: str):
        if self.count_vowels(player1_word) > self.count_vowels(player2_word):
            return 1
        elif self.count_vowels(player2_word) > self.count_vowels(player1_word):
            return 2
        else:
            return 0
 
class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
 
    def round_winner(self, player1_word: str, player2_word: str):
        choices = {"rock" : 0, "paper": 1, "scissors": 2}
        # Not good first
        if player1_word not in choices.keys() and player2_word not in choices.keys():
            return 0
 
        if player1_word not in choices.keys():
            return 2
 
        if player2_word not in choices.keys():
            return 1
 
        # Use dictionary to calculate the difference between
        # choices. For example: player 1 selects paper, value is 1
        # player2 selects rock, value is 0
        # player 1 wins when the difference is 1 or -2
        # player 2 wins when the difference is -1 ot 2
        # 0 means that both selected the same choice
        difference = choices[player1_word] - choices[player2_word]
        
        if difference == 0:
            return 0
 
        if difference == 1 or difference == -2:
            return 1
 
        return 2
 
```