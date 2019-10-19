//
//  ContentView.swift
//  MyMail
//
//  Created by Layer on 2019/10/15.
//  Copyright © 2019 Layer. All rights reserved.
//

import SwiftUI
struct ContentView: View {
    @State var addr = ""
    @State var isPresented = false
    
    var body: some View {
        VStack {
            MapView()//map
                .frame(height: 200)
                .edgesIgnoringSafeArea(.top)
            
            LogoView()//logo
                .offset(x: 0, y: -80)

            VStack {
                Text("Email Pushing")
                    .font(.largeTitle)
                    .fontWeight(.bold)
                    .multilineTextAlignment(.center)
                    .padding()
                
                DateView()
                
                HStack {
                    Text("Target Email Address:")
                        .font(.headline)
                        .multilineTextAlignment(.center)
                    
                    Text(/*@START_MENU_TOKEN@*/"Enter by newline"/*@END_MENU_TOKEN@*/)
                        .font(.caption)
                        .fontWeight(.ultraLight)
                    
                    Spacer()
                }
                .padding()

                TextField("Enter the target email address here...", text: self.$addr){
//                    print(self.addr)
                }
                .padding()
                
                Spacer()
            }
            .padding()
            .offset(x: 0, y: -80)
            Spacer()
           
            Button(action: {
//                print(self.addr)
                self.isPresented = true
            }) {
                Text("Next")
                    .font(.headline)
                    .fontWeight(.light)
                    .foregroundColor(Color.blue)
                    .offset(x: 0, y: -20)
                    .sheet(isPresented: $isPresented, content: {
                        EmailView(addr: self.addr)
                    })
            }
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
