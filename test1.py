#!/usr/bin/python

import re

class Mac:
    'Common class to represente MAC'
    
    def __init__(self,mac,formac_src,formac_dst):
        self.mac = mac.lower()
        self.formac_src = formac_src.upper()
        self.formac_dst = formac_dst.upper()

    def displayMac(self):
        print "MAC",self.mac, "format : ",self.formac_src, "to format : ", self.formac_dst

    def changeFormat(self):
        if self.formac_dst == 'CISCO':
            self.mac_dst = self.mac[:4],self.mac[4:8],self.mac[8:]
            print ".".join(self.mac_dst)
        elif self.formac_dst == 'PLAIN':
            self.mac_dst = self.mac.lower()
            print self.mac_dst
        elif self.formac_dst == 'IEEE':
            self.mac_dst = self.mac[:2],self.mac[2:4],self.mac[4:6],self.mac[6:8],self.mac[8:10],self.mac[10:]
            print ":".join(self.mac_dst)
        elif self.formac_dst == 'DASH':
            self.mac_dst = self.mac[:2],self.mac[2:4],self.mac[4:6],self.mac[6:8],self.mac[8:10],self.mac[10:]
            print "-".join(self.mac_dst)
        else :
            print "Error source format unknown"

    def cleanMac(self):
        p = re.compile( '[0-9a-fA-F]+')
        cleaned_mac = ''.join(p.findall(self.mac))
        return cleaned_mac

    def printMac(self):
        cleaned_mac = self.cleanMac()
        print cleaned_mac

mac1 = Mac("001122334455","plain","ieee")
mac2 = Mac("66:77:88:99:00:11","ieee","ieee")
mac3 = Mac("00:AA:11:BB:22:CC","pf","cisco")

#mac1.displayMac()
#mac1.changeFormat()
#mac2.displayMac()
#mac2.changeFormat()
#mac3.displayMac()
#mac3.changeFormat()
mac2.printMac()
