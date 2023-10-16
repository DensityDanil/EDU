import random
import pandas as pd

def generate_players(num_players):
    players = [f"Player {i+1}" for i in range(num_players)]
    return players

def play_match(player1, player2):
    while True:
        score1 = random.randint(0, 5)
        score2 = random.randint(0, 5)
        print(f"{player1} vs {player2}: {score1} - {score2}")
        if score1 > score2:
            return player1
        elif score2 > score1:
            return player2
        else:
            print('tie!')
            #return f"{player1},{player2}"

def tournament(players):
    round_num = 1
    results = []
    while len(players) > 1:
        random.shuffle(players)
        winners = []
        for i in range(0, len(players), 2):
            match_players = players[i:i+2]
            winner = play_match(match_players[0], match_players[1])
            winners.append(winner)
            results.append((round_num, match_players[0], match_players[1], winner))
        players = winners
        round_num += 1
    return players[0], results

def print_results(results):
    print("Tournament Results:")
    print("{:<7} {:<15} {:<15} {:<15}".format("Round", "Player 1", "Player 2", "Winner"))
    df = pd.DataFrame(results)
    df.columns = 'round_num, player1, player2, winner'.split(', ')
    print(df)
    df.to_excel('tennis.xlsx')
    
    #for round_num, player1, player2, winner in results:
    #    print("{:<7} {:<15} {:<15} {:<15}".format(round_num, player1, player2, winner))

if __name__ == "__main__":
    num_players = 16
    players = generate_players(num_players)
    winner, simulation_results = tournament(players)
    
    # Додаємо інформацію про нічії у фінальну таблицю
    final_results = [(round_num, player1, player2, winner) if winner != "It's a tie!" else (round_num, player1, player2, f"{player1}, {player2}") for round_num, player1, player2, winner in simulation_results]

    print_results(final_results)
    print(f"\nThe winner is: {winner}")
