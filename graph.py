"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()


    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)


    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        q.enqueue(starting_vertex)

        # keep track of visited nodes
        visited = set()

        # repeat until que if empty
        while q.size() > 0:
            v = q.dequeue()

            if v not in visited:
                print(v)
                # mark as visited
                visited.add(v)
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)
 

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        s.push(starting_vertex)

        visited = set()

        while s.size() > 0:
            pop = s.pop()

            if pop not in visited:
                print(pop)
                visited.add(pop)
                for next_vert in self.get_neighbors(pop):
                    s.push(next_vert)
        

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # visited is a set
        visited = set()
        # add first number to the set
        visited.add(starting_vertex)
        # Helper for number
        def dft(number):   
            # print out first number   
            print(number) 
            # find next vertices in neighbors, add them to the visited list, and recursively call them. 
            for next_vertex in self.get_neighbors(number):
                if next_vertex not in visited:
                    visited.add(next_vertex)
                    dft(next_vertex)
        
        dft(starting_vertex)

        # CLASS
    # def dft_recursive(self, starting_vertex, visited=None):

    #     print(starting_vertex)
        
    #     if visited is None:
    #         visited = set()
        
    #     visited.add(starting_vertex)

    #     for next_vertex in self.vertices[starting_vertex]:
    #         if next_vertex not in visited:
    #             self.dft_recursive(next_vertex, visited)

        




    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # similar to BFT, but we want to check if the children have been seen BEFORE we add them to the queue

        # GOAL
        # create lists of traversals to a given route
        # if the route ends in the destination vertex, then return the shortest length list.



        # from MIT, parent pointers create shortest paths
        q = Queue()
        # Q's goal is to create a a list of vertices, finds the 
        q.enqueue([starting_vertex])

        while q.size() > 0:
            path = q.dequeue()
            print("PATH", path)
            node = path[-1]
            print("CURRENT NODE --> ", node)
            print(" ")
            print("queue", q.queue)
            if node == destination_vertex:
                return path
            
            for next_vert in self.get_neighbors(node):
                new_path = list(path)
                new_path.append(next_vert)
                q.enqueue(new_path)


    def dft_rooms(self, starting_vertex):
        """
        Return a list containing a path from
        starting_vertex and find the longest list. 
        """
        # still want the list 
        s = Stack()
        s.push([starting_vertex])
        master_list = []
        while s.size() > 0:
            curr_list = s.pop()
            last_room = curr_list[-1]

            for next_room in self.get_neighbors(last_room):
                new_path = list(curr_list)
                new_path.append(next_room)
                s.push(new_path)
                master_list.append(new_path)
        
        return master_list

        


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    # print(graph.vertices)
    # print(graph.get_neighbors(4))

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    graph.dft_recursive(1)

    # '''
    # Valid BFS path:
    #     [1, 2, 4, 6]
    # '''
    # print(graph.bfs(1, 6))

    # '''
    # Valid DFS paths:
    #     [1, 2, 4, 6]
    #     [1, 2, 4, 7, 6]
    # '''
    # print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
