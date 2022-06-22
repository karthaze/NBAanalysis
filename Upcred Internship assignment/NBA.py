import pandas as pd

## Reading the data, i'm not that well equipped with databases so lets just store it in the file itself

player_data=pd.read_csv('Data/player_data.csv')
player_stats=pd.read_csv('Data/Seasons_Stats.csv')
Players=pd.read_csv('Data/Players.csv')

##creating Dummies
point_guards=player_stats[player_stats['Pos']=='PG']
shooting_guards=player_stats[player_stats['Pos']=='SG']
small_forwards=player_stats[player_stats['Pos']=='SF']
power_forwards=player_stats[player_stats['Pos']=='PF']
centers=player_stats[player_stats['Pos']=='C']
PGS=point_guards.sort_values(['PTS', 'Age', 'G'], ascending=[False, True, True])
SGS=shooting_guards.sort_values(['PTS', 'Age', 'G'], ascending=[False, True, True])
SFS=small_forwards.sort_values(['PTS', 'Age', 'G'], ascending=[False, True, True])
PFS=power_forwards.sort_values(['PTS', 'Age', 'G'], ascending=[False, True, True])
CS=centers.sort_values(['PTS', 'Age', 'G'], ascending=[False, True, True])

#dummy array:
arr=[PGS, SGS, SFS, PFS, CS]


##code

def team_score(arr):
    ans=0
    for i in arr:
        ans+=i[-1]
    return ans
target=int(input())
team=[]
for pos in arr:
    start,end=0,len(pos)
    while start<=end:
        mid=(start+end)//2
        if pos['PTS'].iloc[mid]>=(target/6):
            start=mid+1
        else:
            end=mid-1
    team.append([mid,
                 pos['Player'].iloc[mid-1],
                 pos['PTS'].iloc[mid-1]])
i=0
team1=team
while team_score(team1)<target:
    team=team1
    if i==5:
        i=0
    index=team[i][0]-1
    newscore=team_score(team)-arr[i]['PTS'].iloc[index+1]+arr[i]['PTS'].iloc[index]
    team1[i]=[index, arr[i]['Player'].iloc[index], arr[i]['PTS'].iloc[index]]
    i+=1
for p in team:
    print(p[1:])
