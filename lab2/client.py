import socket, sys

def create_tcp_socket():
    print("Creating socket")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except(socket.error, msg):
        print(f"Failed to create socket Error code :{str(msg[0])}, Error message : {[msg[1]]}")
    print("Socket created successfully")
    return s

def get_remote_ip(host):
    print("Getting IP for {host}")
    try:
        remote_ip = socket.gethostbyname(host)
    except socket.gaierror:
        print("Hostname could not be resolved. Exiting")
        sys.exit()
    print(f"Ip address of {host} is {remote_ip}")
    return remote_ip

def send_data(serversocket, payload):
    print("Sending payload")
    try:
        serversocket.sendall(payload.encode())
    except socket.error:
        print("Send failed")
        sys.exit()
    print("Payload sent successfully")

def main():
    try:
        host = "www.google.com"
        port = 80
        payload = "GET / HTTP/1.0\r\nHost: {0}\r\n\r\n"
        buffer_size = 4096

        s = create_tcp_socket()

        remote_ip = get_remote_ip(host)

        s.connect((remote_ip, port))
        print("Socket Connected to{0} on ip {1}".format(host, remote_ip))

        send_data(s, payload)
        s.shutdown(socket.SHUT_WR)

        full_data = b''
        
        while True:
            data = s.recv(buffer_size)
            

def main():
    try:
        host = 'www.google.ca'