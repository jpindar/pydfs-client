#! python3

"""
dfs1.py
first test of pydfs
"""

import os
from pydfs_lineup_optimizer import get_optimizer, Site, Sport, CSVLineupExporter


lineup_filename = "FanDuel-NFL-2019-11-28-40929-players-list.csv"
output_filename = "lineups1.txt"
csv_filename = "results1.csv"
number_of_lineups = 10
minimum_rank = 1.0

filename = os.getcwd() + os.sep + output_filename   # could use "\\"
print("writing to " + output_filename)
newFile = open(output_filename, 'w')

optimizer = get_optimizer(Site.FANDUEL, Sport.FOOTBALL)
optimizer.load_players_from_csv(lineup_filename)

# player = optimizer.get_player_by_name('Matthew Stafford')
# optimizer.remove_player(player)
teamName = 'DET'
thisTeam = filter(lambda p: p.team == teamName, optimizer.players)
for player in thisTeam:
    optimizer.remove_player(player)



# remove low ranked players
for player in optimizer.players:
    if player.fppg < minimum_rank:
        optimizer.remove_player(player)

playerName = 'Devonta Freeman'
player = optimizer.get_player_by_name(playerName)
optimizer.remove_player(player)


playerName = 'Tarik Cohen'
player = optimizer.get_player_by_name(playerName)
optimizer.add_player_to_lineup(player)
  
for lineup in optimizer.optimize(n=number_of_lineups):
    newFile.write("\n***********\n")
    # print(lineup)
    newFile.write(str(lineup))

newFile.close()


# exporter = CSVLineupExporter(optimizer.optimize(n=number_of_lineups))
# exporter.export(csv_filename)

