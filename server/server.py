import socket
import getMail
import validateEmailAddress
import soap
import rest

bind_ip = "127.0.0.1"
serverPort = 8888
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, serverPort))
server.listen(5)
print('the server is ready to receive')

while True:
    client, addr = server.accept()
    print("Accepted connection from: %s:%d" % (addr[0], addr[1]))
    try:
        reqFrom = str(addr[0])+str(addr[1])
        getMail.emailFrom=reqFrom

        sentence = client.recv(1024)
        print(str(sentence))

        postUrl = str(sentence).split(" ")[1]
        # print(postUrl)

        # soap
        if(postUrl == "/"):
            print("soap")
            soap.doSoap(sentence,client)
        else:
            print("rest")
            rest.doRest(postUrl,client)

    except IOError:
        print("error")
