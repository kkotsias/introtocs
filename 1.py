import random


gameArray = [[0, 0, 0], [0, 0 ,0], [0, 0 ,0]]

steps, stepsInLoop = 0, 0

for i in range(1, 100):
    stepsInLoop = 0
    steps = stepsInLoop + steps
    isDone = False
    ammountOfSmallR = 9
    ammountOfMediumR = 9
    ammountOfLargeR = 9
    ammountOfTotalRings = ammountOfSmallR + ammountOfMediumR + ammountOfLargeR

    while isDone == False:
        filled = 0
        stepsInLoop =+ stepsInLoop
        #picks random square from array
        line = random.randint(0,2)
        col  = random.randint(0,2)
        
        #picks random type of circle (1 = small, 2 = medium, 3 = large)
        typeOfCircle = random.randint(1,3)
        
        if gameArray[line][col] == 0:
            gameArray[line][col] = typeOfCircle
        else:
            filled =+ 1

        #checks if game ends diagonally
        if (gameArray[0][0] == gameArray[1][1] == gameArray[2][2] and gameArray !=0) or gameArray[0][0] < gameArray[1][1] < gameArray[2][2]:
            isDone = True
            stepsInLoop +=1
        #checks if game ends horizontally
        elif (gameArray[0][0] == gameArray[0][1] == gameArray[0][2] and gameArray !=0) or gameArray[0][0] < gameArray[0][1] < gameArray[0][2]:
            isDone = True
            stepsInLoop +=1
        elif (gameArray[1][0] == gameArray[1][1] == gameArray[1][2] and gameArray !=0) or gameArray[1][0] < gameArray[1][1] < gameArray[1][2]:
            isDone = True
            stepsInLoop +=1
        elif (gameArray[2][0] == gameArray[2][1] == gameArray[2][2] and gameArray !=0) or gameArray[2][0] < gameArray[2][1] < gameArray[2][2]:
            isDone = True
            stepsInLoop +=1
        #checks if game ends vertically
        elif (gameArray[0][0] == gameArray[1][0] == gameArray[2][0] and gameArray !=0) or gameArray[0][0] < gameArray[1][0] < gameArray[2][0]:
            isDone = True
            stepsInLoop +=1
        elif (gameArray[0][1] == gameArray[1][1] == gameArray[2][1] and gameArray !=0) or gameArray[0][1] < gameArray[1][1] < gameArray[2][1]:
            isDone = True
            stepsInLoop +=1
        elif (gameArray[0][2] == gameArray[1][2] == gameArray[2][2] and gameArray !=0) or gameArray[0][2] < gameArray[1][2] < gameArray[2][2]:
            isDone = True
            stepsInLoop +=1

        if filled == 27 and isDone == False:
            isDone == True
            stepsInLoop = 0


medianStepsIn100 = steps / 100
print(medianStepsIn100, "steps needed to end the game")

        
                
        


