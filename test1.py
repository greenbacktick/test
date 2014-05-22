#!/usr/bin/python

import re

class Mac:
    'Common class to represente MAC'

    def __init__(self,mac,formac_src,formac_dst):
        self.mac = mac.lower()
        self.formac_src = formac_src.upper()
        self.formac_dst = formac_dst.upper()
    
    def displayMac(self):
        mac = self.changeFormat()
        print "MAC", mac, "format : ", self.formac_src, "to format : ", self.formac_dst
    
    def changeFormat(self):
        mac = self.cleanMac()
        if self.formac_dst == 'CISCO':
            mac_dst = ".".join((mac[:4],mac[4:8],mac[8:]))
        elif self.formac_dst == 'PLAIN':
            mac_dst = mac.lower()
        elif self.formac_dst == 'IEEE':
            mac_dst = ":".join((mac[:2],mac[2:4],mac[4:6],mac[6:8],mac[8:10],mac[10:]))
        elif self.formac_dst == 'DASH':
            mac_dst = "-".join((mac[:2],mac[2:4],mac[4:6],mac[6:8],mac[8:10],mac[10:]))
        else:
            print "Error source format unknown"
        return mac_dst
    
    def cleanMac(self):
        p = re.compile( '[0-9a-fA-F]+')
        cleaned_mac = ''.join(p.findall(self.mac))
        if len(cleaned_mac) != 12:
            print "error : Invalid given MAC address"
            exit()
        else:
            return cleaned_mac

mac1 = Mac("001122334455","plain","ieee")
mac2 = Mac("66:77:88:99:00:11","ieee","dash")
mac3 = Mac("00:AA:11:BB:22:CC","pf","cisco")
mac4 = Mac("30:af:11:cb:46:dc","pf","plain")
mac5 = Mac("adbc54na22ce","pf","plain")

mac1.displayMac()
mac2.displayMac()
mac3.displayMac()
mac4.displayMac()
mac5.displayMac()
#mac1.changeFormat()
#mac2.displayMac()
#mac2.changeFormat()
#mac3.displayMac()
#mac3.changeFormat()
#mac1.changeFormat()
#mac2.changeFormat()
#mac3.changeFormat()
#mac4.changeFormat()
#mac5.changeFormat()
