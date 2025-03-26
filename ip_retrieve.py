import subprocess
import platform

def ip():
    try:
        # Check the platform
        if platform.system() == "Windows":
            output = subprocess.check_output("ipconfig").decode('utf-8').splitlines()
            local_ip = output[-3].split(':')[-1].strip()
            segments = local_ip.split('.')
            segments[-1] = "1"
            return ".".join(segments) + "/24"
        else:
            # Add logic for other platforms (Linux/MacOS) if necessary
            print("This script is optimized for Windows.")
            return None
    except subprocess.CalledProcessError as e:
        print(f"Error retrieving IP: {e}")
        return None

