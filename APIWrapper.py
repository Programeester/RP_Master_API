from requests import *

URL = "https://rpmasterapi-production.up.railway.app"

def create_user(user):
  response = request.post(f"{url}/users/create/", data=dict(user)).json
  return response

def create_tag(tag):
  response = request.post(url, data=dict(tag)).json
  return response
