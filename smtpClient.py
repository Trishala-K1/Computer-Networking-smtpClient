from socket import *
#client_email = "<trishala@gmail.com>"
#Server_email = "<arbritrary@gmail.com>"

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    # print("Ready to receive!")
    # Fill in start
    # Fill in end
    recv = clientSocket.recv(1024).decode()
    # print(recv) #You can use these print statement to validate return codes from the server.
    if recv[:3] != '220':
        return
    #    print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1) 
    if recv1[:3] != '250':
        return
    #    print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    mailFrom = 'MAIL FROM: <trishala@gmail.com>\r\n'
    clientSocket.send(mailFrom.encode())
    recv2 = clientSocket.recv(1024).decode()
    if recv2[:3] != '250':
        return
    #   print('250 reply not received from server.')
    # Fill in start
    # Fill in end

    # Send RCPT TO command and handle server response.
    Rcpt = 'RCPT TO: <arbritrary@gmail.com>\r\n'
    clientSocket.send(Rcpt.encode())
    recv3 = clientSocket.recv(1024).decode()
    if recv3[:3] != '250':
        return
    #   print('250 reply not received from server.')
    # Fill in start
    # Fill in end

    # Send DATA command and handle server response.
    Data = 'DATA\r\n'
    clientSocket.send(Data.encode())
    recv4 = clientSocket.recv(1024).decode()
    if recv4[:3] != '354':
        return
    #    print('354 reply not received from server.')
    # Fill in start
    # Fill in end

    # Send message data.
    clientSocket.send(msg.encode())
    recv5 = clientSocket.recv(1024).decode()
    if recv5[:3] != '250':
        return
    #    print('250 reply not received from server.')
    # Fill in start
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    clientSocket.send(endmsg.encode())
    recv6 = clientSocket.recv(1024).decode()
    if recv6[:3] != '250':
        return
    #    print('250 reply not received from server.')
    # Fill in start
    # Fill in end

    # Send QUIT command and handle server response.
    quit_msg = 'QUIT\r\n'
    clientSocket.send(quit_msg.encode())
    recv7 = clientSocket.recv(1024).decode()
    if recv7[:3] != '221':
        return
    #    print('221 reply not received from server.')
    # Fill in start
    # Fill in end
    clientSocket.close()

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
