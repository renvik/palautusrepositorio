from statistics_service import StatisticsService
from player_reader import PlayerReader
# Muokkaa tätä että injektoi StatisticsService-oliolle PlayerReader-luokan olion
# (jolle on annettu konstruktoriparametrina haluttu osoite) 

def main():
    # lisätty alle PlayerReader-luokan olion injektointi
    stats = StatisticsService(
      PlayerReader("https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt")
    )
    #stats = StatisticsService()
    philadelphia_flyers_players = stats.team("PHI")
    top_scorers = stats.top(10)

    print("Philadelphia Flyers:")
    for player in philadelphia_flyers_players:
        print(player)

    print("Top point getters:")
    for player in top_scorers:
        print(player)


if __name__ == "__main__":
    main()
