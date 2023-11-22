import Maze as maze

visited = list()
pathArray = list()
stack = list()
start = maze.start
goal = maze.goal
matrix = maze.matrix
rows = maze.rows
columns = maze.columns



class Node:
    x = -1
    y = -1
    parent = None
    g = -1
    f = -1
    
    def setParent(self, p):
        self.parent = p
        
    def __init__(self,x,y,g,f):
        self.x = x
        self.y = y
        self.g = g
        self.f = f
        
    #End of class    

def findPath():
    current = Node(start[0],start[1],0,goal[0]+goal[1])
    stack.append(current)
    visited.append(start)
    while not goal in visited:
        current = popFromStack()
        addChildren(current)
        
    current = findGoal()    
    while True:
        pathArray.append((current.x,current.y))
        if(current.parent == None):
            break
        current = current.parent
    
    import UI


        
        
        
        
def popFromStack():
    current = stack[0]
    for each in stack:        
        if(each.f<current.f):
            current = each
    stack.remove(current)
    return current    
    
    
def addChildren(curr):
    i = curr.x
    j = curr.y
    if(check((i+1,j)) and check2((i+1,j),'R')==1):
        node = Node(i+1,j,(curr.g)+1,((curr.g)+1+(goal[0]-i)+(goal[1]-j)))
        node.setParent(curr)
        stack.append(node)
        visited.append((i+1,j))
    if(check((i,j+1)) and check2((i,j+1),'U')==1):
        node = Node(i,j+1,(curr.g)+1,((curr.g)+1+(goal[0]-i)+(goal[1]-j)))
        node.setParent(curr)
        stack.append(node)
        visited.append((i,j+1))
    if(check((i-1,j)) and check2((i-1,j),'L')==1):
        node = Node(i-1,j,(curr.g)+1,((curr.g)+1+(goal[0]-i)+(goal[1]-j)))
        node.setParent(curr)
        stack.append(node)
        visited.append((i-1,j))        
    if(check((i,j-1)) and check2((i,j-1),'D')==1):
        node = Node(i,j-1,(curr.g)+1,((curr.g)+1+(goal[0]-i)+(goal[1]-j)))
        node.setParent(curr)
        stack.append(node)
        visited.append((i,j-1))
    
def check(c):
    i,j = c[0], c[1]    
    if(not (i,j) in visited \
    and (i,j) != start \
    and i>=0 and i<=rows-1 \
    and j>=0 and j<=columns-1):
        if(matrix[i][j] == 0):
            return True
    return False
    
    
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
    
    
def findGoal():
    for each in stack:
        if(each.x == goal[0] and each.y == goal[1]):
            return each
