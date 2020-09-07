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
        parse.error("Specify the interface son ,type --help for more details")
    elif not options.mac_address:
        parse.error("specify the mac address you want type --help for more info")
    return options

def function_to_change(interface,mac_addr):
    subp.call(["ifconfig",interface,"down"])
    subp.call(["ifconfig",interface,"hw","ether",mac_addr])
    subp.call(["ifconfig",interface,"up"])

def get_current_mac(interface):
    ifconfig_result=subp.check_output(["ifconfig",interface])
    rege_ifconfig=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig_result))
    if rege_ifconfig:
         return rege_ifconfig.group(0)
    else:
         return None

print("Starting")
user=input_function()
function_to_change(user.interface,user.mac_address)
final_mac=get_current_mac(user.interface)
if final_mac==user.mac_address:
    print("MAC successfully changed")
    print("Your NEW MAC :",final_mac)
else:
    print("MAC could NOT be changed check your input")

