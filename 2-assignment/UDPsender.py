import time
from socket import *

# Receiver name (IP-address)
receiverName = '192.168.10.155'

# Receiver port
receiverPort = 12000

# Create UDP socket
senderSocket = socket(AF_INET, SOCK_DGRAM)

# Message start number
messageNumber = 10000

# Message
message = 'A' * 1461

# Starting time
startTime = time.time()

# Duration
duration = 30

# Loop
while time.time() - startTime < duration:
    # Payload
    payload = f'{messageNumber};{message}####'

    # Send UDP packet
    senderSocket.sendto(payload.encode(), (receiverName, receiverPort))
    
    # Print sent payload
    print(f"Sent: {payload}")

    # Increase message number by 1
    messageNumber += 1

    # Sleep to achieve 15 packets/second
    time.sleep(0.0666666666666667)

# Close UDP socket
senderSocket.close()
