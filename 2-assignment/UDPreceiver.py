from socket import *

# Receiver port
receiverPort = 12000

# Create UDP socket and bind to receiver port
receiverSocket = socket(AF_INET, SOCK_DGRAM)
receiverSocket.bind(('', receiverPort))

# Print ready message
print('UDP server is ready to receive')

# Init expected message number
expectedNumber = 10000

# Loop
try:
    while True:
        # read sender message and decode
        message, senderAddress = receiverSocket.recvfrom(2048)
        decodedMessage = message.decode()

        # Get message number
        messageNumber = int(decodedMessage.split(';')[0])

        # Check if message number is in order
        if messageNumber != expectedNumber:
            print(f'Warning! Expected {expectedNumber} but got {messageNumber}')

        # Update expected number to match
        expectedNumber = messageNumber + 1
finally:
    # Close the socket when done
    receiverSocket.close()
    print("Receiver socket closed.")
