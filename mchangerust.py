import subprocess
import optparse


parse = optparse.OptionParser()
parse.add_option("-i", "--interface", dest="interface", help="interface changer " )
parse.add_option("-m", "--machanger", dest="mac_address", help="mac change")

(inp,arg) = parse.parse_args()
inter = inp.interface
macha = inp.mac_address

subprocess.call(["ifconfig",inter,"down"])
subprocess.call(["ifconfig", inter, "hw","ether" , macha])
subprocess.call(["ifconfig", inter, "up"])

print("Successfull")