# convoy game of life
import random, time, copy
WIDTH=60
HEIGHT=20
#create a list of  list for the cells details
nextCells=[]
for x in range(WIDTH):
    column=[]
    for y in range(HEIGHT):
        if random.randint(0,1)==0:
            column.append("#")    # add a living cells
        else:
            column.append(" ") # add a dead cell
    nextCells.append(column)#next cell is a coloumn of new list

while True:#main program loop.
    print('\n\n\n\n\n')#seperste each step[mwith new line
    currentCells=copy.deepcopy(nextCells)
    #print current cells on the screen
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y],end="")
        print()                               
         #calculate the next step cells based on current steps cells
    for x in range(WIDTH):
        for y in range(HEIGHT):
            #get neighbouring candidate
            leftCoord=(x-1)%WIDTH
            rightCoord=(x+1)%WIDTH
            aboveCoord=(y-1)% HEIGHT
            belowCoord=(y+1)% HEIGHT
            #count number of living neighbors
            numNeighbors=0
            if currentCells[leftCoord][aboveCoord]=='#':
                numNeighbors+=1
            if currentCells[x][aboveCoord]=='#':
                numNeighbors+=1
            if currentCells[rightCoord][aboveCoord]=='#':
                numNeighbors+=1
            if currentCells[leftCoord][y]=='#':
                numNeighbors+=1
            if currentCells[rightCoord][y]=='#':
                numNeighbors+=1
            if currentCells[leftCoord][belowCoord]=='#':
                numNeighbors+=1
            if currentCells[x][belowCoord]=='#':
                numNeighbors+=1
            if currentCells[rightCoord][belowCoord]=='#':
                numNeighbors+=1
            if currentCells[x][y]=='#'and (numNeighbors==2 or numNeighbors==3):
                nextCells[x][y]='#'
            elif currentCells[x][y]==' ' and numNeighbors ==3:
                nextCells[x][y]='#'
            else:
                nextCells[x][y]=' '
        time.sleep(1)                                                    