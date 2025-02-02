import sys
class Dijkstras_algo:

  def __init__(self,vertices):
    self.V=vertices
    self.graph= [[0 for column in range(vertices)]
                    for row in range(vertices)]

  def minDistance(self, dist, sptSet):
    min = sys.maxsize
    for v in range(self.V):
      if dist[v] < min and sptSet[v] == False:
        min = dist[v]
        min_index = v

    return min_index
 

  def display(self,src,dist):
    for v in range (self.V):
      print("Distance of source {} to vertice {} is = {}".format(src,v,dist[v]))

  def dijkstras(self,src):
    visited =[False]*self.V
    dist = [sys.maxsize] * self.V
    dist[src]=0
    
    for iter in range (self.V):
      u = self.minDistance(dist,visited)
      visited[u]=True
      for v in range(self.V):
        if self.graph[u][v] > 0 and visited[v] is False and dist[v]> self.graph[u][v] +  dist[u]:
          dist[v]=dist[u]+self.graph[u][v] 
    self.display(src,dist)


g = Dijkstras_algo(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]
 
g.dijkstras(0)
 

      

     
