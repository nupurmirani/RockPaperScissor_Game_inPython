import random

def comp():
    player1 = input("Rock(r), Paper(p), or Scissors(s): ").lower()
    if player1 in ['r', 'p', 's']:
        rand = random.randint(1, 3)
        if rand == 1:
            player2 = 'r'
        elif rand == 2:
            player2 = 'p'
        else:
            player2 = 's'
        return player1, player2
    else:
        print("Invalid input. Please choose 'r', 'p', or 's'.")
        return comp()

def get_winner(player1, player2):
    if player1 == player2:
        return None
    if (player1 == 's' and player2 == 'p') or (player1 == 'r' and player2 == 's') or (player1 == 'p' and player2 == 'r'):
        return 'player1'
    else:
        return 'player2'

print("Welcome to Rock, Paper, and Scissors game!")
while True:
    user = input("Who do you want to play with? Comp(c) or Multiplayer(m)? \nIf you want to quit, press (q): ").lower()
    if user == 'c':
        print("You are playing against the computer!")
        player1, player2 = comp()
    elif user == 'm':
        print("Multiplayer mode! Player 1 and Player 2 will play against each other.")
        player1 = input("Player 1, Rock(r), Paper(p), or Scissors(s): ").lower()
        player2 = input("Player 2, Rock(r), Paper(p), or Scissors(s): ").lower()
    elif user == 'q':
        print("Goodbye :)")
        break
    else:
        print("Invalid input. Please select 'c', 'm', or 'q'. Exiting...")
        continue

    winner = get_winner(player1, player2)
    print(f"Player 1 chose: {player1} \nPlayer 2 chose: {player2}")
    if winner is None:
        print("It's a tie!")
    elif winner == 'player1':
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")
