# encoding: utf-8
# Author: <Andre, Hannes>
 
from bottle import *
from os import listdir
from datetime import datetime
import codecs

username = ""
email = ""
age = ""
lgh = ""
tel_nr = ""
likes = ""
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
message = ""
link = ""
link_name = ""


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
        profile_pic = "/static/Bilder/avatar.png"
	if pwd_1 == pwd_2:
                contact.extend((name, surname, pwd_1, profile_pic, street, city, "-", "-", "-", "-"))

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

                        anslag_title = datetime.now()
                        year = str(anslag_title.year)
                        month = str(anslag_title.month)
                        day = str(anslag_title.day)
                        hour = str(anslag_title.hour)
                        minute = str(anslag_title.minute)
                        if len(month) < 2:
                                month = "0" + month
                        if len(day) < 2:
                                day = "0" + day
                        if len(hour) < 2:
                                hour = "0" + hour
                        if len(minute) < 2:
                                minute = "0" + minute

                        anslag_file = codecs.open("anslagsfolder/" + year + "-" + month + "-" + day + " kl." + hour + "." + minute + ".txt", "w", "utf-8") 
                        anslag_content = request.forms.writtenPost
                        
                        """writes name, pic and content in file"""
                        anslag_file.write(username)
                        anslag_file.write("\n")
                        anslag_file.write("/static/Bilder/avatar.png")
                        anslag_file.write("\n")
                        anslag_file.write(" ")
                        anslag_file.write("\n")
                        anslag_file.write("Har flyttat in!")
                        anslag_file.close()
                        
                        return template("myProfile", title=email, text=contact, firstname=firstname, username=username, pwd_1=pwd_1, pwd_2=pwd_2, profile_pic=profile_pic, lastname=lastname, age_1=age_1, streetname=streetname, town=town, appartment=appartment, tel=tel, like=like)
                
        else:
                message = "Lösenorden matchar inte!"
                return template("registerProfileFail", message=message)
  
  
@route("/", method="POST")
def sign_in():
	"""Signing in existing user and goes to home"""
	global username, email, message

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
                        profile_pic = text_file[3]
                        username = firstname + surname
                        f.close()
                        
                        anslag_list = listdir("anslagsfolder")
                        namn_list = []
                        pict_list = []
                        content_list = []
                        time_list = []

                        """prints anslag"""
                        for anslag in reversed(anslag_list):
                                f = codecs.open("anslagsfolder/" + anslag, "r", "utf-8")
                                text_file = f.readlines()
                                try:
                                    firstnamn = text_file[0].replace("\n", " ")
                                    eftnamn = text_file[1].replace("\n", "")
                                    namn = firstnamn + eftnamn
                                except IndexError:
                                    namn = "Namn saknas"

                                try:
                                    pict = text_file[3]
                                except IndexError:
                                    pict = "Bild saknas"

                                try:
                                    cont = text_file[5]
                                except IndexError:
                                    cont = "Innehåll saknas"

                                time_list.append(anslag)
                                namn_list.append(namn)
                                pict_list.append(pict)
                                content_list.append(cont)
                        return template("home", username=username, email=email, profile_pic=profile_pic, anslag_list=anslag_list, namn_list=namn_list, pict_list=pict_list, content_list=content_list, time_list=time_list)
                else:
                        
                        message = "Fel lösenord!"
                        return template("loginProfileFail", message=message)

        else:
                message = "Epostadressen finns inte registrerad!"
                return template("loginProfileFail", message=message)
	

@route("/myProfile/")
def user_profile():
	"""Shows the userprofile"""
	global username, email

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

@route("/home/", method="POST")
def post_anslag():
        global username, email, message


        o = codecs.open("user/" + email + ".txt", "r", "utf-8")
        txt = o.readlines()
        profile_pic = txt[3]
        o.close()
        
        
        anslag_title = datetime.now()
        year = str(anslag_title.year)
        month = str(anslag_title.month)
        day = str(anslag_title.day)
        hour = str(anslag_title.hour)
        minute = str(anslag_title.minute)
        if len(month) < 2:
                month = "0" + month
        if len(day) < 2:
                day = "0" + day
        if len(hour) < 2:
                hour = "0" + hour
        if len(minute) < 2:
                minute = "0" + minute

        anslag_file = codecs.open("anslagsfolder/" + year + "-" + month + "-" + day + " kl." + hour + "." + minute + ".txt", "w", "utf-8") 
        anslag_content = request.forms.writtenPost
        
        """writes name, pic and content in file"""
        anslag_file.write(username)
        anslag_file.write("\n")
        anslag_file.write(profile_pic)
        anslag_file.write("\n")
        anslag_file.write(anslag_content)
        anslag_file.close()


        """prints anslag"""
        anslag_list = listdir("anslagsfolder")
        namn_list = []
        pict_list = []
        content_list = []
        time_list = []
        for anslag in reversed(anslag_list):
                f = codecs.open("anslagsfolder/" + anslag, "r", "utf-8")
                text_file = f.readlines()
                try:
                    firstnamn = text_file[0].replace("\n", " ")
                    eftnamn = text_file[1].replace("\n", "")
                    namn = firstnamn + eftnamn
                except IndexError:
                    namn = "Namn saknas"

                try:
                    pict = text_file[3]
                except IndexError:
                    pict = "Bild saknas"

                try:
                    cont = text_file[5]
                except IndexError:
                    cont = "Innehåll saknas"

                
                time_list.append(anslag)
                namn_list.append(namn)
                pict_list.append(pict)
                content_list.append(cont)
                return template("home", username=username, email=email, profile_pic=profile_pic, anslag_list=anslag_list, namn_list=namn_list, pict_list=pict_list, content_list=content_list, time_list=time_list)
                

@route("/home/")
def home():
        global username, email
        """Lists for all lines in anslag_file"""

        o = codecs.open("user/" + email + ".txt", "r", "utf-8")
        txt = o.readlines()
        profile_pic = txt[3]
        o.close()
        
        anslag_list = listdir("anslagsfolder")
        namn_list = []
        pict_list = []
        content_list = []
        time_list = []
        

        """prints anslag"""
        for anslag in reversed(anslag_list):
                f = codecs.open("anslagsfolder/" + anslag, "r", "utf-8")
                text_file = f.readlines()
                try:
                    firstnamn = text_file[0].replace("\n", " ")
                    eftnamn = text_file[1].replace("\n", "")
                    namn = firstnamn + eftnamn
                except IndexError:
                    namn = "Namn saknas"

                try:
                    pict = text_file[3]
                except IndexError:
                    pict = "Bild saknas"

                try:
                    cont = text_file[5]
                except IndexError:
                    cont = "Innehåll saknas"

        
                time_list.append(anslag)
                namn_list.append(namn)
                pict_list.append(pict)
                content_list.append(cont)
        return template("home", username=username, email=email, profile_pic=profile_pic, anslag_list=anslag_list, namn_list=namn_list, pict_list=pict_list, content_list=content_list, time_list=time_list)


@route("/nabos/")
def nabolist():
	"""Appends usernames into name_list and prints it on the nabopage """
        global username
        
        user_list = listdir("user")
        name_list = []
        pic_list = []
        for user in user_list:
                f = codecs.open("user/" + user, "r", "utf-8")
                text_file = f.readlines()
                firstname = text_file[0]
                surname = text_file[1]
                profile_pic = text_file[3]
                nabos = firstname + surname
                name_list.append(nabos)
                pic_list.append(profile_pic)

                        
	return template("nabos", user=user, user_list=user_list, name_list=name_list, username=username, profile_pic=profile_pic, pic_list=pic_list)


@route("/editProfile/")
def edit_profile():
	"""
	Edit your profile!
	"""
	global username, email
        
        f = codecs.open("user/" + email + ".txt", "r", "utf-8")
        text = f.readlines()
        firstname = text[0]
        lastname = text[1]
        pwd = text[2]
        pic = text[3]
        profile_pic = text[3]
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
	global username, email, message, link
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
                while len(pwd_1) < 2:
                        
                        contact.extend((name, surname, old_pwd, profile_pic, street, city, age, lgh, tel_nr, likes))

                        text_file = codecs.open("user/" + email + ".txt", "w", "utf-8")
                                        
                        for i in contact:
                                text_file.write(i)
                                text_file.write("\n")
                        text_file.close()
                        link_name = "Min profil"
                        link = "/myProfile/"
                        message = "Din profil är nu uppdaterad"
                        return template("updatedProfile", link_name=link_name, message=message, username=username, profile_pic=profile_pic, age=age, lgh=lgh, tel_nr=tel_nr, likes=likes ,name=name)
                
                
                if pwd_1 == pwd_2:
                        contact.extend((name, surname, pwd_1, profile_pic, street, city, age, lgh, tel_nr, likes))

                        text_file = codecs.open("user/" + email + ".txt", "w", "utf-8")
                                        
                        for i in contact:
                                text_file.write(i)
                                text_file.write("\n")
                        text_file.close()

                        link_name = "Min profil"
                        link = "/myProfile/"
                        message = "Din profil är nu uppdaterad"
                        return template("updatedProfile", link_name=link_name, link=link, message=message, username=username, profile_pic=profile_pic, age=age, lgh=lgh, tel_nr=tel_nr, likes=likes ,name=name)
                else:
                        link_name = "Redigera profil"
                        link = "/editProfile/"
                        message = "Lösenorden du skrev matchar inte!"
                        return template("updatedProfile", link_name=link_name, link=link, message=message, username=username, profile_pic=profile_pic)

        else:
                link_name = "Redigera profil"
                link = "/editProfile/"
                message = "Du skrev fel lösenord!"
                return template("updatedProfile", link_name=link_name, link=link, message=message, username=username, profile_pic=profile_pic)


@route("/updatedProfile/")
def upd_user():
	"""
	If wrong password in editUser
	"""
	global username, email, message, link

	o = codecs.open("user/" + email + ".txt", "r", "utf-8")
        txt = o.readlines()
        profile_pic = txt[3]
        o.close()

        link_name = link_name
	link = link
	message = message
	return template("updatedProfile", link_name=link_name, link=link, message=message, username=username, profile_pic=profile_pic)

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
        
        f = codecs.open("user/" + pagename, "r", "utf-8")
	text = f.readlines()
	prof_pic = text[3]
	profile_pic = text[3]
        first = text[0]
        last = text[1]
        age_2 = text[6]
        apa = text[7]
        tele = text[8]
        likees = text[9]
        f.close()
	
	return template("otherUser", username=username, name=pagename, text=text, first=first, last=last, prof_pic=prof_pic, age_2=age_2, apa=apa, tele=tele, likees=likees)


@route("/inbox/")
def inbox():
	"""
	This is the mail inbox
	"""
	global username
	
	
	return template("inbox", username=username)

@route("/write/")
def write_message():
	"""
	This is the write message function
	"""
        #!!!!NEEDS TO BE FIXED/ADJUSTED WHEN HTML IS IN PLACE!!!!

        global username

        user_list = listdir("user")
        name_list = []
        pic_list = []
        for user in user_list:
                f = codecs.open("user/" + user, "r", "utf-8")
                text_file = f.readlines()
                firstname = text_file[0]
                surname = text_file[1]
                profile_pic = text_file[3]
                nabos = firstname + surname
                name_list.append(nabos)
                pic_list.append(profile_pic)

                        
	return template("write", user=user, user_list=user_list, name_list=name_list, username=username, profile_pic=profile_pic, pic_list=pic_list)


@route("/messageView/")
def message():
	"""
	This is the nabo help.
	"""
	global username
	
	return template("messageView", username=username)


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
