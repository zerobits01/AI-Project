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
                
        elif data['method'].upper() == "ASTAR":
            # calling A* search
            try:      
                result = maze_solver.MazeSolver(data['source'], 
                                                 data['destination'],
                                                  data['black']).aStar_graph_search()
                
                if result is False:
                    response = json.dumps({
                        "message": "error has happened",
                        "err": "unknown error"  
                    })                      
                else:
                    response = json.dumps({
                        "message": "your choice was A*",
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

        elif data['method'].upper() == "ALL":
            maze = maze_solver.MazeSolver(data['source'], 
                                    data['destination'],
                                    data['black'])
            
            bfs_result = maze.bfs_graph_search()

            ids_result = maze.ids_graph_search()

            astar_result = maze.aStar_graph_search()

            if bfs_result is False:
                bfs_data = {
                        "message": "error has happened",
                        "err": "unknown error"  
                }
            else:
                bfs_data = {
                    'path': bfs_result[0],
                    'cost': bfs_result[1],
                    'explored_set_len': len(bfs_result[2]),
                    'explored_set': bfs_result[2]
                }
            

            if ids_result is False:
                ids_data = {
                        "message": "error has happened",
                        "err": "unknown error"  
                }
            else:
                ids_data = {
                    'path': ids_result[0],
                    'cost': ids_result[1],
                    'explored_set_len': len(ids_result[2]),
                    'explored_set': ids_result[2]
                }
            

            if astar_result is False:
                astar_data = {
                        "message": "error has happened",
                        "err": "unknown error"  
                }
            else:
                astar_data = {
                    'path': astar_result[0],
                    'cost': astar_result[1],
                    'explored_set_len': len(astar_result[2]),
                    'explored_set': astar_result[2]
                }
            
            
            response = json.dumps({
                "message": "your choice was all methods",
                "BFS": bfs_data,    
                "IDS": ids_data,    
                "AStar": astar_data    
            })

        
        else:
            response = json.loads({
                "error": "method entered is not supported",
                "solution": "make choice between A*, BFS or IDS"
            })
        
        
        
        self.send(text_data=response)