# !/usr/bin/env python3
# This program plays a game of Rock, Paper, Scissors between two Players,
# and reports both Player's scores each round.
import random
moves = ['rock', 'paper', 'scissors']
# The Player class is the parent class for all of the Players
# in this game"""


class Player:
    my_move = None
    their_move = None

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move
# player class that selects moves randomly


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)
# player class that allows a user to choose his moves


class HumanPlayer(Player):
    def move(self):
        while True:
            mychoice = input("Select your move, Rock, Paper or "
                             "Scissors?\n").lower()
            if mychoice in moves:
                return mychoice
            else:
                print("Please enter a valid move")


class ReflectPlayer(Player):
    def move(self):
        self.their_move = "nothing"
        if self.their_move == "nothing":
            return random.choice(moves)
        else:
            return self.their_move


class CyclePlayer(Player):
    def move(self):
        if self.my_move == "rock":
            return "paper"
        elif self.my_move == "paper":
            return "scissors"
        elif self.my_move == "scissors":
            return "rock"
        else:
            return "rock"


def beats(one, two):
    if one == two:
        return "Tie"
    elif ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock')):
        return True


class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1.outcome = 0
        self.p2.outcome = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1 Played: {move1}\nPlayer 2 Played: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1, move2):
            print("** Player One Wins! **")
            self.p1.outcome += 1
        elif beats(move2, move1):
            print("** Player Two Wins! **")
            self.p2.outcome += 1
        elif move1 == move2:
            print("** No Wins! **")
        print(f"Score: Player One: {self.p1.outcome},  Player Two "
              "{self.p2.outcome}")

    def play_game(self):
        print("Rock Paper scissors game, start!")
        while True:
            rounds = input("Enter the number of rounds you want to play: ")
            try:
                rounds = int(rounds)
                for round in range(rounds):
                    print(f"Round {round}:")
                    self.play_round()
                if self.p1.outcome > self.p2.outcome:
                    print("Congratulations Player 1, you won!!")
                elif self.p1.outcome < self.p2.outcome:
                    print("** Congratulations Player Two,"
                          "You are the Winner! **")
                else:
                    print("There is no winner, it is a tie!")
                print(f"Number of round played is: {rounds}")
                print("Game over!")
                while True:
                    again = input("Do you want to play again,"
                                  " yes or no? ").lower()
                    if "yes" in again:
                        print("Lets Play again")
                        break
                    elif "no" in again:
                        print("Game over!")
                        return exit(0)
                    else:
                        print("Invalid answer")
            except ValueError:
                print("Please enter a number")


if __name__ == '__main__':
    players = [RandomPlayer(), ReflectPlayer(), CyclePlayer()]
    while True:
        playmate = input("Choose Playmate:\nEnter 0 for Random Player\nEnter"
                         " 1 for Reflect Player\nEnter 2 for Cycle Player\n")
        try:
            playmate = int(playmate)
            if playmate in range(3):
                game = Game(HumanPlayer(), players[playmate])
                game.play_game()
        except ValueError:
            print("Not a valid number")
