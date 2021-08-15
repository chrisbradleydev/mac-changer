#!/usr/bin/env python3

import optparse
import subprocess


def change_mac(entered_interface, entered_mac_address):
    print(f"[+] changing MAC address for {entered_interface} to {entered_mac_address}")
    subprocess.call(["ifconfig", entered_interface, "down"])
    subprocess.call(["ifconfig", entered_interface, "hw", "ether", entered_mac_address])
    subprocess.call(["ifconfig", entered_interface, "up"])


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="interface to change MAC address")
    parser.add_option("-m", "--mac-address", dest="mac_address", help="new MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] please specify an interface, use --help for more info")
    elif not options.mac_address:
        parser.error("[-] please specify a mac address, use --help for more info")
    return options


parser_options = get_arguments()
change_mac(parser_options.interface, parser_options.mac_address)
