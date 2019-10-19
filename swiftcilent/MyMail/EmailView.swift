//
//  EmailView.swift
//  MyMail
//
//  Created by Layer on 2019/10/16.
//  Copyright © 2019 Layer. All rights reserved.
//

import SwiftUI
import MessageUI
import SwiftHTTP

struct EmailView: View {
    @State var subject: String = ""
    @State var content: String = ""
    @State var flag: Bool = false
    
    let addr: String
    var body: some View {
        VStack {
            Spacer()
            Text("Email Subject:")
                .font(.title)
                .fontWeight(.light)
                .offset(x: -70, y:0)
                
            HStack {
                Spacer(minLength: 30)
                TextField("Enter the message subject here...", text: $subject){
                    print(self.subject)
                    
                }
                Spacer(minLength: 30)
            }
            Spacer()
            Text("Email content:")
                .font(.title)
                .fontWeight(.light)
                .offset(x: -70, y:0)

            HStack {
                Spacer(minLength: 30)
                TextField("Enter the message here...", text: $content){
                    print(self.content)
                    
                }
//                .frame(height: 300)
                Spacer(minLength: 30)
            }
            Spacer()
            Spacer()
            Spacer()
            HStack {
                Button(action: {
                    print("目标地址：" + self.addr)
                    print("邮件主题：" + self.subject)
                    print("邮件内容：" + self.content)
                    let url:String = "http://139.196.161.28:8888/" + self.addr + ",/" + self.subject + "/" + self.content + "/"
                    let params = [""]
                    HTTP.POST(url, parameters: params) { response in
                        self.flag = true
                           if let err = response.error {
                            print("error: \(err.localizedDescription)")
                            
                        }
                    }
                }) {
                    Text("Send")
                        .sheet(isPresented: $flag, content: {
                            ResView()
                        })
                    .padding(30)
                }
            }
        }
    }
}

struct EmailView_Previews: PreviewProvider {
    static var previews: some View {
        EmailView(addr:"test")
    }
}

