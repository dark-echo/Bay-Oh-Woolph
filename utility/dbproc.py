from discord.ext import commands
from utils import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from member import Base, Member
import discord
import asyncio
from rank import Ranks



class Baydb:

    engine = create_engine('sqlite:///C:\\Users\\Daniel\\Source\Repos\\Bay-Oh-Woolph\\bayohwoolph.db')
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()














