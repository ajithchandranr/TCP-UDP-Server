import socket

TCP_PORT = 1234
UDP_PORT = 5678
BUFFER_SIZE = 1024

def start_tcp_server():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.bind(('', TCP_PORT))
    tcp_socket.listen(1)
    print(f'TCP server started on port {TCP_PORT}')

    conn, addr = tcp_socket.accept()
    print(f'Connected by {addr}')

    while True:
        data = conn.recv(BUFFER_SIZE)
        if not data:
            break
        message = data.decode()
        print(f'TCP Received: {message}')

    conn.close()

def start_udp_server():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(('', UDP_PORT))
    print(f'UDP server started on port {UDP_PORT}')

    while True:
        data, addr = udp_socket.recvfrom(BUFFER_SIZE)
        message = data.decode()
        print(f'UDP Received: {message}')

# Main entry point
if __name__ == '__main__':
    server_type = input("Enter 'tcp' for TCP server or 'udp' for UDP server: ")

    if server_type.lower() == 'tcp':
        start_tcp_server()
    elif server_type.lower() == 'udp':
        start_udp_server()
    else:
        print("Invalid server type. Please enter 'tcp' or 'udp'.")
