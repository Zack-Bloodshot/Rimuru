import threading
from Rimuru.modules.sql import BASE, SESSION
from sqlalchemy import (Column, ForeignKey, Integer, String, UnicodeText, UniqueConstraint, func)

class Users(BASE):
  __tablename__ = "users"
  userid = Column(Integer, primary_key=True)
  
  def __init__(self, userid):
    self.userid = userid
 
Users.__table__.create(checkfirst=True)
INSERTION_LOCK = threading.RLock() 

def is_approved(userid):
    try:
        return SESSION.query(Users).get(userid)
    finally:
        SESSION.close()
  
def approve(userid):
  with INSERTION_LOCK:
    user = SESSION.query(Users).get(userid)
    if user:
      SESSION.close()
      return False
    else:
      user = Users(userid)
      SESSION.add(user)
      SESSION.commit()
      return True
  
def disapprove(userid):
  with INSERTION_LOCK:
    user = SESSION.query(Users).get(userid)
    if user:
      SESSION.delete(user)
      SESSION.commit()
      return True 
    else: 
      return False
