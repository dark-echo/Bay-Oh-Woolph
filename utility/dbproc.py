from discord.ext import commands
from utils import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from member import Base, Member
from config import Config
import discord
import asyncio


class Baydb:
    engine = create_engine(Config.MAIN['dbpath'])
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    conn = engine.connect()
