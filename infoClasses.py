from pydantic import BaseModel as bm

class UserInfo(bm):
  user_id : str
  name : str
  xp : int
  level : int


class TagInfo(bm):
  server : str
  creator : str
  name : str
  content : str
