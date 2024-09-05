#!/usr/bin/env python

import scapy.all as scapy
import argparse

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    for element in answered_list:
        print(f"IP Address: {element[1].psrc}")
        print(f"MAC Address: {element[1].hwsrc}")
        print("---------------------------------------")

def main():
    parser = argparse.ArgumentParser(description="Network Scanner to find active IPs and their MAC addresses.")
    parser.add_argument("-i", "--ipaddress", dest="ip", required=True, help="Specify the IP address or network range to scan (e.g., 192.168.1.1/24)")

    options = parser.parse_args()
    ip = options.ip

    scan(ip)

if __name__ == "__main__":
    main()

