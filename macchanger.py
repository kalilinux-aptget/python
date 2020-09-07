#!/usr/bin/env python3
import re
import subprocess as subp
import optparse as optp

def input_function():
    parse=optp.OptionParser()
    parse.add_option("-i","--interface",dest="interface",help="interface to be used")
    parse.add_option("-m","--mac",dest="mac_address",help="mac addr to change")
    options,x=parse.parse_args()
    if not options.interface:
        parse.error("Specify the interface son type --help for more datails")
    elif not options.mac_address:
        parse.error("specify the mac address you want type --help for more info")

def function_to_change(interface,mac_addr):
    subp.call(["ifconfig",interface,"down"])
    subp.call(["ifconfig",interface,"hw","ether",mac_addr])
    subp.call(["ifconfig",interface,"up"])
    subp.call(["ifconfig",interface])

print("Starting")
user_interface,mac_addrs=input_function()
function_to_change(user_interface.interface,user_interface.mac_address)

