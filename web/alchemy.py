
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

DATABASE_URL = 'sqlite:///finance.db'

# SQLAlchemy Setup
engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    FirstName = Column(String)
    LastName = Column(String)

    incomes = relationship("Income", back_populates="user")

class Income(Base):
    __tablename__ = 'income'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    income = Column(Integer)
    description = Column(String)
    source = Column(String)
    date = Column(Date, default=datetime.now)
    user = relationship("User", back_populates="incomes")

class Expenses(Base):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    expenses = Column(Integer)
    description = Column(String)
    source = Column(String) 
    date = Column(Date, default=datetime.now)

class Views(Base):
    __tablename__ = 'v_expenses_income'
    
    id = Column(Integer, primary_key=True)
    FullName = Column(String)
    description_expenses = Column(String)
    expenses = Column(String)
    source_expenses = Column(String)
    date_expenses = Column(DateTime)
    description_income = Column(String)
    income = Column(String)
    source_income = Column(String)
    date_income = Column(String)



class Session():
     def __init__(self, session):
        self.session = session
        
     Base.metadata.create_all(engine)
     def return_session():
         Session = sessionmaker(bind=engine)
         session = Session()
         return session

