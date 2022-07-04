from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.exc import IntegrityError
from sqlalchemy import Column, Integer, String, DateTime, delete
import datetime
import bcrypt


engine = create_engine('sqlite:///db.sqlite3?check_same_thread=False')#, echo=True)

Base = declarative_base()



# List 
class List(Base):
    __tablename__ = 'lists'
    id = Column(Integer, primary_key=True, autoincrement=True)
    link = Column(String,unique=True)
    name = Column(String,unique=True)
    date = Column(DateTime, default=datetime.datetime.utcnow)

class Auth(Base):
  __tablename__ = "auth"
  password = Column(String, primary_key=True)

List.__table__.create(bind=engine, checkfirst=True)
Auth.__table__.create(bind=engine, checkfirst=True)


from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine,autocommit=False,autoflush=False)
session = Session()


#Lists table fucntion
def insert_link(link,name):
  query = List(link=link,name=name)
  try:
    session.add(query)
    session.commit()
  except IntegrityError as e:
    session.rollback()
    session.close()
    return ({"msg":"duplicated"})
  else:
    session.close()
    return ({"msg":"OK"})

def load_link():
  query_data = session.query(List.link,List.name).all()
  session.close()
  return query_data


#auth table function
def change_pw(password):
  query = Auth(password=password)
  try:
    session.add(query)
    session.commit()
  except IntegrityError as e:
    session.rollback()
    session.close()
    return ({"msg":"Not_Changed"})
  else:
    session.close()
    return ({"msg":"OK"})

def load_password():
  query_data = session.query(Auth.password).all()
  session.close()
  return query_data

#delete from list
def delete_link(remove_link):
  if session.query(List).filter(List.link==remove_link).delete() == 1:
    session.query(List).filter(List.link.in_(remove_link)).delete()
    session.commit()
    session.close()
    return ({"msg":"Sucessfully Deleted!"})
  else:
    session.rollback()
    session.close()
    return ({"msg":"Requested Link Not Found"})

#Initalize Default Password
default_password_exist = session.query(Auth.password).all()
if default_password_exist == []:
  password = "defaultpassword".encode('UTF-8')
  encodepassword = bcrypt.hashpw(password,bcrypt.gensalt()).decode('UTF-8')
  query = Auth(password=encodepassword)
  try:
    session.add(query)
    session.commit()
    session.close()
  except:
    session.rollback()
    session.close()

else:
  session.close()