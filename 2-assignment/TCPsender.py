import time
from socket import *

# Receiver name (IP-address)
receiverName = '192.168.10.155'

# Receiver port
receiverPort = 12002

# Create TCP socket on sender to use for connecting to remote receiver
senderSocket = socket(AF_INET, SOCK_STREAM)

# Open the TCP connection
senderSocket.connect((receiverName, receiverPort))

# Message start number
messageNumber = 10000

# Message
message = 'A' * 1404

# Starting time
startTime = time.time()

# Duration
duration = 30

# Loop
while time.time() - startTime < duration:
    # Payload
    payload = f'{messageNumber};{message}####'

    # Send TCP packet
    senderSocket.send(payload.encode())

    # Print sent payload
    print(f"Sent: {payload}")

    # Increase message number by 1
    messageNumber += 1

    # Sleep to achieve 50 packets/second
    time.sleep(0.02)

# Close TCP socket
senderSocket.close()
