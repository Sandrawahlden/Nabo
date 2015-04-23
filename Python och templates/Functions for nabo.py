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
        
	mail_doc = email + ".txt"
	f = open("user/" + email + ".txt", "r")
	
        if mail_doc == f:
            return "User already exist"
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

	return template("myProfile", title=email, text=contact, username=username)



@route("/editProfile/")
def edit_profile():
	"""
	This is the mail inbox
	"""
	global username
	
	return template("editProfile", username=username)
    

@route("/inbox/")
def inbox():
	"""
	This is the mail inbox
	"""
	global username
	
	return template("inbox", username=username)


@route("/write/")
def text_mail():
	"""
	This is where you write to other users
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




