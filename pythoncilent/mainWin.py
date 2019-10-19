import tkinter
import myCilent
import tkinter.messagebox

def mainWin():
    root=tkinter.Tk()
    root.title("Email Pushing")
    root.geometry("500x700+500+50")

    # label title
    labelTitle = tkinter.Label(root, text="Email Pushing", font=("黑体", 35))
    labelTitle.place(x=110, y=20, width=300, height=40)

    # label email address
    labeladdr = tkinter.Label(root, text="Target Email Address:", font=("黑体", 20))
    labeladdr.place(x=30, y=70, width=210, height=25)

    # label border
    labelBorder = tkinter.Label(root, text="————————————————————", font=("黑体", 20))
    labelBorder.place(x=40, y=105, width=408, height=5)

    # text addr
    textAddr = tkinter.Text(root, width=57, height=8,relief = 'sunken')
    textAddr.place(x=40, y=110,)
    textAddr.insert(1.0,'17635366177@163.com')
    scroll1 = tkinter.Scrollbar()
    scroll1.place(x=450, y=110, height=115)
    scroll1.config(command=textAddr.yview)
    textAddr.config(yscrollcommand=scroll1.set)

    # label border
    labelBorder = tkinter.Label(root, text="————————————————————", font=("黑体", 20))
    labelBorder.place(x=40, y=221, width=408, height=5)

    # label Subject
    labelSubject = tkinter.Label(root, text="Email Subject:", font=("黑体", 20))
    labelSubject.place(x=40, y=240, width=130, height=25)

    # Entry Subject
    inputSubject = tkinter.Variable()
    entrySubject = tkinter.Entry(root, textvariable = inputSubject)
    entrySubject.place(x=40, y=270, width=425, height=30)
    inputSubject.set("SubjectTEST")

    # label Email Content
    labelConntent = tkinter.Label(root, text="Email Content:", font=("黑体", 20))
    labelConntent.place(x=30, y=320, width=150, height=25)

    # label border
    labelBorder = tkinter.Label(root, text="————————————————————", font=("黑体", 20))
    labelBorder.place(x=40, y=360, width=408, height=5)

    # text Email Content
    textContent = tkinter.Text(root, width=57, height=20,relief = 'sunken')
    textContent.place(x=40, y=365)
    scroll2 = tkinter.Scrollbar()
    scroll2.place(x=450, y=365, height=268)
    scroll2.config(command=textContent.yview)
    textContent.config(yscrollcommand=scroll2.set)
    textContent.insert(1.0,'ContentTEST')

    # label border
    labelBorder = tkinter.Label(root, text="————————————————————", font=("黑体", 20))
    labelBorder.place(x=40, y=632, width=408, height=5)

    # button ok
    def funcsoap():
        # Gets the target email address
        emailAddress = textAddr.get("0.0", "end").split("\n")
        emailAddress.pop()
        print('TargetEmailAddress:')
        for addr in emailAddress:
            print(addr)
        # Get email subject
        emailSubject=inputSubject.get()
        print('EmailSubject:\n'+emailSubject)
        # Get email subject
        emailContent = textContent.get(0.0, 'end')
        print('EmailContent:\n'+emailContent)
        res = myCilent.sendHTTPSoap(emailAddress,emailSubject,emailContent)
        if(str(res)=="<Response [400]>"):
            print("格式错误")
            tkinter.messagebox.showerror('Error', 'The E-mail format is incorrect！')
        else:
            tkinter.messagebox.showinfo('', 'Email sent successfully！')

    buttonOKsoap = tkinter.Button(root,text="OK.SOAP",command=funcsoap)
    buttonOKsoap.place(x=350, y=650, width=100, height=25)

    def funcrest():
        # Gets the target email address
        emailAddress = textAddr.get("0.0", "end").replace("\n",",")
        print('TargetEmailAddress:')
        print(emailAddress)
        # Get email subject
        emailSubject=inputSubject.get()
        print('EmailSubject:\n'+emailSubject)
        # Get email subject
        emailContent = textContent.get(0.0, 'end')
        print('EmailContent:\n'+emailContent)
        res = myCilent.sendHTTPRest(emailAddress,emailSubject,emailContent)
        if(str(res)=="<Response [400]>"):
            print("格式错误")
            tkinter.messagebox.showerror('Error', 'The E-mail format is incorrect！')
        else:
            tkinter.messagebox.showinfo('', 'Email sent successfully！')

    buttonOKrest = tkinter.Button(root,text="OK.REST",command=funcrest)
    buttonOKrest.place(x=240, y=650, width=100, height=25)

    root.mainloop()

if __name__ == "__main__":
    mainWin()