Here's a README file for your Network Sniffer project repository:

---

# Network Sniffer

A *Network Sniffer* is a tool used to capture, monitor, and analyze network packets in real-time. Network administrators use sniffers to troubleshoot network issues, monitor performance, or detect suspicious activity. In cybersecurity, sniffers help identify potential vulnerabilities and unauthorized access by analyzing packet flows and contents.

## Features

This project provides a Python-based Network Sniffer using the Scapy library, enabling:
- Real-time packet capture
- Inspection of network packet layers (IP, TCP, UDP, and Raw)
- Extraction and display of packet details such as IP addresses, ports, and payload data

## Installation

1. *Install Python* (ensure you have Python 3.x installed).
2. *Install Scapy*:
    bash
    pip install scapy
    
   
## Usage

Run the script to start capturing packets:
bash
python network_sniffer.py


### Code Explanation

The code utilizes *Scapy* to create a network sniffer that captures and processes network packets. Here’s a breakdown of the key components:

1. *Imports*:
    python
    from scapy.all import sniff, IP, TCP, UDP, Raw
    
   These imports bring in essential Scapy functions and packet layers for network packet manipulation and analysis.

2. *Packet Callback Function*:
   python
   def packet_callback(packet):
   
   This function processes each captured packet, extracting relevant information, including IP addresses, TCP/UDP ports, and any available payload data.

3. *IP Layer Extraction*:
   python
   if IP in packet:
       ip_src = packet[IP].src
       ip_dst = packet[IP].dst
       print(f"Source IP: {ip_src}, Destination IP: {ip_dst}")
   
   Checks if a packet contains the IP layer and, if so, prints its source and destination IP addresses.

4. *TCP Layer Extraction*:
   python
   if TCP in packet:
       tcp_src_port = packet[TCP].sport
       tcp_dst_port = packet[TCP].dport
       print(f"TCP Source Port: {tcp_src_port}, Destination Port: {tcp_dst_port}")
   
   Checks for the TCP layer and, if present, prints the source and destination TCP ports.

5. *UDP Layer Extraction*:
   python
   if UDP in packet:
       udp_src_port = packet[UDP].sport
       udp_dst_port = packet[UDP].dport
       print(f"UDP Source Port: {udp_src_port}, Destination Port: {udp_dst_port}")
   
   Checks for the UDP layer and prints the source and destination UDP ports if available.

6. *Raw Layer Extraction*:
   python
   if Raw in packet:
       raw_data = packet[Raw].load
       print(f"Payload (Raw Data): {raw_data}")
   
   If the packet contains a payload, it’s extracted and printed as raw data.

7. *Packet Capture (Sniffing)*:
   python
   sniff(prn=packet_callback, count=10)
   
   This function initiates the packet capture. Adjust count as needed to specify the number of packets to capture (omit for continuous capture).

## Example Output

plaintext
Source IP: 192.168.1.10, Destination IP: 192.168.1.1
TCP Source Port: 443, Destination Port: 49234
Payload (Raw Data): b'GET / HTTP/1.1\r\nHost: example.com\r\n\r\n'


## Note

- *Root Access*: Some operating systems may require root or administrative privileges to sniff network traffic.
- *Filter Options*: Use Scapy filters to target specific protocols (e.g., 'tcp', 'udp') by adding them to the sniff() function.

## License

This project is licensed under the MIT License.
