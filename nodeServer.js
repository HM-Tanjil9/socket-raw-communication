const net = require('net');

const Server = net.createServer((socket) => {
    socket.on('data', (clientData) => {
        console.log("Data received from client :", clientData.toString());
    });
    socket.write("Received on server thank you");
});

Server.listen(8080, () => {
    console.log("New server up on port 8080");
});