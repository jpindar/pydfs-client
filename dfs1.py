#! python3

"""
dfs1.py
This uses pydfs to create lineups

Note that teams are referenced in the roster file by their 2 or 3 capital letter abbreviation,
so pyDFS doesn't know the team names except as the name of their defense.
"""

import os
from pydfs_lineup_optimizer import get_optimizer, Site, Sport, CSVLineupExporter

lineup_filename = "FanDuel-NFL-2020-11-26-51889-players-list-Tday-friends.csv"

output_filename = "lineups3"
number_of_lineups = 10
note1 = ""
minimum_rank = 6.0
playersToAdd = [['','']]
playersToRemove = [['','']]
teamsToRemove = [['','']]


teamsToRemove.append(['PIT', 'game postponed by covid'])
teamsToRemove.append(['BAL', 'game postponed by covid'])
playersToAdd.append(['Deshaun Watson','good dfn stats'])


def addPlayer(thisPlayer, thisNote):
    if thisPlayer == '':
        return
    player = optimizer.get_player_by_name(thisPlayer)
    if player is None:
       print('ERROR - there is no such player as ' + thisPlayer)
       return
    newFile.write('adding ' + thisPlayer + ' (' + thisNote + ')\n')
    optimizer.add_player_to_lineup(player)

def removePlayer(thisPlayer, thisNote):
    if thisPlayer == '':
        return
    player = optimizer.get_player_by_name(thisPlayer)
    if player is None:
       print('ERROR - there is no such player as ' + thisPlayer)
       return
    newFile.write('removing ' + thisPlayer + ' (' + thisNote + ')\n')
    optimizer.remove_player(player)

def removeTeam(thisTeam, thisNote):
    if thisTeam == '':
        return
    newFile.write('removing ' + thisTeam + ' (' + thisNote + ')\n')
    badTeam = filter(lambda p: p.team == thisTeam, optimizer.players)
    for player in badTeam:
        optimizer.remove_player(player)


lineup_pathname = os.getcwd() + os.sep + lineup_filename
print("reading from " + lineup_pathname)
output_pathname = os.getcwd() + os.sep + output_filename + '.txt'
print("writing to " + output_pathname)
newFile = open(output_pathname, 'w')
newFile.write('\n' + lineup_filename + "\n" + output_filename+ "\n" + note1 + '\n')
print('calling optimizer')
optimizer = get_optimizer(Site.FANDUEL, Sport.FOOTBALL)
print('loading players')
optimizer.load_players_from_csv(lineup_pathname)
print('optimizing...')

# remove low ranked players
newFile.write('removing players below minimum rank of ' + str(minimum_rank) + '\n')
for player in optimizer.players:
    if player.fppg < minimum_rank:
        if player.positions[0] != 'D':
            optimizer.remove_player(player)

for player in playersToAdd:
   addPlayer(player[0],player[1])

for player in playersToRemove:
   removePlayer(player[0],player[1])

for bad_team in teamsToRemove:
   removeTeam(bad_team[0],bad_team[1])

print('optimizing...')
lineups = optimizer.optimize(n=number_of_lineups)
print('got lineups')

for lineup in lineups:
    newFile.write("\n***********\n")
    # print(lineup)
    newFile.write(str(lineup))

optimizer.print_statistic()
newFile.close()

# output_pathname = os.getcwd() + os.sep + output_filename + '.csv'
# print("writing csv to " + output_pathname)
# exporter = CSVLineupExporter(optimizer.optimize(n=number_of_lineups))
# exporter.export(output_pathname)

