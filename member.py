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
    globalName = Column(String(250), nullable=False)
    nickname = Column(String(250), nullable=True)
    role = Column(String(250), nullable=True)
    points = Column(Integer, nullable=True)

    engine = create_engine('sqlite:///member.db')

    Base.metadata.create_all(engine)

#Display member method.
    def displayMember(self):
        print ("ID:", self.id, "GlobalAccount:", self.globalName, "Nickname:", self.Nickname, "Role:", self.role, "Points:", self.points)
        
#Example of creating one object, changing value of an object and displaying an object using a method.
'''mem1 = Member(43344454,"larry","doessuck","officer",150)

mem1.globalAccountName="Jack"

mem1.displayMember()'''