#!/usr/bin/python3

class Member: 


#Constuctor that defines properties of member object.
    def __init__(self,id,globalAccountName,serverNickname,role,points):
        self.id = id
        self.globalAccountName = globalAccountName
        self.serverNickname = serverNickname
        self.role = role
        self.points = points
#Display member method.
    def displayMember(self):
        print ("ID:", self.id, "GlobalAccount:", self.globalAccountName, "Nickname:", self.serverNickname, "Role:", self.role, "Points:", self.points)
        
#Example of creating one object, changing value of an object and displaying an object using a method.
'''mem1 = Member(43344454,"larry","doessuck","officer",150)

mem1.globalAccountName="Jack"

mem1.displayMember()'''