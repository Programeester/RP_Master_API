from requests import *

URL = "https://rpmasterapi-production.up.railway.app"

def create_user(user):
  response = request.post(url, data=dict(user))
  return response