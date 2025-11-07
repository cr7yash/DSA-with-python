class Graph:
    def __init__(self):
        self.adjacency_list = {}
        
    def addVertex(self,vertex):
        if vertex not in self.adjacency_list.keys():  # Check for duplicate key
            self.adjacency_list[vertex] = []
            return True
        return False
    
    def addEdge(self,vertex1,vertex2):
        """
        This function should accept two vertices, we can call them vertex1 and vertex2
        The function should find in the adjacency list the key of vertex1 and push vertex2 to the array
        The function should find in the adjacency list the key of vertex2 and push vertex1 to the array
        Don't worry about handling errors/invalid vertices
        """
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        return False
    
    def removeEdge(self,vertex1,vertex2):
        """
        This function should accept two vertices, we'll call them vertex1 and vertex2
        The function should reassign the key of vertex1 to be an array that does not contain vertex2
        The function should reassign the key of vertex2 to be an array that does not contain vertex1
        Don't worry about handling errors/invalid vertices
        """
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1] = [v for v in self.adjacency_list[vertex1] if v != vertex2]
            self.adjacency_list[vertex2] = [v for v in self.adjacency_list[vertex2] if v != vertex1]
            return True
        return False
    
    def removeVertex(self,vertex):
        """
        This function should accept a vertex to remove.
        It should remove all edges connected to that vertex, and then remove the vertex itself.
        """
        if vertex in self.adjacency_list:
            
            while len(self.adjacency_list[vertex]) > 0:
                adjacentVertex = self.adjacency_list[vertex].pop()
                self.removeEdge(vertex,adjacentVertex)
            del self.adjacency_list[vertex]
            return True
        return False
            
    
    

g = Graph()

g.addVertex("A")
print(g.adjacency_list)
g.addVertex("B")
print(g.adjacency_list)
g.addVertex("C")
print(g.adjacency_list)
g.addVertex("D")
print(g.adjacency_list)
g.addEdge("A","B")
print(g.adjacency_list)
g.addEdge("A","C")
print(g.adjacency_list)
g.addEdge("A","D")
print(g.adjacency_list)
g.addEdge("B","D")
print(g.adjacency_list)
g.addEdge("C","D")
print(g.adjacency_list)
g.addEdge("C","D")
print(g.adjacency_list)
g.removeEdge("D","C")
print(g.adjacency_list)
g.removeEdge("B","D")
print(g.adjacency_list)
g.removeVertex("D")
print(g.adjacency_list)
g.removeVertex("C")
print(g.adjacency_list)