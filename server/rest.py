import validateEmailAddress
import getMail
def doRest(postUrl,client):
    rec = postUrl.split("/")
    for str in rec:
        print(str)

    addr = rec[1][:-1]
    subject = rec[2]
    content = rec[3][:-3]

    addrs = addr.split(",")

    flag = True
    for addr in addrs:
        print(addr)
        if (validateEmailAddress.validateEmailAddress(addr)) == False:
            headerRes = 'HTTP/1.1 400 OK\r\n' \
                        'Connection: close'
            client.send(headerRes.encode())
            client.close()
            falg = False
            break

    if (flag == True):
        getMail.sendEmailBatch(addrs, subject, content)
        headerRes = 'HTTP/1.1 200 OK\r\n' \
                    'Connection: close'
        client.send(headerRes.encode())
        client.close()