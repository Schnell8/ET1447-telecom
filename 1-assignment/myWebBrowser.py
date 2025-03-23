from socket import *

# Server name
serverName = "www.ingonline.nu"

# Server port
serverPort = 80

# Example board
board = "xoxoeoeex"

# Create HTTP GET request string
request = f"GET /tictactoe/index.php?board={board} HTTP/1.1\r\nHost: {serverName}\r\nConnection: close\r\n\r\n"

# Create TCP socket
clientSocket = socket(AF_INET, SOCK_STREAM)

# Connect to server
clientSocket.connect((serverName, serverPort))

# Send HTTP request
clientSocket.send(request.encode())

# Receive and print response from server
response = clientSocket.recv(1024)
print(response.decode())

# Close socket
clientSocket.close()
