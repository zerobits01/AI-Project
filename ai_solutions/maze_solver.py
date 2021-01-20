import sys
import collections
from queue import PriorityQueue
from itertools import count
from ai_solutions.graph_node import GraphNode

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
            @type node: GraphNode
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
            @type node: GraphNode
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

    
    def dls_graph_search(self, cut_off):
        '''This is the graph search implementation of dls Alg
            it is specificly implemented for solving Maze
            
            @returns : solution path, cost, count of explored set or False
        '''
        if cut_off < 1:
            return False
                
        set_limit = 0
        for i in range(0, cut_off+1):
            set_limit = set_limit + 4 ** i
        
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
                    continue
                
                tmp = self.get_specific_child(curr, 'T')
                if tmp and tmp.coordinate not in explored_set:
                    curr = tmp
                    print(f"TOP:\t{curr.coordinate}")
                    level = level + 1
                    explored_set.add(curr.coordinate)
                    if curr == self.DST:
                        path, cost = self.create_path(curr)
                        print(20*'#' + '\n' + "solved" + '\n' + 20*'#' + '\n')
                        return path, cost-1, list(explored_set)
                    continue

                tmp = self.get_specific_child(curr, 'R')
                if tmp and tmp.coordinate not in explored_set:
                    curr = tmp
                    print(f"TOP:\t{curr.coordinate}")
                    level = level + 1
                    explored_set.add(curr.coordinate)
                    if curr == self.DST:
                        path, cost = self.create_path(curr)
                        print(20*'#' + '\n' + "solved" + '\n' + 20*'#' + '\n')
                        return path, cost-1, list(explored_set)
                    continue
                    
                tmp = self.get_specific_child(curr, 'B')
                if tmp and tmp.coordinate not in explored_set:
                    curr = tmp
                    print(f"TOP:\t{curr.coordinate}")
                    level = level + 1
                    explored_set.add(curr.coordinate)
                    if curr == self.DST:
                        path, cost = self.create_path(curr)
                        print(20*'#' + '\n' + "solved" + '\n' + 20*'#' + '\n')
                        return path, cost-1, list(explored_set)

                    continue

                tmp = self.get_specific_child(curr, 'L')
                if tmp and tmp.coordinate not in explored_set:
                    curr = tmp
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
    
        
    def ids_graph_search(self):
        '''
            solve the maze by ids graph search
            
            @returns : solution path, cost, count of explored set  or False
        '''
        try:
            for cut_off in count(start=1):
                print(20*"!@#$")
                print(f"new round\t{cut_off}")
                print(20*"!@#$")
                result = self.dls_graph_search(cut_off)
                
                if result != False and isinstance(result[1], int):
                    return result
                
                if result != False and result[2].__len__() == 400:
                    return [], 'Inf', result[2]  # no answer found

    
        except Exception as e:
            print(20*'$')
            print(sys.exc_info()[-1].tb_lineno, e) 
            print(20*'$')
            return False


    def aStar_graph_search(self):
        '''
            solve the maze by a* graph search
            
            @returns : solution path, cost, count of explored set 
        '''
        try:
            open = []
            explored_set = []

            open.append(self.SRC)

            while open:
                current_cell = open.pop(0)

                if current_cell.coordinate not in explored_set:
                    explored_set.append(current_cell.coordinate)

                if current_cell.coordinate == self.DST.coordinate:
                        path, cost = self.create_path(current_cell)
                        print(20*'#' + '\n' + "solved" + '\n' + 20*'#' + '\n')
                        return path, cost-1, list(explored_set)

                children = self.get_children(current_cell)
                for child in children:
                    child.payed = abs(child.coordinate[0] - self.SRC.coordinate[0]) + abs(
                        child.coordinate[1] - self.SRC.coordinate[1])
                    child.hurestic = abs(child.coordinate[0] - self.DST.coordinate[0]) + abs(
                        child.coordinate[1] - self.DST.coordinate[1])
                    child.total = child.payed + child.hurestic

                    flag = True
                    for tmp in open:
                        if (child == tmp and child.total >= tmp.total):        
                            flag = False 
                            break
                    
                    if flag:
                        if child.coordinate not in explored_set:
                            open.append(child)
                            sorted(open, key=lambda GraphNode_ob: GraphNode_ob.total)
                                
            return [], 'Inf', list(explored_set)
        
        except Exception as e:
            print(20*'$')
            print(sys.exc_info()[-1].tb_lineno, e) 
            print(20*'$')
            return False    
        
        return False



"""
points to pay attention
- set is not serializable so use list at last step
- checking advance debugging in python
"""

# source: https://towardsdatascience.com/a-star-a-search-algorithm-eb495fb156bb
# source: https://www.annytab.com/a-star-search-algorithm-in-python/

# we have to check something important
'''
    what if they set the start at 1,1 and the walls arround it?
'''

