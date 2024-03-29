from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.exc import IntegrityError
from sqlalchemy import Column, Integer, String, DateTime, delete, update
import datetime
import bcrypt


engine = create_engine('sqlite:///db/db.sqlite3?check_same_thread=False')#, echo=True)

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
  id = Column(Integer,primary_key=True, autoincrement=True)
  password = Column(String)

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
    return ({"msg":"Link is duplicated!"})
  else:
    session.close()
    return ({"msg":"OK"})

def load_link():
  query_data = session.query(List.id,List.link,List.name).all()
  session.close()
  return query_data


#auth table function
def change_pw(new_password):
  try:
    auth = session.query(Auth).filter(Auth.id == '1').first()
    auth.password = new_password    
    session.commit()
    session.close()
    return ({"msg":"OK"})
  except IntegrityError as e:
    session.rollback()
    session.close()
    print(e)
    return ({"msg":"Not_Changed"})
  except:
    return({"msg":"Something is Wrong!"})

    

def load_password():
  query_data = session.query(Auth.password).all()
  print(query_data)
  session.close()
  return query_data

#delete from list
def delete_link(removed_id):
  if session.query(List).filter(List.id.in_(removed_id)).delete() != 0: # remove_id is list, so list remove funcion.
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