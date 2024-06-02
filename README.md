
# Rock, Paper, Scissors Game

This is a Python implementation of the classic Rock, Paper, Scissors game. The game allows the user to play either against the computer or in a multiplayer mode where two players can compete against each other. The game also provides an option to quit.

## Features

- Single-player mode: Play against the computer.
- Multiplayer mode: Two players can play against each other.
- Input validation to ensure valid game choices.
- Displays the winner after each round.

## How to Play

1. The game will prompt the user to choose between playing against the computer (`c`) or playing in multiplayer mode (`m`). The user can also quit the game by pressing `q`.
2. In single-player mode, the user will input their choice of Rock (`r`), Paper (`p`), or Scissors (`s`). The computer will randomly select one of the three options.
3. In multiplayer mode, both players will input their choices of Rock (`r`), Paper (`p`), or Scissors (`s`).
4. The game will then compare the choices and determine the winner based on the rules:
   - Rock beats Scissors
   - Scissors beats Paper
   - Paper beats Rock
5. The game will display the choices of both players and announce the winner or declare a tie.


### Functions

#### `comp()`
This function handles the single-player mode. It prompts the player to enter their choice and then randomly selects a choice for the computer. It returns the choices of both the player and the computer.

#### `get_winner(player1, player2)`
This function takes the choices of both players as input and determines the winner based on the rules of Rock, Paper, Scissors. It returns the winner or `None` if it's a tie.

### Main Game Loop
The game continuously prompts the user to choose between playing against the computer, playing in multiplayer mode, or quitting the game. Depending on the user's choice, it calls the appropriate functions and displays the results.
