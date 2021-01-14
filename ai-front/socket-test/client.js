#!/usr/bin/env node
var WebSocketClient = require('websocket').client;



/*
e_path = [(3, 0), (3, 1), (2, 1), (1, 1),
          (0, 1), (0, 2), (0, 3)]
*/

/********************** CLIENT 0 ********************

var client0 = new WebSocketClient();

data0 = {
    method: "bfs",
    source: [3, 0], 
    destination: [0, 3], 
    black: [[0, 0], [1, 2], [2, 0], [3, 3]], 
    size: 4
}

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

    connection.sendUTF(JSON.stringify(data0));
});

client0.connect('ws://127.0.0.1:8000/ws/solve/bfs/', "", "http://localhost:8000");




/********************** CLIENT 1 ********************/

var client1 = new WebSocketClient();

data1 = {
    method: "ids",
    source: [3, 0], 
    destination: [0, 3], 
    black: [[0, 0], [1, 2], [2, 0], [3, 3]], 
    size: 4
}



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

    connection.sendUTF(JSON.stringify(data1));
});

client1.connect('ws://127.0.0.1:8000/ws/solve/bfs/', "", "http://localhost:8000");




/********************** CLIENT 2 ********************

var client2 = new WebSocketClient();

data2 = {
    method: "A*",
    source: [3, 0], 
    destination: [0, 3], 
    black: [[0, 0], [1, 2], [2, 0], [3, 3]], 
    size: 4
}


client2.on('connectFailed', function(error) {
    console.log('Connect Error: ' + error.toString());
});

client2.on('connect', function(connection) {
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

    connection.sendUTF(JSON.stringify(data2));
});

client1.connect('ws://127.0.0.1:8000/ws/solve/bfs/', "", "http://localhost:8000");


/********************** Done ********************/