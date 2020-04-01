# Round robin tournament problem for Coding is Fun
#
# Date: 2020/04/01
#By Oliver Long longoliver2005@gmail.com 

N = int(input("How many teams?: "))
Rounds = int(input("How many rounds?: "))
#create a 2d array representing playable games
games = [0] * N
for i in range(N):
    games[i] = [0] * N

    # a team cannot play itself
    games[i][i] = 1


# Header
print("********************************")
print("Results")
print("********************************")

def findGames():
    nextTryX = 0
    nextTryY = 0
    while True:
        if len(roundGames) == int(N/2):
            return True
        if findOneGame(nextTryX,nextTryY) == -1:
            #not found
            #print("popped to game ", len(roundGames))
            if len(roundGames) == 0:
                return False
            nextTryX = roundGames[len(roundGames) - 1][0]
            nextTryY = roundGames[len(roundGames) - 1][1] + 1
            teamsPlayed[roundGames[len(roundGames) - 1][0]] = 0
            teamsPlayed[roundGames[len(roundGames) - 1][1]] = 0

            roundGames.pop()
            
        else:
            nextTryX = 0
            nextTryY = 0
            #print("game number ", end ="")
            #print(len(roundGames), end = "")
            #print("x = ", end = "")
            #print(roundGames[len(roundGames) - 1][0], end = "")
            #print(", y = ", end = "")
            #print(roundGames[len(roundGames) - 1][1])
        

def findOneGame(newX, newY):
    #print("Looking for game starting from:", newX, " ", newY, end="")
    
    for l in  range(newX ,N):
        for m in range(newY, N):

            x = l
            y = m
            

            # Check if game has been played, or is valid
            if games[x][y] == 0 and teamsPlayed[x] == 0 and teamsPlayed[y] == 0:

                

                teamsPlayed[x] = 1
                teamsPlayed[y] = 1
                
                roundGames.append([x,y])
                #print(" found ", x, ", ",y)
                return [x,y]
                
    #print(" Not found ")
    return -1


# Loop through rounds
for j in range(Rounds):

    # Reset array
    teamsPlayed = [0] * N
    roundGames = []
    if findGames() == False:
        print("Can't find games for round" ,j + 1)
        break

    

    print("Round ", end = "")
    print(j + 1)
    print("********************************")

    

    for i in range(len(roundGames)):
        print("Team ", end = "")
        print(roundGames[i][0] + 1 , end = "")
        print(" vs. Team ", end = "")
        print(roundGames[i][1] + 1, end = " |   ")
        # Mark the game as played
        games[roundGames[i][0]][roundGames[i][1]] = 1
        games[roundGames[i][1]][roundGames[i][0]] = 1


    print("\n********************************\n")
    #print(teamsPlayed)
    #print()
    #for n in range(N):
    #    print(games[n])
    

#for n in range(N):
 #   print(games[n])

