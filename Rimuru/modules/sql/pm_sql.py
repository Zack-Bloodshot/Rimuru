from Rimuru.modules.sql import BASE, SESSION
from sqlalchemy import (Column, ForeignKey, Integer, String, UnicodeText, UniqueConstraint, func
import threading 

class Users(BASE):
  __tablename__ = "users"
  userid = Column(Integer, primary_key=True)
  
  def __init__(self, userid):
    self.userid = userid
 
Users.__table__.create(checkfirst=True)
LOCK = threading.Rlock()

def is_approved(userid):
  try:
    user = SESSION.query(Users).get(userid)
    if user:
      return True
    else:
      return False
  finally:
    SESSION.close()
  
def approve(userid):
  user = SESSION.query(Users).get(userid)
  if user:
    SESSION.close()
    return False
  else:
    user = Users(userid)
    SESSION.add()
    SESSION.commit()
    return True
  
def disapprove(userid):
  user = SESSION.query(Users).get(userid)
  if user:
    SESSION.delete(user)
    SESSION.commit()
    return True 
  else: 
    return False
