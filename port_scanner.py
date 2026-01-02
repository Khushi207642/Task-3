import socket

def scan_ports(host, start_port=1, end_port=100):
    print(f"\nScanning {host} from port {start_port} to {end_port}")
    open_ports = []

    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((host, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except:
            pass

    return open_ports


if __name__ == "__main__":
    host = "127.0.0.1"
    ports = scan_ports(host)
    print("Open ports:", ports)
