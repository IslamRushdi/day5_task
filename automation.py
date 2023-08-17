import socket
import sys

def scan_ports(host):
    open_ports = []
    
    for port in range(1, 65536):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if 0 == result:
            open_ports.append(port)
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
        sock.close()
        
    return open_ports

try:
    localhost = '127.0.0.1'
    open_ports = scan_ports(localhost)
    print(f"Open ports on {localhost}: {open_ports}")
except socket.gaierror:
    print('Hostname could not be resolved.')
    sys.exit()
except socket.error:
    print("Couldn't connect to server.")
    sys.exit()
except KeyboardInterrupt:
    print('intterupted')
