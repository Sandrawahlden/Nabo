# coding: utf-8
# Author: <Andre, Hannes>
 
from bottle import *
from os import listdir
username = ""
email = ""

@route("/static/<filepath:path>")
def server_static(filepath):
	"""CSS"""
	return static_file(filepath, root="static")

@route("/")
def start():
	"""
	This is the sign in page.
	"""      
	return template("index")

@route("/nabos/")
def nabolist():
	"""Appends usernames into name_list and prints it on the nabopage """
        global username
        
        user_list = listdir("user")
        name_list = []

        for user in user_list:
                f = open("user/" + user, "r")
                text_file = f.readlines()
                firstname = text_file[0]
                surname = text_file[1]
                nabos = firstname + surname
                name_list.append(nabos)
	return template("nabos", user_list=user_list, name_list=name_list, username=username)


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

@route("/myProfile/")
def register_user():
	"""Register user and saves the name, surename, adress, email and
	password in a document"""
	global username, email

	return template("myProfile", username=username)  
  
@route("/home/", method="POST")
def sign_in():
	"""Signing in existing user and goes to home"""
	global username 

	email = request.forms.mail
	pwd_1 = request.forms.pwd

	f = open("user/" + email + ".txt", "r")
	text_file = f.readlines()
	print pwd_1
	pwd_2 = text_file[3].replace("\n", "")
        print pwd_2
	if pwd_1 == pwd_2:
		firstname = text_file[0]
		surname = text_file[1]
		username = firstname + surname
		f.close()
		return template("home", username=username)
	else:
		return "<p>Login Failed!</p>"


@route("/home/")
def my_profile():
        global username, email

        return template("home", username=username) 

run(host='localhost', port=8080, debug=True, reloader=True)
