import customtkinter as ctk
from ip_retrieve import ip
import scapy.all as scapy


app = ctk.CTk()
app.title('Wifi Scanner')
app.geometry("800x800")

# Label for IP entry
label_ip = ctk.CTkLabel(app, text="Enter IP address and range", fg_color="transparent")
label_ip.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

# Entry field for IP input
entry = ctk.CTkEntry(app, placeholder_text="e.g. 192.168.8.1/24")
entry.grid(row=0, column=1, padx=20, pady=20, sticky="ew")

# Button to collect IP
m_ip = ctk.CTkButton(app, text="Collect IP")
m_ip.grid(row=0, column=3, padx=20, pady=20, sticky="ew")

# Label for displaying captured IP
label_display = ctk.CTkLabel(app, text="Captured IP will appear here:", fg_color="transparent")
label_display.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

# Entry (or Label) for displaying captured IP
entry_a = ctk.CTkLabel(app, text="Waiting for IP...", fg_color="transparent")
entry_a.grid(row=1, column=1, padx=30, pady=30, sticky="ew")

# Function to update the label with captured IP
def update_ip_label():
    captured_ip = ip()
    if captured_ip:
        entry_a.configure(text=f"Captured IP: {captured_ip}")
    else:
        entry_a.configure(text="Failed to retrieve IP.")

# Button to collect ip automatically
auto_ip = ctk.CTkButton(app, text="Gather my IP", command=update_ip_label)
auto_ip.grid(row=1, column=3, padx=20, pady=20, sticky="ew")

# Results frame


def scan():
    info = {}
    answered, unanswered = scapy.arping('192.168.8.1/24', verbose=0)
    for sent, received in answered:
        info[received.hwsrc.replace(':', "-").upper()] = received.psrc
    return info

def update_results():
    results = scan()
    if results:
        keys_text = "\n".join(results.keys())  # Convert keys to a string
        values_text = "\n".join(results.values())  # Convert values to a string
        label_results2.configure(text=f"MAC Addresses:\n{keys_text}")
        label_results.configure(text=f"IP Addresses:\n{values_text}")
    else:
        label_results2.configure(text="No devices found.")
        label_results.configure(text="No devices found.")


# Frame for IP Addresses
frame_ip = ctk.CTkFrame(app, width=300, height=200)
frame_ip.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")  # Separate row and column

# Label for IP Addresses
label_results = ctk.CTkLabel(
    frame_ip, text="IP Addresses will appear here...", fg_color="transparent", wraplength=280
)
label_results.pack(padx=20, pady=20)  # Use pack for better positioning within the frame

# Frame for MAC Addresses
frame_mac = ctk.CTkFrame(app, width=300, height=200)
frame_mac.grid(row=2, column=1, padx=20, pady=20, sticky="nsew")  # Adjacent column

# Label for MAC Addresses
label_results2 = ctk.CTkLabel(
    frame_mac, text="MAC Addresses will appear here...", fg_color="transparent", wraplength=280
)
label_results2.pack(padx=20, pady=20)

# Adjust grid configuration to distribute space evenly
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(2, weight=1)


scan_btn = ctk.CTkButton(app, text="Scan", text_color="white", fg_color="blue", hover_color="red", command=update_results)
scan_btn.grid(row=3, column=1)

if __name__ == "__main__":
    app.mainloop()
