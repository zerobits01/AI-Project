import sys
import collections
from queue import PriorityQueue


class GraphNode:
    '''
        This class is the tree GraphNode
        I will use this for creating my search trees in MazeSolver
    '''

    
    def __init__(self, parent, coordinate):
        '''
            initializing the GraphNode based on the parent and coordinate
            @param parent: GraphNodes parent which can be None
            @type parent: GraphNode
            @param coordinate: two element list which first one is row the other is col
            @type coordinate: list
        '''
        
        self.parent = parent
        self.coordinate = coordinate
        self.hurestic = 0
        self.payed = 0 # payed till here
        self.total = 0 # the whole cost


    def __le__(self, other: object):
        '''
            checking if other GraphNode is less than this GraphNode or not
            @type other: GraphNode
        '''
        return self.coordinate[0] <= other.coordinate[0] \
            and self.coordinate[1] <= other.coordinate[1]


    def __ge__(self, other: object):
        '''
            checking if other GraphNode is greater than this GraphNode or not
            @type other: GraphNode
        '''
        return self.coordinate[0] >= other.coordinate[0] \
            and self.coordinate[1] >= other.coordinate[1]

    def __eq__(self, other: object):
        return self.coordinate[0] == other.coordinate[0] \
            and self.coordinate[1] == other.coordinate[1]


class MazeSolver:
    '''
        this class is for solving the maze question
        using three algorithms:
        - BFS
        - IDS
        - A*
    '''
    def __init__(self, source, destination, black_cells, size=20):
        '''
            Initial the source and destination cells
            @param source: source cell, two element (row, col)
            @type source: tuple
            @param destination: dst, two elemets (row, col)
            @type destication: tuple
            @param BLACKED: list of black cells in the maze like [(row, col), (row, col), etc]
            @type type: tuple
            @param size: the maze dimention size, this will create size*size maze
            @type size: integer
        '''

        # variables
        self.FIRST = (0, 0)
        self.LAST = (size - 1, size - 1)
        
        self.BLACKED = set([(x[0], x[1]) for x in black_cells])
        
        self.SRC = GraphNode(None, (source[0], source[1]))
        self.DST = GraphNode(None, (destination[0], destination[1]))
        
        self.size = size

        print(20*'#' + '\n' + "MazeSolver creation" + '\n' + 20*'#' + '\n')
        
    
    def create_path(self, node: GraphNode):
        """creates the solution path based on the parents till it visits SRC
            
            @param node: dst node wchich we wanna find path to it from source
            @type node: GraphNode
            @returns: list of the coordinates to go in correct order
            @rtype: list
        """
        path = []
        cost = 0
        
        while node:
            path.insert(0, node.coordinate)
            node = node.parent
            cost = cost + 1

        print(20*'#' + '\n' + "path creation" + '\n' + 20*'#' + '\n')
        
        return path, cost
    
    
    def is_child_valid(self, node: GraphNode):
        '''
            checks if the created node is valid or not
            @param node: input node to check
            @type node: GraphNode
            @returns: boolean value which shows if the created node is valid or not
            @rtype: bool
        '''

        print(20*'#' + '\n' + "is valid" + '\n' + 20*'#' + '\n')
        
        if node.coordinate[0] < 0 or node.coordinate[1] < 0 or \
            node.coordinate[0] >= self.size or node.coordinate[1] >= self.size or \
                node.coordinate == node.parent.coordinate or node.coordinate in self.BLACKED :
            return False

        return True    
    
     
    def get_children(self, node: GraphNode):
        '''
            this will create the child nodes then return them as a list
            @param node: the node we wanna search for the children
            @type node: TreeNode
            @returns: list of children
            @rtype: list
        '''
        try:
            children = []
        
            b_child = GraphNode(
                node, (node.coordinate[0] - 1, node.coordinate[1]))
            
            t_child = GraphNode(
                node, (node.coordinate[0] + 1, node.coordinate[1]))
            
            l_child = GraphNode(
                node, (node.coordinate[0], node.coordinate[1] - 1))
            
            r_child = GraphNode(
                node, (node.coordinate[0], node.coordinate[1] + 1))



            if self.is_child_valid(b_child):
                children.append(b_child)

            if self.is_child_valid(t_child):
                children.append(t_child)

            if self.is_child_valid(r_child):
                children.append(r_child)

            if self.is_child_valid(l_child):
                children.append(l_child)
                
                
            print(20*'#' + '\n' + "get children" + '\n' + 20*'#' + '\n')
            
            return children

        except Exception as e:
            print(20*'$')
            print(sys.exc_info()[-1].tb_lineno, e) 
            print(20*'$')            
    
    
    def bfs_graph_search(self):
        '''
            solve the maze by bfs graph search
            
            @returns : solution path, cost, count of explored set 
        '''
        try:     
            print(20*'#' + '\n' + "start bfs" + '\n' + 20*'#' + '\n')
            
            queue = collections.deque([self.SRC])
            explored_set = set()
            
            while queue:
                            
                curr = queue.popleft()
                
                if curr == self.DST:
                    # returning path, cost and explored_set count
                    
                    path, cost = self.create_path(curr)
                    print(20*'#' + '\n' + "solved" + '\n' + 20*'#' + '\n')
                    return path, cost-1, list(explored_set)
                
                explored_set.add(curr.coordinate)

                # add current cell's child to queue to visit
                children = self.get_children(curr)

                for child in children:
                    if child.coordinate not in explored_set:
                        queue.append(child)

            print(20*'#' + '\n' + "no solution" + '\n' + 20*'#' + '\n')
            return [], 'Inf', 400  # no answer found
        except Exception as e:
            print(20*'$')
            print(sys.exc_info()[-1].tb_lineno, e) 
            print(20*'$')

    
    def ids_graph_search(self):
        '''
            solve the maze by ids graph search
            
            @returns : solution path, cost, count of explored set 
        '''
        queue = collections.deque([self.SRC])
        explored_set = set()
        

    
    def aStar_graph_search(self):
        '''
            solve the maze by a* graph search
            
            @returns : solution path, cost, count of explored set 
        '''
        queue = collections.deque([self.SRC])
        explored_set = set()


"""
points to pay attention
- set is not serializable so use list at last step
"""