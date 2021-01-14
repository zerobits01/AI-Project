import sys
import collections
from queue import PriorityQueue
from itertools import count


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
        children = []

        try:
        
            b_child = GraphNode(
                node, (node.coordinate[0], node.coordinate[1] - 1))
            
            t_child = GraphNode(
                node, (node.coordinate[0], node.coordinate[1] + 1))
            
            l_child = GraphNode(
                node, (node.coordinate[0] - 1, node.coordinate[1]))
            
            r_child = GraphNode(
                node, (node.coordinate[0] + 1, node.coordinate[1]))

            if self.is_child_valid(b_child):
                children.append(b_child)

            if self.is_child_valid(t_child):
                children.append(t_child)

            if self.is_child_valid(r_child):
                children.append(r_child)

            if self.is_child_valid(l_child):
                children.append(l_child)
                 
            print(20*'#' + '\n' + "get children" + '\n' + 20*'#' + '\n')
            
        except Exception as e:
            print(20*'$')
            print(sys.exc_info()[-1].tb_lineno, e) 
            print(20*'$')            

        return children

    
    def get_specific_child(self, node: GraphNode, which_child):
        '''
            this will create specific child of the given node
            @param node: the node we wanna search for the children
            @type node: TreeNode
            @param which_child: L-eft, R-ight, B-ottom, T-op
            @type which_child: char
            @returns: list of children
            @rtype: list
        '''
        try:
        
            if which_child == 'B':
                b_child = GraphNode(
                    node, (node.coordinate[0], node.coordinate[1] - 1))
                if self.is_child_valid(b_child):
                    return b_child


            if which_child == 'T':
                t_child = GraphNode(
                    node, (node.coordinate[0], node.coordinate[1] + 1))
                if self.is_child_valid(t_child):
                    return t_child


            if which_child == 'L':            
                l_child = GraphNode(
                    node, (node.coordinate[0] - 1, node.coordinate[1]))
                if self.is_child_valid(l_child):
                    return l_child


            if which_child == 'R':            
                r_child = GraphNode(
                    node, (node.coordinate[0] + 1, node.coordinate[1]))
                if self.is_child_valid(r_child):
                    return r_child
                
            return None

        except Exception as e:
            print(20*'$')
            print(sys.exc_info()[-1].tb_lineno, e) 
            print(20*'$')   
            return None         
    
    
    def bfs_graph_search(self):
        '''
            solve the maze by bfs graph search
            
            @returns : solution path, cost, count of explored set 
        '''
        try:
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

            return [], 'Inf', list(explored_set)  # no answer found
        
        except Exception as e:
            print(20*'$')
            print(sys.exc_info()[-1].tb_lineno, e) 
            print(20*'$')
            return False

    
    def dls_graph_search_1(self, cut_off):
        '''This is the graph search implementation of dls Alg
            it is specificly implemented for solving Maze
            
            @returns : solution path, cost, count of explored set or False
        '''
        if cut_off < 1:
            return False
                
        set_limit = 0
        for i in range(0, cut_off+1):
            set_limit = set_limit + 4 ** i
        
        print(f"set limit \t{set_limit}\n")
        explored_set = set()
        level = 0
        try:
            level = level+1
            curr = self.SRC
            explored_set.add(curr.coordinate)
            
            if curr.coordinate == self.DST.coordinate:
                path, cost = self.create_path(self.SRC)
                return path, cost-1, list(explored_set)
            
            while True:
                
                print(len(explored_set), "\n", set_limit, "\n")
                
                if(len(explored_set) == set_limit):
                    break
                
                if level == cut_off:
                    level = level - 1
                    curr = curr.parent
                
                tmp = self.get_specific_child(curr, 'T')
                curr = tmp if tmp else curr
                if curr.coordinate not in explored_set:
                    print(f"TOP:\t{curr.coordinate}")
                    level = level + 1
                    explored_set.add(curr.coordinate)
                    if curr == self.DST:
                        path, cost = self.create_path(curr)
                        print(20*'#' + '\n' + "solved" + '\n' + 20*'#' + '\n')
                        return path, cost-1, list(explored_set)
                    continue

                tmp = self.get_specific_child(curr, 'R')
                curr = tmp if tmp else curr
                if curr.coordinate not in explored_set:
                    print(f"TOP:\t{curr.coordinate}")
                    level = level + 1
                    explored_set.add(curr.coordinate)
                    if curr == self.DST:
                        path, cost = self.create_path(curr)
                        print(20*'#' + '\n' + "solved" + '\n' + 20*'#' + '\n')
                        return path, cost-1, list(explored_set)
                    continue
                    
                tmp = self.get_specific_child(curr, 'B')
                curr = tmp if tmp else curr
                if curr.coordinate not in explored_set:
                    print(f"TOP:\t{curr.coordinate}")
                    level = level + 1
                    explored_set.add(curr.coordinate)
                    if curr == self.DST:
                        path, cost = self.create_path(curr)
                        print(20*'#' + '\n' + "solved" + '\n' + 20*'#' + '\n')
                        return path, cost-1, list(explored_set)

                    continue

                tmp = self.get_specific_child(curr, 'L')
                curr = tmp if tmp else curr
                if curr.coordinate not in explored_set:
                    print(f"TOP:\t{curr.coordinate}")
                    level = level + 1
                    explored_set.add(curr.coordinate)                    
                    if curr == self.DST:
                        path, cost = self.create_path(curr)
                        print(20*'#' + '\n' + "solved" + '\n' + 20*'#' + '\n')
                        return path, cost-1, list(explored_set)
                    continue
                
                level = level - 1
                curr = curr.parent   
                         
            return False
                
        except Exception as e:
            print(20*'$')
            print(sys.exc_info()[-1].tb_lineno, e) 
            print(20*'$')
            return False
    
        
    def ids_graph_search_1(self):
        '''
            solve the maze by ids graph search
            
            @returns : solution path, cost, count of explored set  or False
        '''
        try:
            for cut_off in count(start=1):
                print(20*"!@#$")
                print(f"new round\t{cut_off}")
                print(20*"!@#$")
                result = self.dls_graph_search_1(cut_off)
                
                if result != False and isinstance(result[1], int):
                    return result
                
                if result != False and result[2].__len__() == 400:
                    return [], 'Inf', result[2]  # no answer found

    
        except Exception as e:
            print(20*'$')
            print(sys.exc_info()[-1].tb_lineno, e) 
            print(20*'$')
            return False


    def dls_graph_search(self, src, destination, cut_off, explored_set):
        '''This is the graph search implementation of dls Alg
            it is specificly implemented for solving Maze
            
            @returns : solution path, cost, count of explored set or False
        '''
        try:
            explored_set.append(src.coordinate)

            if src == destination:
                path, cost = self.create_path(src)
                return True, path, cost, explored_set

            if cut_off <= 0:
                return False, None, None, explored_set

            children = self.get_children(src)

            for child in children:
                if child.coordinate not in explored_set:
                    flag, path, cost, explored_set = \
                        self.dls_graph_search(child, destination, cut_off-1, explored_set)
                    if flag:
                        return flag, path, cost, explored_set
            return False, None, None, explored_set

        except Exception as e:
            print(20*'$')
            print(sys.exc_info()[-1].tb_lineno, e) 
            print(20*'$')
            return False



    def ids_graph_search(self):
        '''
            solve the maze by ids graph search
            
            @returns : solution path, cost, count of explored set  or False
        '''

        # Store explored_set TreeNodes for each iteration
        explored_set = set()

        # Repeatedly depth-limit search till the reaches the goal's depth
        try:
            for i in count():
                tmp = self.dls_graph_search(self.SRC, self.DST, i, [])
                if tmp[0]:
                    return tmp[1], tmp[2], tmp[3]
        
        except Exception as e:
            print(20*'$')
            print(sys.exc_info()[-1].tb_lineno, e) 
            print(20*'$')
            return False    
        
        return False



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
- checking advance debugging in python
"""