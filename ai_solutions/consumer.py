import json
import sys
from channels.generic.websocket import WebsocketConsumer
from ai_solutions import maze_solver



class SolverConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        '''
            this receive data and send back the response to the user
        '''
        
        response = ""
        print(text_data)
        
        data = json.loads(text_data)
        
        
        
        if data['method'].upper() == 'BFS':
            # calling bfs search
            try:
                
                path, cost, exp_set = maze_solver.MazeSolver(data['source'], 
                                                 data['destination'],
                                                  data['black']).bfs_graph_search()
                
                response = json.dumps({
                    "message": "your choice was BFS",
                    "path": path,
                    'cost': cost,
                    'explored_set': exp_set    
                })
                
                print(20*'#' + '\n' + "BFS" + '\n' + 20*'#' + '\n')
            except Exception as e:
                response = json.dumps({
                            "error": e.__str__(),
                            "line": sys.exc_info()[-1].tb_lineno
                })    
              
        elif data['method'].upper() == 'IDS':
            # calling IDS search
            try:
                response = json.dumps({
                    "message": "choosed type is IDS"    
                })
            except Exception as e:
                response = json.dumps({
                            "error": e.__str__()    
                })
        
        elif data['method'].upper() == "A*":
            # calling A* search
            try:
                raise ValueError("A* problem")
            
            except Exception as e:
                    response = json.dumps({
                        "error": e.__str__()    
                    })
        
        else:
            response = json.loads({
                "error": "method entered is not supported",
                "solution": "make choice between A*, BFS or IDS"
            })
        
        
        
        self.send(text_data=response)