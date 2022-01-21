import numpy as np


class NODE:

  def __init__(self):
    self.state = None
    self.action = None
    self.parent = None
    self.path_cost = 0
    self.depth = 0
  
  def parity(self):
    I=0
    for i in range (n) :
      for j in range (n) :
        if self.state[i,j] == 0:
          d = 2*n-i-j-2    #Assigning d value for the given state
        if j == n-1 and i != n-1:
          p = i+1
          q = 0
        elif j == n-1 and i == n-1 :
          p = i
          q = j
        else :
          p = i
          q = j+1
        for k in range (p,n):
          for l in range (q,n):
            if self.state[k,l] > self.state[i,j] and self.state[k,l] != 0:
              I+=1    #Calculating the value of I for the given state
    return (d + I) % 2   #Returning the value of the parity


class Queue:

  def __init__(self):
    self.items = []

  def isEmpty(self):
    return self.items == []
	
  def enqueue(self, item):
    self.items.insert(0,item)
  
  def dequeue(self):
    return self.items.pop()
  
  def size(self):
    return len(self.items)


class Puzzle :

  def __init__(self,Sstate,Gstate) :
    self.Sstate = Sstate
    self.Gstate = Gstate
  
  def GoalTest(self,N):
    for i in range(n):
      for j in range(n):
        if N.state[i,j] != self.Gstate[i,j]:
          return 0  
    return 1
  
  def Swap(self,Node,action):
    arr = Node.state
    arr2 = np.zeros((n,n),dtype=int)
    for i in range(n):
      for j in range(n):
        if Node.state[i,j] == 0:
          D = (i,j)
          break
    print D
    if action == "Up":
      if D[0] != 0:
        arr[D[0],D[1]] = arr[D[0]-1,D[1]]
        arr[D[0]-1,D[1]] = 0    
        return arr
      else:
        return arr2  
    elif action == "Down":
      if D[0] != n-1:
        arr[D[0],D[1]] = arr[D[0]+1,D[1]]
        arr[D[0]+1,D[1]] = 0    
        return arr
      else:
        return arr2
    elif action == "Right":
      if D[1] != n-1:
        arr[D[0],D[1]] = arr[D[0],D[1]+1]
        arr[D[0],D[1]+1] = 0    
        return arr
      else:
        return arr2
    elif action == "Left":
      if D[1] != 0:
        arr[D[0],D[1]] = arr[D[0],D[1]-1]
        arr[D[0],D[1]-1] = 0    
        return arr
      else:
        return arr2

  def Successors(self,Node):
    List = []
    List.append((self.Swap(Node,"Up"),"Up"))
    List.append((self.Swap(Node,"Down"),"Down"))
    List.append((self.Swap(Node,"Right"),"Right"))
    List.append((self.Swap(Node,"Left"),"Left"))    
    return List

  def Solution(self,Node):
    path = []
    while Node.parent != None:
      path.append(Node.action)
      Node = Node.parent  
    return path
  
  def TreeSearch (self,fringe):
    N = NODE()
    N.state = self.Sstate
    fringe.enqueue(N)
    while True:
      if fringe.isEmpty() == 1:
        return None
      else:
        N = fringe.dequeue()
        if self.GoalTest(N) == 1 :
          return self.Solution(N)
        E = self.Expand(N)
        for i in E:
          fringe.enqueue(i)

  def Expand(self,N):
    successors = []
    for i in self.Successors(N):
      if (i[0])[0,0] != 0 and (i[0])[0,1] !=0:
        N1 = NODE()
        N1.state = i[0]
        N1.parent = N
        N1.action = i[1]
       # N1.path_cost = N.path_cost + 1
        #N1.depth = N.depth + 1
        successors.append(N1)
    return successors

              
n = raw_input("Type the number of rows or columns of the puzzle: ")
n = int(n)
GS = np.arange(n*n).reshape(n,n)
SS = np.array([[1,0],[2,3]]) 
print SS
print GS
#SS = np.random.permutation(GS)         
GAME = Puzzle(SS,GS)
Q = Queue() 
print GAME.TreeSearch(Q)
           

