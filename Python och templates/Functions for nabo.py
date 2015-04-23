@route("/myProfile/")
def register_user():
	"""Register user and saves the name, surename, adress, email and
	password in a document"""
	global username, email, profile_pic

	user = username.replace("\n", " ")
        first = user.split(" ")
        firstname = first[0]
        profile_pic = text_file[4]

	return template("myProfile", username=username, firstname=firstname, profile_pic=profile_pic)  
