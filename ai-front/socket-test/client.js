#!/usr/bin/env node

var WebSocketClient = require('websocket').client;

var client = new WebSocketClient();

/*
model
{
    method: "ids",
    source: [3, 0], 
    destination: [0, 3], 
    black: [[0, 0], [1, 2], [2, 0], [3, 3]], 
    size: 4
}
*/

let data = []
let blacked = [[], [], []]
let r, c;

for(let i = 0; i < 3; i++){
    for(let j = 0; j < 30; j++){
        r = Math.floor(Math.random() * 10) + 1;
        c = Math.floor(Math.random() * 10) + 1;
        blacked[i].push([r, c]);
    }
}

for(let i = 0; i < 3; i++){
    console.log(blacked[i])
}


for(let i = 0; i < 3; i++){
    data[i] = {
        method: "all",
        source: [6, 8], 
        destination: [4, 3], 
        black: blacked[i], 
        size: 10
    }
}


client.on('connectFailed', function(error) {
    console.log('Connect Error: ' + error.toString());
});

client.on('connect', function(connection) {

    console.log('WebSocket client connected');

    connection.on('error', function(error) {
        console.log("Connection Error: " + error.toString());
    });

    connection.on('close', function() {
        console.log('echo-protocol Connection Closed');
    });

    connection.on('message', function(message) {
        if (message.type === 'utf8') {
            
            // printing info like eplored set size and ...
            tmp_data = JSON.parse(message.utf8Data);
            let formatted_print = "choice:\t"+ tmp_data.message;
            let bfs_formatted = "BFS\n" +  "Path is:\t" + JSON.stringify(tmp_data.BFS.path) + "\n" + 
                "cost is:\t" + tmp_data.BFS.cost + "\n" + "explored_set_len is:\t" +
                tmp_data.BFS.explored_set_len + "\n" + "explored_set is:\t" + JSON.stringify(tmp_data.BFS.explored_set);

            let ids_formatted = "IDS\n" +  "Path is:\t" + JSON.stringify(tmp_data.IDS.path) + "\n" +
                "cost is:\t" + tmp_data.IDS.cost + "\n" + "explored_set_len is:\t" +
                tmp_data.IDS.explored_set_len + "\n" + "explored_set is:\t" + JSON.stringify(tmp_data.IDS.explored_set);
            
            let astar_formatted = "AStar\n" +  "Path is:\t" + JSON.stringify(tmp_data.AStar.path) + "\n" +
                "cost is:\t" + tmp_data.AStar.cost + "\n" + "explored_set_len is:\t" +
                tmp_data.AStar.explored_set_len + "\n" + "explored_set is:\t" + JSON.stringify(tmp_data.AStar.explored_set);
            
            
            console.log(formatted_print);
            console.log(bfs_formatted);
            console.log(ids_formatted);
            console.log(astar_formatted);
        }
    });


    for(let i = 0; i < 3; i++){
        connection.sendUTF(JSON.stringify(data[i]));        
    }


});

client.connect('ws://127.0.0.1:8000/ws/solve/bfs/', "", "http://localhost:8000");


// this step writing automated test and showing the result in console