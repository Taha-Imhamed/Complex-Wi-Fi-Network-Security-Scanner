import subprocess
import time
import os
import csv
from datetime import datetime

# Class to represent a Wi-Fi network
class WiFiNetwork:
    def __init__(self, ssid, bssid, encryption_type, signal_strength):
        self.ssid = ssid
        self.bssid = bssid
        self.encryption_type = encryption_type
        self.signal_strength = signal_strength
        self.security_status = self.get_security_status()

    # Method to determine security status based on encryption type
    def get_security_status(self):
        if self.encryption_type == 'WPA2':
            return "Strong Security"
        elif self.encryption_type == 'WEP':
            return "Weak Security (WEP)"
        elif self.encryption_type == 'None':
            return "No Security (Open Network)"
        else:
            return "Unknown Security"

# Function to execute shell commands and handle errors
def execute_command(command):
    try:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        if error:
            raise Exception(f"Error executing command: {error.decode()}")
        return output.decode()
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

# Function to start monitor mode on the Wi-Fi interface
def start_monitor_mode(interface):
    print(f"Starting monitor mode on {interface}...")
    execute_command(f'sudo airmon-ng start {interface}')
    time.sleep(2)
    return f"{interface}mon"  # Returns the new monitor mode interface

# Function to stop monitor mode on the Wi-Fi interface
def stop_monitor_mode(interface):
    print(f"Stopping monitor mode on {interface}...")
    execute_command(f'sudo airmon-ng stop {interface}')
    time.sleep(1)

# Function to scan Wi-Fi networks and return a list of WiFiNetwork objects
def scan_wifi_networks(interface):
    print("Scanning Wi-Fi networks...")
    execute_command(f'sudo airodump-ng {interface} --output-format csv --write wifi_scan_results')
    time.sleep(10)  # Let it scan for a while

    # Parse the CSV file with scan results
    networks = []
    with open('wifi_scan_results-01.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] != 'BSSID':  # Ignore header rows
                ssid = row[13]
                bssid = row[0]
                encryption = row[5]
                signal_strength = row[3]
                networks.append(WiFiNetwork(ssid, bssid, encryption, signal_strength))
    return networks

# Function to display the scan results in a readable format
def display_networks(networks):
    print("\nWi-Fi Networks and Security Status:")
    for network in networks:
        print(f"SSID: {network.ssid}, BSSID: {network.bssid}, Security: {network.security_status}, Signal Strength: {network.signal_strength} dBm")

# Function to save scan results to a CSV file
def save_results_to_csv(networks):
    filename = f"wifi_scan_results_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"
    print(f"Saving results to {filename}...")
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["SSID", "BSSID", "Security", "Signal Strength"])
        for network in networks:
            writer.writerow([network.ssid, network.bssid, network.security_status, network.signal_strength])

# Main function to coordinate the scanning and processing
def main():
    interface = "wlan0"  # Change this to your network interface (e.g., wlan0, wlan1)
    monitor_interface = start_monitor_mode(interface)

    networks = scan_wifi_networks(monitor_interface)
    display_networks(networks)
    save_results_to_csv(networks)

    stop_monitor_mode(monitor_interface)

   
    # memo is watching you

if __name__ == "__main__":
    main()
