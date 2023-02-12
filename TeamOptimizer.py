import random, copy

players = {} # key:value, key:value
teamCount = 0
add_ons = []

population = []
playerCount = 0

playersPerTeam = 0

availablePlayers = []
def simulate(p, t, a):
    global players, teamCount, add_ons, playerCount, playersPerTeam, availablePlayers, population
    population = []
    players = p
    teamCount = t
    add_ons = a
    playerCount = len(players)
    playersPerTeam = int(playerCount/teamCount)
    availablePlayers = list(players.keys())
    for i in range(30):
        population.append([])
        population[i] = createRandomTeams(population[i])
    population.pop()
    a = chooseBestTeamSet(population)
    
    for i in range(1,3000):
        
        population = repopulate(population)
        a = chooseBestTeamSet(population)
    return a



def getScore(team):
    score = sum(team)
    for addon in add_ons: # [[1,2], 5]
        score += addon[1]
        for player in addon[0]:
            if team.count(player) == 0:
                score -= addon[1]
                break
    return score

def createRandomTeams(teamSet):
    ap = copy.deepcopy(availablePlayers)
    for i in range(teamCount):
        teamSet.insert(0,[])
        for j in range(playersPerTeam):
            teamSet[0].insert(0,ap.pop(random.randint(0,len(ap)-1)))
    return teamSet


def calculateDisparity(teamSet): #basically, how wacko the teams are
    dif = 0.0
    av = 0.0
    teamsScore = []
    for i in teamSet:
        teamsScore.append(getScore(i))
        
    av = sum(teamsScore)/teamCount
    for i in range(0, len(teamsScore)):
        dif += abs(teamsScore[i] - av)
##        print(dif)
    return abs(dif)
    




def chooseBestTeamSet(popu):
    d = float('inf')
    minDif = float('inf')
    bestTeamSet = []
    n = 0
    for ts in popu:
        d = calculateDisparity(ts)
        
        #print(n, " disparity is ", d)
        #print()
        n +=1
        #print()
        if(d < minDif):
            bestTeamSet = ts
            minDif = d

    
    return bestTeamSet




def mutate_attempt(arr):   #a probabalistic swap function
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if random.random() < 0.15:
                k = random.randint(0, len(arr) - 1)
                l = random.randint(0, len(arr[0]) - 1)
                while k == i and l == j:
                    k = random.randint(0, len(arr) - 1)
                    l = random.randint(0, len(arr[0]) - 1)
                # Swap the elements
                arr[i][j], arr[k][l] = arr[k][l], arr[i][j]
    return arr

def repopulate(popu):
    popu[0] = chooseBestTeamSet(popu)
    #print("pop 0 disparity is ", calculateDisparity(popu[0]))
    for x in range(1, len(popu)):
        popu[x] = mutate_attempt(copy.deepcopy(popu[0]))
    return popu




















##run if u want


##
##
##someplayerstuff = {0:7, 1:5, 2:4, 3:6, 4:9, 5:11, 6:3, 7:5, 8:2, 9:1, 10:4, 11:7}
##someteamcount = 4
##someadds = [[[1,2],5], [[3,4],-3], [[5,2],9], [[5,3],9]]
##
##smth = simulate(someplayerstuff, someteamcount, someadds)
##
##print(smth)
##print(calculateDisparity(smth))

    
    


