# TCP/UDP Server

The TCP/UDP Server project is a Python script that implements a server to receive messages over the TCP and UDP network protocols.

## Features

- Supports both TCP and UDP protocols for message reception.
- Handles incoming messages and displays them on the console.
- Simple and easy to use.

## Prerequisites

Before running the server, ensure you have the following dependencies installed:

- Python (version 3.6 or higher)

## Getting Started

To get started with the TCP/UDP Server, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/ajithchandranr/TCP-UDP-Server.git
   ```

2. Change into the project directory:
   ```
   cd tcp-udp-server
   ```

3. Run the server:
   ```
   python server.py
   ```

4. The server is now listening for incoming messages on the specified ports.

## Usage

To use the TCP/UDP server:

1. Choose whether to use TCP or UDP for your communication needs.
2. Set up a TCP or UDP client to send messages to the server.
3. The server will receive the messages and display them on the console.

## Examples

Here's an example of how to use the server with a TCP client:

```python
import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 1234
MESSAGE = 'Hello, server!'

# Create a TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
s.connect((TCP_IP, TCP_PORT))

# Send the message
s.sendall(MESSAGE.encode())

# Close the connection
s.close()
```

And here's an example using a UDP client:

```python
import socket

UDP_IP = '127.0.0.1'
UDP_PORT = 5678
MESSAGE = 'Hello, server!'

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send the message to the server
sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))

# Close the socket
sock.close()
```

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License

## Contact

This README provides an overview of your TCP/UDP Server project, how to use it, and other important details. Feel free to modify and expand it based on your project's specific requirements.

e-mail     : ajithchandranr@protonmail.com 
 
linkedin  : https://www.linkedin.com/in/ajithchandranr/
