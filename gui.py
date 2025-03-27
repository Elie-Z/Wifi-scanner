import customtkinter as ctk
from ip_retrieve import ip
import scapy.all as scapy
import ipaddress

def is_valid_ip_range(ip_range):
    try:
        # Validate the input as an IPv4 network
        ipaddress.ip_network(ip_range, strict=False)
        return True
    except ValueError:
        return False

app = ctk.CTk()
app.title('Wifi Scanner')
app.geometry("800x550")


def update_results():
    entered_ip = manual_ip.get()

    # Check if the entered IP is valid
    if is_valid_ip_range(entered_ip):
        warning_label.configure(text=f'Scanning: {entered_ip}', font=("Arial", 18), text_color="green")
        info = {}
        answered, unanswered = scapy.arping(entered_ip, verbose=0)

        for sent, received in answered:
            info[received.hwsrc.replace(':', "-").upper()] = received.psrc

        if info:
            # Display MAC and IP addresses
            keys_text = "\n".join(info.keys())
            values_text = "\n".join(info.values())
            mac_label.configure(text=f"MAC Addresses:\n{keys_text}")
            ip_label.configure(text=f"IP Addresses:\n{values_text}")
        else:
            # No devices found
            mac_label.configure(text="No devices found.")
            ip_label.configure(text="No devices found.")
    elif entered_ip.strip() == "":
        # Prompt for empty input
        warning_label.configure(text="Please enter an IP range.", font=("Arial", 18), text_color="red")
    else:
        # Invalid IP range
        warning_label.configure(text=f"{entered_ip} is NOT a valid IP range.", font=("Arial", 18), text_color="red")


def auto_ip():
    captured_ip = ip()
    if captured_ip:
        manual_ip.delete(0, ctk.END)
        manual_ip.insert(0, captured_ip)

# First layout
label_ip = ctk.CTkLabel(app, text="Enter IP address and range", fg_color="transparent")
label_ip.place(x=120, y=50)

manual_ip = ctk.CTkEntry(app, placeholder_text="e.g. 192.168.8.1/24", width=150)
manual_ip.place(x=300, y=50)

auto_ip_btn = ctk.CTkButton(app, text="Automatically Get My IP", command=auto_ip, width=100)
auto_ip_btn.place(x=500, y=50)

warning_label = ctk.CTkLabel(app, text='', text_color="red")
warning_label.place(x=260, y=100)

# Second Layout - IP Addresses Frame
frame_ip = ctk.CTkFrame(app, width=200, height=300)
frame_ip.place(x=150, y=150)

scrollable_frame_ip = ctk.CTkScrollableFrame(frame_ip, width=160, height=270)
scrollable_frame_ip.place(x=10, y=10)

ip_label = ctk.CTkLabel(scrollable_frame_ip, text='IP Address')
ip_label.pack(pady=3)

# Second Layout - MAC Addresses Frame
frame_mac = ctk.CTkFrame(app, width=200, height=300)
frame_mac.place(x=380, y=150)

scrollable_frame_mac = ctk.CTkScrollableFrame(frame_mac, width=160, height=270)
scrollable_frame_mac.place(x=10, y=10)

mac_label = ctk.CTkLabel(scrollable_frame_mac, text='MAC Addresses')
mac_label.pack(pady=3)

# Scan Button
scan_btn = ctk.CTkButton(app, text="Scan", text_color="white", fg_color="blue", hover_color="red", command=update_results)
scan_btn.place(x=300, y=500)

if __name__ == "__main__":
    app.mainloop()
