import pygame
import time
import Maze as maze
import AStar as AS

visited = AS.visited
matrix = maze.matrix
pathArray = AS.pathArray
rows = len(matrix)
columns = len(matrix[0])
nodeList = list()
state = 'searching'
start = maze.start
end = maze.goal

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)


pygame.init()
logoPicture = pygame.image.load('images//logo.png')
pygame.display.set_icon(logoPicture)
pygame.display.set_caption('Maze')

if(rows <=10):
    SCREEN_HEIGHT = 300
elif(rows <=30):
    SCREEN_HEIGHT = 450
elif(rows <=50):
    SCREEN_HEIGHT = 700
else:
    SCREEN_HEIGHT = 800

if(columns <=10):
    SCREEN_WIDTH = 300
    delay = 0.7
elif(columns <=30):
    SCREEN_WIDTH = 450
    delay = 0.3
elif(columns <=50):
    SCREEN_WIDTH = 700
    delay = 0
else:
    SCREEN_WIDTH = 800 
    delay = 0


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((255, 0, 0))

picture0 = pygame.Surface((int(SCREEN_WIDTH/columns), int(SCREEN_HEIGHT/rows)))
picture0.fill((0, 214, 253))
picture1 = pygame.Surface((int(SCREEN_WIDTH/columns), int(SCREEN_HEIGHT/rows)))
picture1.fill((0, 0, 0))

wallPic = pygame.image.load('images//wall.png')
startPic = pygame.image.load('images//start.png')
endPic = pygame.image.load('images//end.png')
pictureWall = pygame.transform.scale(wallPic,(int(SCREEN_WIDTH/columns),int(SCREEN_HEIGHT/rows)))
picturestart = pygame.transform.scale(startPic,(int(SCREEN_WIDTH/columns),int(SCREEN_HEIGHT/rows)))
pictureEnd = pygame.transform.scale(endPic,(int(SCREEN_WIDTH/columns),int(SCREEN_HEIGHT/rows)))



def updateScreen():
    for each in range(rows):
        for j in range(columns):
            s = nodeList[each][j]
            screen.blit(s, (j*int(SCREEN_WIDTH/columns),each*int(SCREEN_HEIGHT/rows)))
            pygame.display.flip()
                

for each in range(rows):
    temp = list()
    for j in range(columns):
        if(matrix[each][j] == 0):
            surf = pygame.Surface((int(SCREEN_WIDTH/columns), int(SCREEN_HEIGHT/rows)))
            surf.blit(picture0, (2, 2))
            temp.append(surf)
        else:    
            surf = pygame.Surface((int(SCREEN_WIDTH/columns), int(SCREEN_HEIGHT/rows)))
            surf.blit(picture1,(2,2))
            temp.append(surf)
    nodeList.append(temp)

s1 = pygame.Surface((int(SCREEN_WIDTH/columns), int(SCREEN_HEIGHT/rows)))
s1.blit(picturestart, (0, 0))
s2 = pygame.Surface((int(SCREEN_WIDTH/columns), int(SCREEN_HEIGHT/rows)))
s2.blit(pictureEnd, (0, 0))
nodeList[end[0]][end[1]] = s2

    


running = True
# Main loop
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False
    if(len(visited) == 0):
        state = 'end'
    updateScreen()    
    while len(visited)>0:
        x = visited[0]
        visited.remove(x)
        s1 = pygame.Surface((int(SCREEN_WIDTH/columns), int(SCREEN_HEIGHT/rows)))
        s1.fill((120,120,120))
        s2 = pygame.Surface((int(SCREEN_WIDTH/columns)-4, int(SCREEN_HEIGHT/rows)-4))
        s2.fill((255, 159, 164))
        s1.blit(s2, (2,2))
        nodeList[x[0]][x[1]] = s1    
        break
    if(state == 'end'):
        for each in pathArray:
            y = pathArray.pop()
            s1 = pygame.Surface((int(SCREEN_WIDTH/columns), int(SCREEN_HEIGHT/rows)))
            s1.fill((250,10,150))
            s2 = pygame.Surface((int(SCREEN_WIDTH/columns)-4, int(SCREEN_HEIGHT/rows)-4))
            s2.fill((200,20,75))
            s1.blit(s2, (2,2))
            nodeList[y[0]][y[1]] = s1    
            break
    time.sleep(delay)
    

pygame.quit()