import json
from channels.generic.websocket import WebsocketConsumer




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
                response = json.dumps({
                    "message": "choosed type is BFS"    
                })
                
            except Exception as e:
                pass
            
        
        elif data['method'].upper() == 'IDS':
            # calling IDS search
            try:
                response = json.dumps({
                    "message": "choosed type is IDS"    
                })
            except Exception as e:
                pass
        
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