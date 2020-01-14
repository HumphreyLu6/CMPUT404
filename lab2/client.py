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

def send_data(servicesocket, payload):
    

def main():
    try:
        host = 'www.google.ca'