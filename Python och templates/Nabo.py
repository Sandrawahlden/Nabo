# encoding: utf-8
# Author: <Andre, Hannes>
 
from bottle import *
from os import listdir
from datetime import datetime
import codecs

username = ""
email = ""
profile_pic = ""
age = ""
lgh = ""
tel_nr = ""
likes = ""
message = ""
firstname = ""
lastname = ""
pwd = ""
pic = ""
age_1 = ""
streetname = ""
town = ""
appartment = ""
tel = ""
like = ""


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
	global username, email, lastname, pwd, age_1, streetname, town, appartment, tel, like

	contact = []
	name = request.forms.name
	surname = request.forms.surname
	email = request.forms.email
	pwd_1 = request.forms.pwd_1
        pwd_2 = request.forms.pwd_2
        street = request.forms.adress
        city = request.forms.city
	if pwd_1 == pwd_2:
                contact.extend((name, surname, pwd_1, "/static/Bilder/avatar.png", street, city, "Du har inte angivit din alder annu", "Vilken vaning bor du pa?", "Ange ditt telefonnummer", "Vad gillar du?"))

                mail = email + ".txt"
                
                if mail in listdir("user"):

                        message = "Epostadress finns redan registrerad!"
                        return template("registerProfileFail", message=message)
                
                else:
                        text_file = codecs.open("user/" + email + ".txt", "w", "utf-8")
                        
                        for i in contact:
                                text_file.write(i)
                                text_file.write("\n")
                        text_file.close()

                        f = codecs.open("user/" + email + ".txt", "r", "utf-8")
                        text_file = f.readlines()
                        firstname = text_file[0]
                        surname = text_file[1]
                        username = firstname + surname
                        f.close()
                        return template("myProfile", title=email, text=contact, firstname=firstname, username=username, pwd_1=pwd_1, pwd_2=pwd_2, profile_pic=profile_pic, lastname=lastname, age_1=age_1, streetname=streetname, town=town, appartment=appartment, tel=tel, like=like)
                
        else:
                message = "Passwordsen matchar inte varandra!"
                return template("registerProfileFail", message=message)
  
  
@route("/home/", method="POST")
def sign_in():
	"""Signing in existing user and goes to home"""
	global username, email, message, profile_pic

	email = request.forms.mail
	pwd_1 = request.forms.pwd
	mailadress = email + ".txt"
        if mailadress in listdir("user"):
                f = codecs.open("user/" + email + ".txt", "r", "utf-8")
                text_file = f.readlines()
                pwd_2 = text_file[2].replace("\n", "")
                if pwd_1 == pwd_2:
                        firstname = text_file[0]
                        surname = text_file[1]
                        username = firstname + surname
                        f.close()
                        
                        anslag_list = listdir("anslagsfolder")
                        namn_list = []
                        pict_list = []
                        content_list = []
                        time_list = []

                        """prints anslag"""
                        for anslag in reversed(anslag_list):
                                f2 = codecs.open("user/" + email + ".txt", "r", "utf-8")
                                anslag_file = f2.readlines()
                                try:
                                    namn = anslag_file[0]
                                except IndexError:
                                    namn = "Namn saknas"
                                try:
                                    pict = anslag_file[1]
                                except IndexError:
                                    pict = "Bild saknas"
                                try:
                                    cont = anslag_file[2]
                                except IndexError:
                                    cont = "Content saknas"
                                time_list.append(anslag)
                                namn_list.append(namn)
                                pict_list.append(pict)
                                content_list.append(cont)
                        return template("home", username=username, email=email, profile_pic=profile_pic, anslag_list=anslag_list, namn_list=namn_list, pict_list=pict_list, content_list=content_list, time_list=time_list)
                else:
                        message = "Fel password!"
                        return template("loginProfileFail", message=message)

        else:
                message = "Epostadressen finns inte registrerad!"
                return template("loginProfileFail", message=message)
	

@route("/myProfile/")
def user_profile():
	"""Shows the userprofile"""
	global username, email, profile_pic

        f = codecs.open("user/" + email + ".txt", "r", "utf-8")
	text = f.readlines()
	profile_pic = text[3]
        firstname = text[0]
        age_1 = text[6]
        appartment = text[7]
        tel = text[8]
        like = text[9]
        f.close()

	return template("myProfile", username=username, firstname=firstname, profile_pic=profile_pic, age_1=age_1, appartment=appartment, tel=tel, like=like)


@route("/home/")
def home():
        global username, email, profile_pic
        """Lists for all lines in anslag_file"""
        anslag_list = listdir("anslagsfolder")
        namn_list = []
        pict_list = []
        content_list = []
        time_list = []

        """prints anslag"""
        for anslag in reversed(anslag_list):
                f = codecs.open("user/" + email + ".txt", "r", "utf-8")
                text_file = f.readlines()
                try:
                    namn = text_file[0]
                except IndexError:
                    namn = "Namn saknas"

                try:
                    pict = text_file[1]
                except IndexError:
                    pict = "Bild saknas"

                try:
                    cont = text_file[2]
                except IndexError:
                    cont = "Content saknas"
                time_list.append(anslag)
                namn_list.append(namn)
                pict_list.append(pict)
                content_list.append(cont)
                print time_list, namn_list, pict_list, content_list
        return template("home", username=username, email=email, profile_pic=profile_pic, anslag_list=anslag_list, namn_list=namn_list, pict_list=pict_list, content_list=content_list, time_list=time_list)

##@route("/home/", method="POST")
##def create_anslag():
##        """create anslag with date as filename"""
##        global username, email, profile_pic
##
##        anslag_title = datetime.now()
##        year = str(anslag_title.year)
##        month = str(anslag_title.month)
##        day = str(anslag_title.day)
##        hour = str(anslag_title.hour)
##        minute = str(anslag_title.minute)
##        if len(month) < 2:
##                month = "0" + month
##        if len(day) < 2:
##                day = "0" + day
##        if len(hour) < 2:
##                hour = "0" + hour
##        if len(day) < 2:
##                day = "0" + day
##
##        anslag_file = open("anslagsfolder/" + year + "-" + month + "-" + day + " kl." + hour + "." + minute + ".txt", "w") 
##        anslag_content = request.forms.writtenPost
##        
##        """writes name, pic and content in file"""
##        anslag_file.write(username)
##        anslag_file.write("\n")
##        anslag_file.write(profile_pic)
##        anslag_file.write("\n")
##        anslag_file.write(anslag_content)
##        anslag_file.close()
##
##        return template("board", username=username, email=email, profile_pic=profile_pic)

@route("/board/")
def board():
        global username, email
        """Lists for all lines in anslag_file"""
        anslag_list = listdir("anslagsfolder")
        namn_list = []
        pict_list = []
        content_list = []
        time_list = []

        """prints anslag"""
        for anslag in reversed(anslag_list):
                f = codecs.open("user/" + email + ".txt", "r", "utf-8")
                text_file = f.readlines()
                try:
                    namn = text_file[0]
                except IndexError:
                    namn = "Namn saknas"

                try:
                    pict = text_file[1]
                except IndexError:
                    pict = "Bild saknas"

                try:
                    cont = text_file[2]
                except IndexError:
                    cont = "Content saknas"
                time_list.append(anslag)
                namn_list.append(namn)
                pict_list.append(pict)
                content_list.append(cont)

        return template("board", username=username, email=email, anslag_list=anslag_list, namn_list=namn_list, pict_list=pict_list, content_list=content_list, time_list=time_list)

        

##def anslag():
##        global username, email
##        """Lists for all lines in anslag_file"""
##        anslag_list = listdir("anslagsfolder")
##        namn_list = []
##        pict_list = []
##        content_list = []
##        time_list = []
##
##        """prints anslag"""
##        for anslag in anslag_list:
##                f = open("anslagsfolder/" + anslag, "r")
##                text_file = f.readlines()
##                namn = text_file[0]
##                pict = text_file[1]
##                cont = text_file[2]
##                time_list.append(anslag)
##                namn_list.append(namn)
##                pict_list.append(pict)
##                content_list.append(cont)



@route("/nabos/")
def nabolist():
	"""Appends usernames into name_list and prints it on the nabopage """
        global username, profile_pic
        
        user_list = listdir("user")
        name_list = []
        pic_list = []
        for user in user_list:
                f = codecs.open("user/" + email + ".txt", "r", "utf-8")
                text_file = f.readlines()
                firstname = text_file[0]
                surname = text_file[1]
                profile_pic = text_file[3]
                nabos = firstname + surname
                name_list.append(nabos)
                pic_list.append(profile_pic)

                        
	return template("nabos", user_list=user_list, name_list=name_list, username=username, profile_pic=profile_pic, pic_list=pic_list)


@route("/editProfile/")
def edit_profile():
	"""
	Edit your profile!
	"""
	global username, profile_pic, email
        
        f = codecs.open("user/" + email + ".txt", "r", "utf-8")
        text = f.readlines()
        firstname = text[0]
        lastname = text[1]
        pwd = text[2]
        pic = text[3]
        age_1 = text[6]
        streetname = text[4]
        town = text[5]
        appartment = text[7]
        mail = email
        tel = text[8]
        like = text[9]
        f.close()
	
	return template("editProfile", email=email, username=username, profile_pic=profile_pic, age=age, lgh=lgh, tel_nr=tel_nr, likes=likes, firstname=firstname, lastname=lastname, pwd=pwd, mail=mail, age_1=age_1, streetname=streetname, town=town, appartment=appartment, pic=pic, tel=tel, like=like)

@route("/editProfile/", method="POST")
def edit_prof():
	"""
	Edit your profile!
	"""
	global username, profile_pic, email, message
        contact = []
	name = request.forms.name
	surname = request.forms.surname
	street = request.forms.street
	city = request.forms.city
	email = request.forms.email
	pwd_1 = request.forms.pwd_1
	pwd_2 = request.forms.pwd_2
	old_pwd = request.forms.old_pwd
        profile_pic = request.forms.profile_pic
        """Age or birth date?"""
        age = request.forms.age
        lgh = request.forms.lgh
        tel_nr = request.forms.tel_nr
        """Likes in what form?"""
        likes = request.forms.likes

        f = codecs.open("user/" + email + ".txt", "r", "utf-8")
	text_file = f.readlines()
	old_pwd_2 = text_file[2].replace("\n", "")
	if old_pwd == old_pwd_2:
                if pwd_1 and pwd_2 is None:
                        
                        contact.extend((name, surname, old_pwd, profile_pic, street, city, age, lgh, tel_nr, likes))

                        text_file = codecs.open("user/" + email + ".txt", "w", "utf-8")
                                        
                        for i in contact:
                                text_file.write(i)
                                text_file.write("\n")
                        text_file.close()
                        message = "Din profil ar nu uppdaterad"
                        return template("updatedProfile", message=message, username=username, profile_pic=profile_pic, age=age, lgh=lgh, tel_nr=tel_nr, likes=likes ,name=name)

                if pwd_1 == pwd_2:
                        contact.extend((name, surname, pwd_1, profile_pic, street, city, age, lgh, tel_nr, likes))

                        text_file = codecs.open("user/" + email + ".txt", "w", "utf-8")
                                        
                        for i in contact:
                                text_file.write(i)
                                text_file.write("\n")
                        text_file.close()
                        message = "Din profil ar nu uppdaterad"
                        return template("updatedProfile", message=message, username=username, profile_pic=profile_pic, age=age, lgh=lgh, tel_nr=tel_nr, likes=likes ,name=name)

        else:
                message = "Du skrev fel password!"
                return template("updatedProfile", message=message, username=username, profile_pic=profile_pic)


@route("/updatedProfile/")
def upd_user():
	"""
	If wrong password in editUser
	"""
	global username, profile_pic, email, message
	
	message = message
	return template("updatedProfile", message=message, username=username, profile_pic=profile_pic)

@route("/registerProfileFail/")
def register_Profile_Fail():
	"""
	If wrong input in register user
	"""
	global message
	
	message = message
	return template("registerProfileFail", message=message)

@route("/loginProfileFail/")
def login_Profile_Fail():
	"""
	If wrong input in login user
	"""
	global message
	
	message = message
	return template("loginProfileFail", message=message)


@route("/otherUser/<pagename>")
def other_user(pagename):
	"""
	This shows another user.
	"""
	global username, email

        
##        f = open("user/" + email + ".txt", "r")
##	text_file = f.readlines()
	
	
	return template("otherUser", username=username)


@route("/inbox/")
def inbox():
	"""
	This is the mail inbox
	"""
	global username
	
	return template("inbox", username=username)

@route("/write/")
def about_us():
	"""
	This is the mail inbox
	"""
	global username
	
	return template("write", username=username)


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
