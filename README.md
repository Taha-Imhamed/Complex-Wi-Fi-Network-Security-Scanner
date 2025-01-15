# Wi-Fi Network Security Scanner

This Python script is designed to scan nearby Wi-Fi networks and evaluate their security level. It uses Kali Linux tools (`airmon-ng`, `airodump-ng`, `aircrack-ng`) to scan the networks and report if they have weak or no security.

## Features
- Scan available Wi-Fi networks in your area.
- Check the security level of each network (No Security, WEP, WPA2).
- Report weak or unsecured networks.
- Save the results to a CSV file for further analysis.

## Requirements
- Python 3.x
- Kali Linux (or a Linux distribution with `aircrack-ng` tools installed)
- `airmon-ng` and `airodump-ng` tools (from `aircrack-ng` suite)

## Installation

1. Install `aircrack-ng` tools:
   ```bash
   sudo apt update
   sudo apt install aircrack-ng

### How to Use the Script:
1. Clone the GitHub repository where you will store this project.
2. Ensure your Wi-Fi adapter supports monitor mode.
3. Run the script with `sudo` since it requires root privileges to use network interfaces.
4. The script will display the list of nearby networks and their security status (WPA2, WEP, or open).

Feel free to update the repository with your custom modifications and additional features. Let me know if you need help with anything else!
