import scapy.all as scapy
from ip_retrieve import ip
from data import fetch_data
import time

def scan(ip):
    """
    Perform an ARP scan on the given IP range.
    :param ip: The IP range to scan.
    :return: List of MAC addresses found on the network.
    """
    try:
        answered, unanswered = scapy.arping(ip, verbose=0)
        if not answered:
            print("No responses received. Please check the network or IP range.")
            return []

        found_macs = [mac.hwsrc.replace(':', '-').upper() for _, mac in answered]
        return found_macs
    except Exception as e:
        print(f"Error during ARP scan: {e}")
        return []

def mac_compare(macs_found):
    data = fetch_data()
    unknown_mac = [m for m in macs_found if m not in data['Mac Address'].values]

    return unknown_mac

def scan_loop():
    ip_range = ip()
    macs_found = scan(ip_range)
    unknown_macs = mac_compare(macs_found)

    if unknown_macs:
        print(f'Found {len(unknown_macs)} unknown devices:\n')
        for mac in unknown_macs:
            print(mac)
    else:
        print("\nAll devices are known.")


def user_run():
    repeated_scan = input('Do you want scan loop? Y/N\n').upper()

    print('****************************')
    print('Scanning for Unknown devices')
    print('****************************')

    if repeated_scan == "Y":
        while True:
            try:
                print('------------------------')
                scan_loop()
                time.sleep(5)
            except KeyboardInterrupt:
                print('\nScan Completed!')
                print("\nExiting program. Goodbye!")
                break

    elif repeated_scan == "N":
        print('****************************')
        print('Scanning for Unknown devices')
        print('****************************')
        scan_loop()
        print('\nScan Completed!')
    else:
        print('Please answer with Y or N')

if __name__ == "__main__":
    user_run()