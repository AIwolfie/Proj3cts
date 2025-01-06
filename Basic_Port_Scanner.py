import socket
import threading

def scan_port(ip, port, open_ports):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            if s.connect_ex((ip, port)) == 0:
                print(f"Port {port} is open.")
                open_ports.append(port)
    except socket.error:
        pass

def main():
    print("Basic Port Scanner")
    print("------------------")

    ip = input("Enter the IP address: ").strip()
    try:
        start_port = int(input("Enter the starting port: "))
        end_port = int(input("Enter the ending port: "))

        if start_port < 0 or end_port > 65535 or start_port > end_port:
            raise ValueError("Invalid port range. Ports must be between 0 and 65535, and the start port must be less than or equal to the end port.")
    except ValueError as e:
        print(f"Error: {e}")
        return

    print(f"\nScanning IP {ip} for open ports from {start_port} to {end_port}...\n")

    open_ports = []
    threads = []

    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(ip, port, open_ports))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    if open_ports:
        print(f"\nOpen ports: {', '.join(map(str, open_ports))}")
    else:
        print("\nNo open ports found.")

if __name__ == "__main__":
    main()
