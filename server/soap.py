import getMail
import validateEmailAddress

def doSoap(sentence,client):
    bodyBegin = "<soap:Body>"
    bodyEnd = "</soap:Envelope>"
    beginNum = str(sentence).find(bodyBegin)
    endNum = str(sentence).find(bodyEnd)
    # print(beginNum)
    # print(endNum)
    body = str(sentence)[beginNum:endNum]
    # print(body)

    addrbegin = "Addr: "
    subjectbegin = "Subject:"
    contentbegin = "Content:"
    addrnum = body.find(addrbegin)
    subjectnum = body.find(subjectbegin)
    contentnum = body.find(contentbegin)

    print(body[addrnum:subjectnum])
    print(body[subjectnum:contentnum])
    print(body[contentnum:-2])

    a = body[addrnum + 6:subjectnum]
    s = str(body[subjectnum + 8:contentnum])
    c = str(body[contentnum + 8:-2])

    addrs = body[addrnum + 6:subjectnum].split(" ")

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
        getMail.sendEmailBatch(addrs, s, c)
        headerRes = 'HTTP/1.1 200 OK\r\n' \
                    'Connection: close'
        client.send(headerRes.encode())
        client.close()