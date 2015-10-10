#!/usr/bin/python

import sys
from Players import Moves
from Players import PlayerFactory

def checkArgs():
    validArgNum = len(sys.argv) == 3

    if not validArgNum:
        raise Exception("Arguments should be in the following format: [AI Difficulty] [Number Of Games To Play]")


if __name__ == "__main__":
    checkArgs()

    print "Hello!\n" \
          "Welcome to our Rock-Paper-Scissor-Lizard-Spock Game!\n" \
          "For those not familiar with how the game is played, I will explain it now.  R=Rock, P=Paper, S=Scissors, " \
          "L=Lizard, and W=Spock.\n" \
          "S>P, P>R, R>L, L>W, W>S, S>L, L>P, P>W, W>R, R>S. For this trial, you will play 50 games of rock paper " \
          "scissors and our AI will attempt to beat you as much as possible.\n" \
          "Good luck!\n"

    player = PlayerFactory.initPlayer(int(sys.argv[1]))
    maxNumGames = int(sys.argv[2])

    print "You selected (" + player.getPlayerName() + ") player and number of moves (%d)" % maxNumGames

    player1History = ""
    player2History = ""
    scoreHistory = []
    numGames = 0
    while numGames < maxNumGames:
        AIMove = player.getNextMove(player1History, player2History, scoreHistory, -1)
        try:
            move = Moves.parseMove(raw_input("\nEnter your move for trial %d:  " % numGames))
        except:
            print "Sorry, I didn't quite catch that. Please enter Rock | Paper | Scissors | Lizard | Spock."
        else:
            print "You tried (" + Moves.convertToFullName(move) + ") and I tried (" + Moves.convertToFullName(AIMove) + ")"
            result = Moves.compare(move, AIMove)

            if result is 1:
                print "You win!"
            elif result is -1:
                print "You lose!"
            else:
                print "You tie!"

            player1History += AIMove
            player2History += move
            scoreHistory.append(result)

            numGames += 1

    scoreSum = sum([outcome for outcome in scoreHistory])

    print "========================================"

    if scoreSum >= 1:
        print "Overall you win!"
    elif scoreSum <= -1:
        print "Overall you lose!"
    else:
        print "Overall you tie!"
