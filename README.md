# Wi-Fi Scanner App

A simple Python application to scan the local network and retrieve the IP and MAC addresses of devices connected to the network.

## Features

- Scan a given IP range (e.g., `192.168.1.0/24`).
- Displays a list of connected devices' IP addresses and corresponding MAC addresses.
- Option to automatically retrieve your IP address and use it for scanning.
- Continuous scanning loop with start and stop functionality.

## Requirements

- Python 3.x
- `scapy` for network scanning.
- `customtkinter` for the GUI interface.

To install the required dependencies, run the following command:

## How to Use

### 1. Clone the Repository:

To get started, clone the repository to your local machine. In your terminal or command prompt, run:

```bash
git clone https://github.com/your-username/wifi-scanner.git
```
This will create a copy of the project on your local machine.

### 2. Navigate to the Project Directory:
Once cloned, change into the project directory:

```bash
cd wifi-scanner
```

### 3. Install Dependencies:
The application requires certain Python libraries to run. You can install these by running:

```bash
pip install customtkinter scapy ip-retrieve
```

### 4. Run the Application:
Once the dependencies are installed, you can start the application by running:

```bash
python app.py
```
This will launch the Wi-Fi Scanner GUI application.

---

### Start Scanning:
Enter the desired IP range (e.g., 192.168.1.0/24).

Click Start Scan to begin scanning for devices.

The app will show a list of connected devices’ IP and MAC addresses.


### Stop the Scan:
You can stop the continuous scan by clicking the Stop Loop button.


### Auto IP Detection:
To automatically detect your local IP range, click Automatically Get My IP, and the app will fill in the IP range for you.
