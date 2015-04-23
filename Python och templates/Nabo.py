# coding: utf-8
# Author: <Andre, Hannes>
 
from bottle import *
from os import listdir

username = ""
email = ""
profile_pic = ""
age = ""
lgh = ""
tel_nr = ""
likes = ""

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

	contact.extend((name, surname, adress, pwd_1, "/static/Bilder/avatar.png", "null", "null", "null", "null"))

        mail = email + ".txt"
        
        if mail in listdir("user"):
                
                return "user already exist"
        
        else:
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
                return template("myProfile", title=email, text=contact, firstname=firstname, username=username)


@route("/myProfile/")
def register_user():
	"""Register user and saves the name, surename, adress, email and
	password in a document"""
	global username, email

	user = username.replace("\n", " ")
        first = user.split(" ")
        firstname = first[0]
	return template("myProfile", username=username, firstname=firstname)  
  
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

@route("/nabos/")
def nabolist():
	"""Appends usernames into name_list and prints it on the nabopage """
        global username, profile_pic
        
        user_list = listdir("user")
        name_list = []

        for user in user_list:
                f = open("user/" + user, "r")
                text_file = f.readlines()
                firstname = text_file[0]
                surname = text_file[1]
                nabos = firstname + surname
                name_list.append(nabos)
        if text_file[4] == "null":
                profile_pic = "/static/Bilder/avatar.png"
                print profile_pic
        else:
                profile_pic = text_file[4]
                print profile_pic
                        
	return template("nabos", user_list=user_list, name_list=name_list, username=username, profile_pic=profile_pic)


@route("/editProfile/")
def edit_profile():
	"""
	This is the mail inbox
	"""
	global username, profile_pic

        contact = []
	name = request.forms.name
	surname = request.forms.surname
	adress = request.forms.adress
	email = request.forms.email
	pwd_1 = request.forms.pwd_1
        profile_pic = request.forms.profile_pic
        """Age or birth date?"""
        age = request.forms.age
        lgh = request.forms.lgh
        tel_nr = request.forms.tel_nr
        """Likes in what form?"""
        likes = request.forms.likes
        
	contact.extend((name, surname, adress, pwd_1, profile_pic, age, lgh, tel_nr, likes))
	
	
	return template("editProfile", username=username, profile_pic=profile_pic, age=age, lgh=lgh, tel_nr=tel_nr, likes=likes)
    

@route("/inbox/")
def inbox():
	"""
	This is the mail inbox
	"""
	global username
	
	return template("inbox", username=username)


@route("/help/")
def nabo_help():
	"""
	This is the nabo help.
	"""
	global username
	
	return template("help", username=username)
    

@route("/contact/")
def contact_us():
	"""
	This is the contact site where you can find how to contact us.
	"""
	global username
	
	return template("contact", username=username)


@route("/about/")
def about_us():
	"""
	This is the mail inbox
	"""
	global username
	
	return template("about", username=username)

run(host='localhost', port=8080, debug=True, reloader=True)
