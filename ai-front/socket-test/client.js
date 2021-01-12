#!/usr/bin/env node
var WebSocketClient = require('websocket').client;


var client0 = new WebSocketClient();

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

    connection.sendUTF(JSON.stringify({
        method: "bfs"
    }));
});

client0.connect('ws://127.0.0.1:8000/ws/solve/bfs/', "", "http://localhost:8000");


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