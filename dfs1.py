#! python3

"""
dfs1.py
This uses pydfs to create lineups
"""

import os
from pydfs_lineup_optimizer import get_optimizer, Site, Sport, CSVLineupExporter


lineup_filename = "FanDuel-NFL-2019-11-28-40929-players-list.csv"
output_filename = "lineups1"
number_of_lineups = 10
note1 = ""
minimum_rank = 1.0

lineup_pathname = os.getcwd() + os.sep + lineup_filename
print("reading from " + lineup_pathname)
output_pathname = os.getcwd() + os.sep + output_filename + 'txt'
print("writing to " + output_pathname)
newFile = open(output_pathname, 'w')
newFile.write('\n' + lineup_filename + "\n" + output_filename+ "\n" + note1 + '\n')
print('calling optimizer')
optimizer = get_optimizer(Site.FANDUEL, Sport.FOOTBALL)
print('loading players')
optimizer.load_players_from_csv(lineup_pathname)
print('optimizing...')

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

# output_pathname = os.getcwd() + os.sep + output_filename + 'csv'
# print("writing csv to " + output_pathname)
# exporter = CSVLineupExporter(optimizer.optimize(n=number_of_lineups))
# exporter.export(output_pathname)

