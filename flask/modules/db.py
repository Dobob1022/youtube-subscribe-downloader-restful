from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.exc import IntegrityError

engine = create_engine('sqlite:///db.sqlite3', echo=True)

Base = declarative_base()


from sqlalchemy import Column, Integer, String, DateTime
class List(Base):
    __tablename__ = 'lists'
    id = Column(Integer, primary_key=True, autoincrement=True)
    link = Column(String,unique=True)
    date = Column(Integer)


List.__table__.create(bind=engine, checkfirst=True)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

testinput = List(link="FUQ")



def insert_link(link):
  query = List(link=link)
  try:
    session.add(query)
    session.commit()
  except IntegrityError as e:
    print ({"result":"duplicated"})
    return ({"result":"duplicated"})
  else:
    print ({"result":"OK"})
    return ({"result":"OK"})

