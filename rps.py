# We'll import numpy as a basic "AI" that choose between the moves.
import numpy as np
moves = ['Rock', 'Paper', 'Scissors']


# When it comes to player's turn, execute this
def turn(choice):
    while choice not in ['R', 'P', 'S']:
        print('Try again!', end=' ')
        choice = input().upper()
    choice = 'Rock' if choice == 'R' else ('Paper' if choice == 'P' else "Scissors")
    return choice


# Condition of a win, base on this we can calculate the score
def conditions(player_move, ai_move):
    if player_move == ai_move:
        return 0.5
    if ((player_move == 'Rock' and ai_move == 'Scissors')
            or (player_move == 'Paper' and ai_move == 'Rock')
            or (player_move == 'Scissors' and ai_move == 'Paper')):
        return 1
    if ((ai_move == 'Rock' and player_move == 'Scissors')
            or (ai_move == 'Paper' and player_move == 'Rock')
            or (ai_move == 'Scissors' and player_move == 'Paper')):
        return -1


def scoring(player_move, ai_move, player_score, ai_score):
    if conditions(player_move, ai_move) == 1:
        print('You win!')
        player_score += 1
    elif conditions(player_move, ai_move) == -1:
        print('Opponent win...')
        ai_score += 1
    else:
        print('Draw')
        player_score += 0.5
        ai_score += 0.5
    return player_score, ai_score


if __name__ == '__main__':
    your_score = 0
    cpu_score = 0
    print('Welcome to Rock Paper Scissors!')
    print('Make your move:', end=' ')

    while True:
        player = input().upper()
        player = turn(player)
        ai = np.random.choice(moves)
        # Ensures that the computer can only choose between the pre-determined moves.

        print(f'You chose {player}')
        print(f'Computer chose {ai}')
        your_score, cpu_score = scoring(player, ai, your_score, cpu_score)

        # Dealing with the player wanting to play again
        print('Play again? (Y/N)', end=' ')
        again = input().upper()
        while again not in ['Y', 'N']:
            print('Invalid statement. Type again?', end=' ')
            again = input().upper()
        if again == 'Y':
            print('\nMake your move:', end=' ')
            continue
        elif again == 'N':
            break

    print(
        f"""\nTotal score:
    You: {your_score}
    AI: {cpu_score}
Thanks for playing! See you next time <3""")
