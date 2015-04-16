# coding: utf-8
# Author: <Andre, Hannes>
 
from bottle import route, run, template, request, static_file
username = ""
email = ""

@route("/static/<filename>")
def server_static(filename):
  """CSS"""
  return static_file(filename, root="static")

@route('/static/<filepath:path>')
def server_static(filepath):
  """pictures"""
  return static_file(filepath, root='/static/Bilder')
 
@route("/")
def start():
  """
  This is the sign in page.
  """      
  return template("index")


@route("/myProfile/", method="POST")
def register_user():
  """Register user and saves the name, surename, adress, email and
  password in a document"""
  global username, email

  contact = []
  name = request.forms.name
  surname = request.forms.surname
  adress = request.forms.adress
  email = request.forms.email
  pwd_1 = request.forms.pwd_1

  contact.extend((name, surname, adress, pwd_1))

  text_file = open("user/" + email + ".txt", "w")

  for i in contact:
    text_file.write(i)
    text_file.write("\n")

  text_file.close()

  f = open("user/" + email + ".txt", "r")
  text_file = f.readlines()
  firstname = text_file[0]
  surname = text_file[1]
  username = firstname + surname
  f.close()
    
  return template("myProfile", title=email, text=contact, username=username)
  
  
@route("/home/", method="POST")
def sign_in():
  """Signing in existing user and goes to home"""
  global username 

  email = request.forms.mail
  pwd = request.forms.pwd
    
  f = open("user/" + email + ".txt", "r")
  text_file = f.readlines()
  pwd_2 = text_file[3]
  f.close()

  if pwd == pwd_2:
    return poop
  else:
    f = open("user/" + email + ".txt", "r")
    text_file = f.readlines()
    firstname = text_file[0]
    surname = text_file[1]
    username = firstname + surname
    f.close()
    return template("home", title=email, pwd=pwd, username=username)
    

@route("/home/<name>")
def my_profile(name):
  global username, email
    
  f = open("user/" + email + ".txt", "r")
  text_file = f.readlines()
  firstname = text_file[0]
  surname = text_file[1]
  name = firstname + surname
  f.close()
  return template("myProfile", username=username) 
 
run(host='localhost', port=8080, debug=True, reloader=True)
