from socket import *

# Receiver port
receiverPort = 12000

# Create TCP welcoming socket
receiverSocket = socket(AF_INET, SOCK_STREAM)
receiverSocket.bind(('',receiverPort))

# Receiver starts listening for incoming TCP requests
receiverSocket.listen(1)

print ('TCP server is ready to receive')

# Accept connection from sender
connectionSocket, senderAddress = receiverSocket.accept()
print(f'Connected to {senderAddress}')

# Init expected message number
expectedNumber = 10000

# Loop
try:
    while True:
        # Init buffer for incoming message
        buffer = ''

        # Loop
        while True:
            # Receive message chunk from sender and decode
            message_chunk = connectionSocket.recv(2048).decode()

            # Add chunk to buffer
            buffer += message_chunk

            # Check if full message
            if '####' in buffer:
                break  # We have the full message

        # Debug
        #print(f"Received full message: {buffer}")

        # Get message number
        messageNumber = int(buffer.split(';')[0])

        # Check if message number is in order
        if messageNumber != expectedNumber:
            print(f'Warning! Expected {expectedNumber} but got {messageNumber}')

        # Update expected number to match
        expectedNumber = messageNumber + 1

finally:
    # Close connection
    print('Connection closed...')
    connectionSocket.close()
    receiverSocket.close()
