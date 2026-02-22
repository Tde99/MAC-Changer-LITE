```
  __  __          _____   _      _____ _______ ______ 
 |  \/  |   /\   / ____| | |    |_   _|__   __|  ____|
 | \  / |  /  \ | |      | |      | |    | |  | |__   
 | |\/| | / /\ \| |      | |      | |    | |  |  __|  
 | |  | |/ ____ \ |____  | |____ _| |_   | |  | |____ 
 |_|  |_/_/    \_\_____| |______|_____|  |_|  |______|
```
MAC-LITE (FAST MAC CHANGER)
A high-speed, lightweight Python script designed for quick MAC address 
spoofing on Linux systems. By utilizing the 'subprocess' module and 
'optparse' for streamlined CLI arguments, this tool provides a seamless 
way to enhance network privacy in seconds.

**Features**
* **Instant Spoofing:** Change your MAC address with a single command.
* **CLI Optimized:** Full support for command-line arguments (`-i`, `-m`).
* **Secure Execution:** Uses list-based subprocess calls to prevent shell injection.
* **Minimalist Design:** No unnecessary bloat—just pure performance.

**Prerequisites**
* Python 3.x
* Net-tools (`ifconfig` must be installed)
* Root/Sudo privileges

**Installation**

1. Clone the repository:
   * git clone https://github.com/Tde99/MAC-Lite.git

2. Navigate to the directory:
   * cd MAC-Lite

3. Make the script executable:
   * chmod +x mac_lite.py

**Usage**
Run the script with sudo and provide the interface and the new MAC address:

sudo python3 mac_lite.py -i eth0 -m 00:11:22:33:44:55

**How it Works:**
The script performs a three-step hardware address modification:
1. **Down:** Disables the target network interface.
2. **Modify:** Injects the new hardware (ether) address.
3. **Up:** Re-enables the interface with the new identity.



**Important Notes:**
* **Temporary:** The changes last until the next system reboot.
* **Legal Use:** Intended for privacy research and authorized security audits.
* **Compatibility:** Works on most Debian-based distributions (Kali, Ubuntu, etc.).
