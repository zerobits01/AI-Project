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
                
                result = maze_solver.MazeSolver(data['source'], 
                                                 data['destination'],
                                                  data['black']).bfs_graph_search()
                
                if result is False:
                    response = json.dumps({
                        "message": "error has happened",
                        "err": "unknown error"  
                    })                      
                else:
                    response = json.dumps({
                        "message": "your choice was BFS",
                        "path": result[0],
                        'cost': result[1],
                        'explored_set': result[2]    
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
                   
                result = maze_solver.MazeSolver(data['source'], 
                                                 data['destination'],
                                                  data['black']).ids_graph_search()
                
                if result is False:
                    response = json.dumps({
                        "message": "error has happened",
                        "err": "unknown error"  
                    })                      
                else:
                    response = json.dumps({
                        "message": "your choice was IDS",
                        "path": result[0],
                        'cost': result[1],
                        'explored_set': result[2]    
                    })
                
                print(20*'#' + '\n' + "IDS" + '\n' + 20*'#' + '\n')
            
            except Exception as e:
                response = json.dumps({
                            "error": e.__str__(),
                            "line": sys.exc_info()[-1].tb_lineno
                })    
                
        elif data['method'].upper() == "A*":
            # calling A* search
            try:      
                result = ("path", "cost", "explored")
                         # maze_solver.MazeSolver(data['source'], 
                         #                         data['destination'],
                         #                         data['black']).aStar_graph_search()
                
                if result is False:
                    response = json.dumps({
                        "message": "error has happened",
                        "err": "unknown error"  
                    })                      
                else:
                    response = json.dumps({
                        "message": "your choice was IDS",
                        "path": result[0],
                        'cost': result[1],
                        'explored_set': result[2]    
                    })
                
                print(20*'#' + '\n' + "A*" + '\n' + 20*'#' + '\n')
            
            except Exception as e:
                response = json.dumps({
                            "error": e.__str__(),
                            "line": sys.exc_info()[-1].tb_lineno
                })    

        else:
            response = json.loads({
                "error": "method entered is not supported",
                "solution": "make choice between A*, BFS or IDS"
            })
        
        
        
        self.send(text_data=response)