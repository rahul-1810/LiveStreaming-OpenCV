import socket, cv2 , pickle,struct

# Creating_Socket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = 5050
socket_address = ('<your IP>',port)

# Socket_Binding
server_socket.bind(socket_address)

# Socket Listen
server_socket.listen(5)
print("LISTENING AT:",socket_address)

# Socket Accept
while True:
    client_socket,addr = server_socket.accept()
    print('GOT CONNECTION FROM:',addr)
    if client_socket:
        vid = cv2.VideoCapture(0)
        
        while(vid.isOpened()):
            img,frame = vid.read()
            a = pickle.dumps(frame)
            message = struct.pack("Q",len(a))+a
            client_socket.sendall(message)
            
            cv2.imshow('TRANSMITTING VIDEO',frame)
            key = cv2.waitKey(1) & 0xFF
            if key ==ord('q'):
                client_socket.close()
