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

filename = os.getcwd() + os.sep + output_filename   # could use "\\"
print("writing to " + output_filename)
newFile = open(output_filename, 'w')
newFile.write('No lions \n')
newFile.write('No players below 6.0 points\n')
newFile.write('add Tarik Cohen\n')
newFile.write('remove Devonta Freeman (just back from foot injury)')
newFile.write('add Drew brees');


optimizer = get_optimizer(Site.FANDUEL, Sport.FOOTBALL)
optimizer.load_players_from_csv(lineup_filename)


# Stafford is out this week, let's not play any Lions
# player = optimizer.get_player_by_name('Matthew Stafford')
# optimizer.remove_player(player)
lions = filter(lambda p: p.team == 'DET', optimizer.players)
for player in lions:
    optimizer.remove_player(player)



# remove low ranked players (who might not even start!)
minimum_rank = 6.0
for player in optimizer.players:
    if player.fppg < minimum_rank:
        optimizer.remove_player(player)


# Devonta Freeman  is just back from a foot injury
player = optimizer.get_player_by_name('Devonta Freeman')
optimizer.remove_player(player)


# recommended by Sportsline
player = optimizer.get_player_by_name('Tarik Cohen')
optimizer.add_player_to_lineup(player)
  
  
# just because
player = optimizer.get_player_by_name('Drew Brees')
optimizer.add_player_to_lineup(player)

for lineup in optimizer.optimize(n=number_of_lineups):
    newFile.write("\n***********\n")
    print(lineup)
    newFile.write(str(lineup))

newFile.close()


# exporter = CSVLineupExporter(optimizer.optimize(n=number_of_lineups))
# exporter.export(csv_filename)



