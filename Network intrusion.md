
# Network Intrusion Detection System (NIDS)

## Overview

A Network Intrusion Detection System (NIDS) is a security tool that monitors network traffic in real time, analyzing it for suspicious activity or known attack patterns. It alerts administrators upon detecting potentially malicious activity, allowing them to respond or block the threat.

### Example
In this project, Suricata is configured to monitor incoming and outgoing network traffic. If Suricata detects a pattern matching a known attack, such as an SQL injection attempt, it logs the event and alerts administrators, enabling rapid response.

## Tools Used

1. *Suricata* - An IDS/IPS that scans network traffic for suspicious patterns based on predefined rules.
2. *nmap* - A network scanning tool to detect active hosts, open ports, and services on a network.

## Setup Instructions

### 1. Installing Suricata
To install Suricata on Ubuntu, run the following commands:

bash
sudo apt-get update
sudo apt-get install suricata -y


- sudo apt-get update: Updates package lists for the latest versions.
- sudo apt-get install suricata -y: Installs Suricata.

### 2. Configuring Suricata

To configure Suricata, edit the main configuration file (suricata.yaml):

bash
sudo nano /etc/suricata/suricata.yaml


In the configuration, set the network variables:

yaml
vars:
  address-groups:
    HOME_NET: "[network ip]"


Replace [network ip] with your network IP address or range that Suricata will monitor.

### 3. Updating and Running Suricata

Run the following commands to update Suricata's rules and start monitoring:

bash
sudo suricata-update
sudo suricata -c /etc/suricata/suricata.yaml -i eth0


- sudo suricata-update: Downloads the latest rules for threat detection.
- sudo suricata -c /etc/suricata/suricata.yaml -i eth0: Starts Suricata with the specified configuration file and network interface (eth0 here; replace if different).

### 4. Installing and Using nmap

Install nmap to scan your network:

bash
sudo apt-get install nmap -y
sudo nmap -sP [Network ip]
sudo nmap -A [Network ip]  # More aggressive scan for noticeable traffic


- sudo apt-get install nmap -y: Installs nmap for scanning.
- sudo nmap -sP [Network ip]: Lists active hosts. Replace [Network ip] with your target network range.

### 5. Monitoring Logs

Use these commands to monitor Suricata's log files:

bash
sudo tail -f /var/log/suricata/fast.log
sudo tail -f /var/log/suricata/eve.json


- *fast.log*: Provides quick alerts in a minimal format.
- *eve.json*: Detailed JSON-based log file, ideal for integration with visualization tools.

## License

This project is open-source and available under the [MIT License](LICENSE).

