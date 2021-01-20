
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

