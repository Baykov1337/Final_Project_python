
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Date, text
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from datetime import datetime
from create_veiw import Create_VIEW
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

class Session():
     def __init__(self, session):
        self.session = session
        
     Base.metadata.create_all(engine)
     def return_session():
         Session = sessionmaker(bind=engine)
         session = Session()
         session.execute(text(Create_VIEW.sql_query()))
         return session
class Views(Base):
    __tablename__ = 'v_expenses_income'
    
    id = Column(Integer, primary_key=True)
    FullName = Column(String, default="")
    description_expenses = Column(String, default="")
    expenses = Column(String, default="")
    source_expenses = Column(String, default="")
    date_expenses = Column(DateTime, default=datetime.now)
    description_income = Column(String, default="")
    income = Column(String, default="")
    source_income = Column(String, default="")
    date_income = Column(String, default="")

