import numpy as np
import random
import json


    
def saveInFile(row, column, s, g):
    data = {}
    data= {
        'start' : [s[0],s[1]],
        'goal' : [g[0],g[1]],
        'rows' : row,
        'columns' : column}
    with open('files//options.txt', 'w') as outfile:
        json.dump(data, outfile)
        print('Maze variables were saved in File.') 



try:    
    with open('files//options.txt','r') as json_file:
        text = json_file.read()
except FileNotFoundError:
    with open('files//options.txt', 'w') as outfile:
        outfile.write('')
    print('first define the variables:')
    rows = int(input('enter new row:'))
    columns = int(input('enter new columns:'))
    startx = int(input('enter the x of start position:'))
    starty = int(input('enter the y of start position:'))
    goalx = int(input('enter the x of goal position:'))
    goaly = int(input('enter the y of goal position:'))
    start = (startx,starty)
    goal = (goalx,goaly)
    saveInFile(rows, columns, start, goal)  
with open('files//options.txt','r') as json_file:    
    data = json.load(json_file)


visited = list()
notAvailable = list()
pathArray = list()
matrix = list()
a = list()

rows = data['rows']
columns = data['columns']
start = (data['start'][0],data['start'][1])
goal = (data['goal'][0],data['goal'][1])
print('parameters of the Maze:')
print('rows: ', rows)
print('columns: ', columns)
print('start: ', start)
print('goal: ', goal)  
      
matrix = np.random.randint(0,2,size=(rows,columns))
        

    
def build():
    pathArray.append(start)
    avDirect = list()
    i,j = start[0], start[1]
    while True:
        #direction = { left, right, up, down}
        if(check((i-1,j)) == 1 and check2((i-1,j),'L')==1):
            avDirect.append((i-1,j))
        elif((goal[0],goal[1]) in pathArray):
            return    
        if(check((i+1,j)) == 1 and check2((i+1,j),'R')==1):
            avDirect.append((i+1,j))
        elif((goal[0],goal[1]) in pathArray):
            return    
        if(check((i,j-1)) == 1 and check2((i,j-1),'D')==1):
            avDirect.append((i,j-1))
        elif((goal[0],goal[1]) in pathArray):
            return            
        if(check((i,j+1)) == 1 and check2((i,j+1),'U')==1):
            avDirect.append((i,j+1))
        elif((goal[0],goal[1]) in pathArray):
            return    
        
        
        
        if(len(avDirect)==0): 
            s = pathArray.pop()
            visited.append(s)
            notAvailable.append(s)
            currentD = pathArray[-1]
            i = currentD[0]
            j = currentD[1]
            continue
        
            
        currentD = findNext(avDirect)
        pathArray.append(currentD)
        avDirect = list()
        i = currentD[0]
        j = currentD[1]
        
        
            
            
            
def check(c):
    if(c[0]>=0 and c[1]>=0 and c[0]<=rows-1 and c[1]<=columns-1 \
        and not (c[0],c[1]) in pathArray \
            and not (c[0],c[1]) in notAvailable\
                and c!=(0,0)):
                    if((c[0]+1,c[1]) != (goal[0],goal[1]) and (c[0]-1,c[1]) != (goal[0],goal[1]) and (c[0],c[1]+1) != (goal[0],goal[1]) and (c[0],c[1]-1) != (goal[0],goal[1])):
                        return 1
                    elif((c[0]+1,c[1]) == (goal[0],goal[1])):
                            pathArray.append((c[0],c[1]))
                            pathArray.append((goal[0],goal[1]))
                            endFindingPath()
                            return 2 
                    elif((c[0]-1,c[1]) == (goal[0],goal[1])):
                            pathArray.append((c[0],c[1]))
                            pathArray.append((goal[0],goal[1]))
                            endFindingPath()
                            return 2 
                    elif((c[0],c[1]+1) == (goal[0],goal[1])):
                            pathArray.append((c[0],c[1]))
                            pathArray.append((goal[0],goal[1]))
                            endFindingPath()
                            return 2 
                    elif((c[0],c[1]-1) == (goal[0],goal[1])):
                            pathArray.append((c[0],c[1]))
                            pathArray.append((goal[0],goal[1]))
                            endFindingPath()    
                            return 2                   
    return 0
        
def check2(c, direction):

    if(direction == 'L' \
        and not (c[0]-1,c[1]) in pathArray \
            and not (c[0],c[1]-1) in pathArray \
                and not (c[0],c[1]+1) in pathArray):
                    return 1
    elif(direction == 'R' \
        and not (c[0]+1,c[1]) in pathArray \
            and not (c[0],c[1]-1) in pathArray \
                and not (c[0],c[1]+1) in pathArray):
                    return 1                
    elif(direction == 'U' \
        and not (c[0]+1,c[1]) in pathArray \
            and not (c[0]-1,c[1]) in pathArray \
                and not (c[0],c[1]+1) in pathArray):
                    return 1 
    elif(direction == 'D' \
        and not (c[0]+1,c[1]) in pathArray \
            and not (c[0]-1,c[1]) in pathArray \
                and not (c[0],c[1]-1) in pathArray):
                    return 1 
    return 0
        
def endFindingPath():  
    print('path was successfuly found!')
    print('\a')
    for each in pathArray:
        matrix[each[0]][each[1]] = 0
    print('Maze= ')
    print(matrix)    
    return

def findNext(dList):  
    v = random.choice(dList)
    return v
    
    
   
    