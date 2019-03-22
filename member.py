#!/usr/bin/python3
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.types import *
from sqlalchemy import create_engine
from config import Config
import _datetime
import logging
logger = logging.getLogger('bayohwoolph.member')

Base = declarative_base()

class Member(Base):
    """Tracking data about Dark Echo members."""

    __tablename__ = 'member'

    id = Column(BigInteger, primary_key=True)
    globalName = Column(String(250), nullable=False)
    nickname = Column(String(250), nullable=True)
    role = Column(String(250), nullable=True)
    points = Column(BigInteger, nullable=True, default=0)
    rankId = Column (BigInteger, nullable=True)
    joinDate = Column (DateTime, nullable=True)
    checkInDate = Column (DateTime, nullable=True)
    nextDate = Column (DateTime, nullable=True)
    

    def __init__(self,id,globalAccountName,serverNickname,role,rankId,joinDate):
        self.id = id
        self.globalName = globalAccountName
        self.nickname = serverNickname
        self.role = role
        self.rankId = rankId
        self.joinDate = joinDate


#Display member method.
    def displayMember(self):
        logger.info("ID:", self.id, "GlobalAccount:", self.globalName, "Nickname:", self.nickname, "Role:", self.role)

#Example of creating one object, changing value of an object and displaying an object using a method.
'''mem1 = Member(43344454,"larry","doessuck","officer",150)

mem1.globalAccountName="Jack"

mem1.displayMember()'''




engine = create_engine(Config.MAIN['dbpath'])

Base.metadata.create_all(engine)
