import customtkinter as ctk
from ip_retrieve import ip
import scapy.all as scapy
import ipaddress


class WifiScannerApp:
    def __init__(self):
        self.loop_running = False
        self.app = ctk.CTk()
        self.app.title('Wifi Scanner')
        self.app.geometry("800x550")

        self.create_widgets()

    def create_widgets(self):
        # Input and Auto IP
        ctk.CTkLabel(self.app, text="Enter IP address and range", fg_color="transparent").place(x=120, y=50)

        self.manual_ip = ctk.CTkEntry(self.app, placeholder_text="e.g. 192.168.8.1/24", width=150)
        self.manual_ip.place(x=300, y=50)

        ctk.CTkButton(self.app, text="Automatically Get My IP", command=self.auto_ip, width=100).place(x=500, y=50)

        self.warning_label = ctk.CTkLabel(self.app, text='', text_color="red")
        self.warning_label.place(x=260, y=90)

        # IP Addresses Frame
        frame_ip = ctk.CTkFrame(self.app, width=200, height=300)
        frame_ip.place(x=150, y=160)

        ctk.CTkLabel(self.app, text='IP Address').place(x=220, y=130)

        scrollable_frame_ip = ctk.CTkScrollableFrame(frame_ip, width=160, height=270)
        scrollable_frame_ip.place(x=10, y=10)

        self.ip_content = ctk.CTkLabel(scrollable_frame_ip, text="")
        self.ip_content.pack(pady=5)

        # MAC Addresses Frame
        frame_mac = ctk.CTkFrame(self.app, width=200, height=300)
        frame_mac.place(x=380, y=160)

        ctk.CTkLabel(self.app, text='Mac Address').place(x=440, y=130)

        scrollable_frame_mac = ctk.CTkScrollableFrame(frame_mac, width=160, height=270)
        scrollable_frame_mac.place(x=10, y=10)

        self.mac_content = ctk.CTkLabel(scrollable_frame_mac, text="")
        self.mac_content.pack(pady=5)

        # Control Buttons
        ctk.CTkButton(self.app, text="Start Scan", text_color="white", fg_color="blue", hover_color="red",
                      command=self.start_scan_loop).place(x=180, y=480)

        ctk.CTkButton(self.app, text="Stop Loop", text_color="white", fg_color="red", hover_color="darkred",
                      command=self.stop_scan_loop).place(x=405, y=480)

    @staticmethod
    def is_valid_ip_range(ip_range):
        try:
            ipaddress.ip_network(ip_range, strict=False)
            return True
        except ValueError:
            return False

    def auto_ip(self):
        captured_ip = ip()
        if captured_ip:
            self.manual_ip.delete(0, ctk.END)
            self.manual_ip.insert(0, captured_ip)

    def update_results(self):
        entered_ip = self.manual_ip.get()

        if self.is_valid_ip_range(entered_ip):
            self.warning_label.configure(text=f'Scanning: {entered_ip}', font=("Arial", 18), text_color="green")
            info = {}

            try:
                answered, unanswered = scapy.arping(entered_ip, verbose=0)
            except Exception as e:
                self.warning_label.configure(text=f"Error: {str(e)}", font=("Arial", 18), text_color="red")
                return

            for sent, received in answered:
                info[received.hwsrc.replace(':', "-").upper()] = received.psrc

            if info:
                self.mac_content.configure(text="\n".join(info.keys()))
                self.ip_content.configure(text="\n".join(info.values()))
            else:
                self.mac_content.configure(text="No devices found.")
                self.ip_content.configure(text="No devices found.")
        elif entered_ip.strip() == "":
            self.warning_label.configure(text="Please enter an IP range.", font=("Arial", 18), text_color="red")
        else:
            self.warning_label.configure(text=f"{entered_ip} is NOT a valid IP range.", font=("Arial", 18), text_color="red")

    def scan_loop(self):
        if self.loop_running:
            self.update_results()
            self.app.after(5000, self.scan_loop)

    def start_scan_loop(self):
        self.loop_running = True
        self.scan_loop()

    def stop_scan_loop(self):
        self.loop_running = False

    def run(self):
        self.app.mainloop()

if __name__ == "__main__":
    WifiScannerApp().run()
