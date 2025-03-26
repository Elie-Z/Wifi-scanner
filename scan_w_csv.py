import scapy.all as scapy
import csv

# Define the IP range
ip_range = '192.168.8.1/24'

# Perform ARP scan
try:
    answered, unanswered = scapy.arping(ip_range, verbose=0)
except Exception as e:
    print(f"Error during ARP scan: {e}")
    exit()

# Check if any responses were received
if not answered:
    print("No responses received. Please check the network or IP range.")
    exit()

csv_file = 'arp_scan_results.csv'
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['IP Address', 'MAC Address'])

    for sent, received in answered:
        print(received.hwsrc.replace(':', "-").upper())
        writer.writerow([received.psrc, received.hwsrc.replace(':', "-").upper()])

print(f"Results saved to {csv_file}")
