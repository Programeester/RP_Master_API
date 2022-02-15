from requests import *

URL = "https://rpmasterapi-production.up.railway.app"

def create_user(user):
  response = request.post(url, data=dict(user))
  return response

def create_tag(tag):
  response = request.post(url, data=dict(tag))
  return response

def
