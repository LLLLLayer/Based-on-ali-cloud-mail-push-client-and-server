import requests

def sendHTTPSoap(addrs,subject,content):
    myAddr=''
    for addr in addrs:
        myAddr = myAddr +" " + addr
    mySubject=subject
    myContent=content

    SOAP = "<?xml version=\"1.0\"?>\n"+"<soap:Envelope"+\
           "xmlns:soap=\"http://www.w3.org/2001/12/soap-envelope\""+\
           "soap:encodingStyle=\"http://www.w3.org/2001/12/soap-encoding\">"+\
           "<soap:Header>"+\
           "<soap:Body>"+"Addr:"+myAddr+"Subject:"+mySubject+"Content:"+myContent+\
           "</soap:Envelope>"

    res = requests.request(method='POST',
                 url='http://139.196.161.28:8888/',
                 # url='http://127.0.0.1:8888/',
                 data=SOAP.encode("utf-8"))
    return res

def sendHTTPRest(addrs,subject,content):
    myAddr=addrs
    mySubject=subject
    myContent=content

    REST = ""

    res = requests.request(method='POST',
                 url='http://139.196.161.28:8888/' + myAddr + '/' + mySubject + '/' + myContent + '/',
                 # url='http://127.0.0.1:8888/'+myAddr+'/'+mySubject+'/'+myContent + '/',
                 data=REST.encode("utf-8"))
    return res

# sendHTTPsoap("","","")