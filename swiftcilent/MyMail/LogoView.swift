//
//  LogoView.swift
//  MyMail
//
//  Created by Layer on 2019/10/15.
//  Copyright © 2019 Layer. All rights reserved.
//

import SwiftUI

struct LogoView: View {
    var body: some View {
        Image("logo")
        .shadow(radius: 5)
        .clipShape(Circle())
        .overlay(Circle().stroke(Color.black, lineWidth: 1))
    }
}

struct LogoView_Previews: PreviewProvider {
    static var previews: some View {
        LogoView()
    }
}
