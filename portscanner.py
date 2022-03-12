import socket

print("Please enter an IP Address to scan.")

target = input("> ")

print("*" * 40)
print("*** Scanning: " + target + " ***")
print("*" * 40)

for port in range(1, 65535):
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = s.connect_ex((target, port))
if result == 0:

print("Port: " + str(port) + " is open")

s.close()