from scapy.all import sniff, IP

def handle_packet(pkt):
    if IP in pkt:
        ip_layer = pkt[IP]
        protocol_number = ip_layer.proto
        sender_ip = ip_layer.src
        target_ip = ip_layer.dst

        protocol_names = {1: "ICMP", 6: "TCP", 17: "UDP"}
        protocol_type = protocol_names.get(protocol_number, "Unknown Protocol")

        packet_details = (
            f"Protocol: {protocol_type}\n"
            f"Sender IP address: {sender_ip}\n"
            f"Target IP address: {target_ip}\n"
            f"{'-' * 50}\n"
        )

        print(packet_details, end="")

        with open('file.txt', 'a') as file:
            file.write(packet_details)

def main():
    sniff(prn=handle_packet, filter="ip", store=0)

if __name__ == "__main__":
    main()
