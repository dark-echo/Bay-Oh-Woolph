#!/usr/bin/python3
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Member(Base): 
    __tablename__ = 'member'

    id = Column(Integer, primary_key=True)
    globalName = Column(String(250), nullable=True)
    nickname = Column(String(250), nullable=True)
    role = Column(String(250), nullable=True)
    points = Column(Integer, nullable=True, default=0)
    

    def __init__(self,id,globalAccountName,serverNickname,role):
        self.id = id
        self.globalName = globalAccountName
        self.nickname = serverNickname
        self.role = role


#Display member method.
    def __str__(self):
        return "\n AccountName: %s Nickname: %s Points: %s" % (self.globalName,self.nickname,self.points)

#Example of creating one object, changing value of an object and displaying an object using a method.
'''mem1 = Member(43344454,"larry","doessuck","officer",150)

mem1.globalAccountName="Jack"

mem1.displayMember()'''

engine = create_engine('sqlite:///bayohwoolph.db')

Base.metadata.create_all(engine)
