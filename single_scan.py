import scapy.all as scapy
from ip_retrieve import ip


def single_scan(ip_address):
    try:
        print(f"Scanning IP: {ip_address}")
        scapy.arping(ip_address)
        print('\n***********')
        print('Scan Completed!')
    except Exception as e:
        print(f"Error during scan: {e}")


if __name__ == "__main__":
    ip = ip()
    if ip:
        single_scan(ip)
    else:
        print("Failed to retrieve or process the IP address.")
