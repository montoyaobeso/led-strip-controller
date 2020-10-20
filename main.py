"""
A simple Python script to set colors on a shitty cheap RGB Bluetooth LED Strip
"""
# simple inquiry example
import bluetooth

nearby_devices = bluetooth.discover_devices(lookup_names=True)
print("Found {} devices.".format(len(nearby_devices)))

for addr, name in nearby_devices:
    print("  {} - {}".format(addr, name))

# bluetooth low energy scan
from bluetooth.ble import DiscoveryService

service = DiscoveryService()
devices = service.discover(2)

for address, name in devices.items():
    print("name: {}, address: {}".format(name, address))





# serverMACAddress = '00:1f:e1:dd:08:3d'
# port = 3
# s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
# s.connect((serverMACAddress, port))

# while True:
#     text = str(raw_input()) # Note change to the old (Python 2) raw_input
#     if text == "quit":
#         break
#     print(text.split(','))
#
#     if len(text.split(',')) == 3:
#         R, G, B = text.split(',')
#         print("R: {}, G: {}, B: {}".format(R, G, B))
#     else:
#         print("Enter R, G, B values as 'RED,GREEN,BLUE'")
    # s.send(text)
# sock.close()