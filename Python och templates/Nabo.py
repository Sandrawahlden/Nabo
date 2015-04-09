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

@route("/board/<filename>")
def list_email():
    """
    list the sign in names
    """
    global list_1
    list_1 = []
    files = listdir("user")
    print files # a list of all filenames in directory wiki

    for i in files:
      list_1.append(i[:-4])
      
    return template("board", articlenames=list_1)


@route("/Nabo/", method="POST")
def index():
    """Register user and saves the email and password in a document"""
    global list_1

    email = request.forms.email
    pwd_1 = request.forms.pwd_1
    text_file = open("user/" + email + ".txt", "w")
    text_file.write(pwd_1)
    text_file.close()
    return template("home", title=email, text=pwd_1, articlenames=list_1)

 
 
run(host='localhost', port=8080, debug=True, reloader=True)
