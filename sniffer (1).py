from scapy.all import sniff, IP, TCP, UDP, Raw  

def packet_callback(packet):  
    # Check if the packet has IP layer  
    if IP in packet:  
        ip_src = packet[IP].src  
        ip_dst = packet[IP].dst  
        print(f"Source IP: {ip_src}, Destination IP: {ip_dst}")  

    # Check if the packet has TCP layer  
    if TCP in packet:  
        tcp_src_port = packet[TCP].sport  
        tcp_dst_port = packet[TCP].dport  
        print(f"TCP Source Port: {tcp_src_port}, Destination Port: {tcp_dst_port}")  
    
    # Check if the packet has UDP layer  
    if UDP in packet:  
        udp_src_port = packet[UDP].sport  
        udp_dst_port = packet[UDP].dport  
        print(f"UDP Source Port: {udp_src_port}, Destination Port: {udp_dst_port}")  

    # Check if the packet has Raw layer (contains payload)  
    if Raw in packet:  
        raw_data = packet[Raw].load  
        print(f"Payload (Raw Data): {raw_data}")  

# Start sniffing (set filter according to your needs, e.g., 'tcp', 'udp', etc.)  
sniff(prn=packet_callback, count=10)