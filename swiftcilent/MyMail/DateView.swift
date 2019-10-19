//
//  DateView.swift
//  MyMail
//
//  Created by Layer on 2019/10/16.
//  Copyright © 2019 Layer. All rights reserved.
//

import SwiftUI

struct DateView: View {
    var now = Date()
    static let dateFormatter: DateFormatter = {
    let formatter = DateFormatter()
    formatter.dateStyle = .long
    return formatter
    }()
    
    var body: some View {
        Text("The time is: \(now, formatter: Self.dateFormatter)")
            .font(.body)
            .fontWeight(.ultraLight)
            .padding()
    }
}

struct DateView_Previews: PreviewProvider {
    static var previews: some View {
        DateView()
    }
}
