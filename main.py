import scapy.all as scapy
import re
import time

ip_add_range_pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")

# Get the address range to ARP
while True:
    ip_add_range_entered = input(
        "\nPlease enter the IP address and range that you want to send the ARP request to (ex 192.168.1.0/24): ")
    if ip_add_range_pattern.search(ip_add_range_entered):
        print(f"{ip_add_range_entered} is a valid IP address range")
        break

# Continuous ARP scanning
try:
    while True:
        print("\nStarting ARP scan...")
        scapy.arping(ip_add_range_entered)
        print("\nScan complete. Waiting for the next scan...")

        time.sleep(5)
except KeyboardInterrupt:
    print("\nExiting program. Goodbye!")