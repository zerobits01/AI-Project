import collections
from queue import PriorityQueue


class Node:
    '''
        This class is the tree node
        I will use this for creating my search trees in MazeSolver
    '''
    
    def __init__(self, parent, position):
        '''
            initializing the node based on the parent and position
            :param parent: nodes parent which can be None
            :type parent: Node
            :param position: two element list which first one is row the other is col
            :type position: list
        '''
        self.parent = parent
        self.position = position

        self.h = 0 # hurestic 
        self.g = 0 # payed till here
        self.f = 0 # the whole cost

    def __le__(self, other: object):
        '''
            checking if other node is less than this node or not
            :type other: Node
        '''
        return self.position[0] <= other.position[0] \
            and self.position[1] <= other.position[1]

    def __ge__(self, other: object):
        '''
            checking if other node is greater than this node or not
            :type other: Node
        '''
        return self.position[0] >= other.position[0] \
            and self.position[1] >= other.position[1]


class MazeSolver:
    '''
        this class is for solving the maze question
        using three algorithms:
        - BFS
        - IDS
        - A*
    '''


    def __init__(self, source, destination, black_cells, size):
        '''
            Initial the source and destination cells
            :param source: source cell, two element (row, col)
            :type source: list
            :param destination: dst, two elemets (row, col)
            :type destication: list
            :param black_cells: list of black cells in the maze like [(row, col), (row, col), etc]
            :type type: list
            :param size: the maze dimention size, this will create size*size maze
            :type size: integer
        '''
        
        # variables
        self.FIRST_CELL = (0, 0)
        self.LAST_CELL = (size - 1, size - 1)
        self.black_cells = black_cells
        self.source_cell = Node(Node(None, None), source)
        self.destination_cell = Node(Node(None, destination), destination)



    def init_child(self, current):
        '''
            Returns children of the given cell
            :param current: current cell you wanna check
            :type current: Node
                    
        '''

        children = []
        
        bottom_cell = Node(
            current, (current.position[0] - 1, current.position[1]))
        
        top_cell = Node(
            current, (current.position[0] + 1, current.position[1]))
        
        left_cell = Node(
            current, (current.position[0], current.position[1] - 1))
        
        right_cell = Node(
            current, (current.position[0], current.position[1] + 1))

        # check cells are in range FIRST_CELL to LAST_CELL
        # and prevent to add parent to child
        # and not in filled cells
        # children are added in clockwise order
        if bottom_cell >= self.FIRST_CELL and not bottom_cell.position == current.parent.position:
            children.append(bottom_cell)
            
        if left_cell >= self.FIRST_CELL and not left_cell.position == current.parent.position:
            children.append(left_cell)
        
        if top_cell <= self.LAST_CELL and not top_cell.position == current.parent.position:
            children.append(top_cell)
        
        if right_cell <= self.LAST_CELL and not right_cell.position == current.parent.position:
            children.append(right_cell)

        # remove children which are in filled cells
        child = [
            c for c in children if not self.black_cells.__contains__(c.position)]
        return child

    def retrieve_path(self, current_cell):
        """Retrieve path from root to goal"""

        path = []
        while current_cell.position is not self.source_cell.position:
            path.append(current_cell.position)
            current_cell = current_cell.parent

        path.append(self.source_cell.position)
        path.reverse()
        return path  # Return reversed path

    def bfs_search(self):
        """ BFS Search """

        queue = collections.deque([self.source_cell])
        explored_set = []
        flag = False

        explored_set.append(self.source_cell)
        while queue:
            current = queue.popleft()
            if current.position == self.destination_cell.position:
                flag = True
                # return path and expanded cells
                return self.retrieve_path(current), [v.position for v in explored_set]
            # add current cell's child to queue to visit
            child = self.init_child(current)
            for cell in child:
                if not [v.position for v in explored_set].__contains__(cell.position):
                    explored_set.append(cell)
                    queue.append(cell)

        if not flag:
            print("Can not reach the goal !!")
            return None

    def dls_search(self, src, destination, maxDepth, explored_set):
        """DSL Search base on graph search"""

        explored_set.append(src.position)

        if src.position == destination.position:
            return True, self.retrieve_path(src), explored_set
        # If reached the maximum depth, stop recursing.
        if maxDepth <= 0:
            return False, None, explored_set
        child = self.init_child(src)
        # Recur for all the vertices adjacent to this vertex
        for i in child:
            # check the child wasn't visit yet
            if not explored_set.__contains__(i.position):
                flag, path, explored_set = self.dls_search(
                    i, destination, maxDepth-1, explored_set)
                if flag:
                    return True, path, explored_set
        return False, None, explored_set

    def ids_search(self):
        """Iterative DLS"""

        from itertools import count

        # Store explored_set nodes for each iteration
        explored_set = dict()

        # Repeatedly depth-limit search till the reaches the goal's depth
        for i in count():
            flag, path, explored_set[i] = self.dls_search(
                self.source_cell, self.destination_cell, i, [])
            if flag:
                return path, explored_set
        return False

    def astar_search(self):

        # Create lists for open nodes and closed nodes
        open = []
        explored_set = []

        open.append(self.source_cell)

        # Loop until the open list is empty
        while open:
            # Get the node with the lowest cost
            current_cell = open[0]
            open.remove(current_cell)
            # Add the current node to the closed list
            if not explored_set.__contains__(current_cell.position):
                explored_set.append(current_cell.position)

            # Check if we have reached the goal, return the path
            if current_cell.position == self.destination_cell.position:
                return self.retrieve_path(current_cell), explored_set

            child = self.init_child(current_cell)
            # Loop child
            for cell in child:
                # Generate heuristics (Manhattan distance)
                cell.g = abs(cell.position[0] - self.source_cell.position[0]) + abs(
                    cell.position[1] - self.source_cell.position[1])
                cell.h = abs(cell.position[0] - self.destination_cell.position[0]) + abs(
                    cell.position[1] - self.destination_cell.position[1])
                cell.f = cell.g + cell.h
                # Check if child is in open list and if it has a lower f value
                if self.add_to_open(open, cell):
                    if not explored_set.__contains__(cell.position):
                        # Everything is green, add child to open list
                        open.append(cell)
                        sorted(open, key=lambda node_ob: node_ob.f)
        # Return None, no path is found
        return None

    def add_to_open(self, open, child):
        """Check if a child should be added to open list"""

        for node in open:
            if (child == node and child.f >= node.f):
                return False
        return True


