#!/usr/bin/env node
var WebSocketClient = require('websocket').client;


var client0 = new WebSocketClient();

data = {
    method: "bfs",
    source: [3, 0], 
    destination: [0, 3], 
    black: [[0, 0], [1, 2], [2, 0], [3, 3]], 
    size: 4
}

/*
e_path = [(3, 0), (3, 1), (2, 1), (1, 1),
          (0, 1), (0, 2), (0, 3)]
e_visited = [(3, 0), (3, 1), (2, 1), (3, 2), (1, 1), (2, 2),
             (0, 1), (1, 0), (2, 3), (0, 2), (1, 3), (0, 3)]
*/

client0.on('connectFailed', function(error) {
    console.log('Connect Error: ' + error.toString());
});

client0.on('connect', function(connection) {
    console.log('WebSocket client connected');
    connection.on('error', function(error) {
        console.log("Connection Error: " + error.toString());
    });
    connection.on('close', function() {
        console.log('echo-protocol Connection Closed');
    });
    connection.on('message', function(message) {
        if (message.type === 'utf8') {
            console.log("Received: '" + message.utf8Data + "'");
        }
    });

    connection.sendUTF(JSON.stringify(data));
});

client0.connect('ws://127.0.0.1:8000/ws/solve/bfs/', "", "http://localhost:8000");





/**
 * testing multiple client connections
 */
var client1 = new WebSocketClient();

client1.on('connectFailed', function(error) {
    console.log('Connect Error: ' + error.toString());
});

client1.on('connect', function(connection) {
    console.log('WebSocket client connected');
    connection.on('error', function(error) {
        console.log("Connection Error: " + error.toString());
    });
    connection.on('close', function() {
        console.log('echo-protocol Connection Closed');
    });
    connection.on('message', function(message) {
        if (message.type === 'utf8') {
            console.log("Received: '" + message.utf8Data + "'");
        }
    });

    connection.sendUTF(JSON.stringify({
        method: "a*"
    }));
});

client1.connect('ws://127.0.0.1:8000/ws/solve/bfs/', "", "http://localhost:8000");