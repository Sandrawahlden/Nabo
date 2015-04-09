# coding: utf-8
# Author: <Andre>
 
from bottle import route, run, template, request, static_file
from os import listdir
list_1 = []

@route("/static/<filename>")
def server_static(filename):
  """CSS"""
  return static_file(filename, root="static")
 
@route("/")
def start():
    """
    This is the sign in page.
    """      
    return template("index")

@route("/board/")
def list_email():
    """
    list the sign in names
    """
    global list_1
    list_1 = []
    files = listdir("user")

    for i in files:
      list_1.append(i[:-4])
      
    return template("board", username=list_1)


@route("/nabo/submit/", method="POST")
def index():
    """Register user and saves the name, surename, adress, email and
    password in a document"""
    global list_1

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
    return template("home", title=email, text=contact, username=list_1)

 
 
run(host='localhost', port=8080, debug=True, reloader=True)
