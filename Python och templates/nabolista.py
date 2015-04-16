from bottle import *
from os import listdir

#Routen måste fixas till passande url
@route("/")
def nabolist():
    """Appends usernames into name_list and prints it on the nabopage """
    user_list = listdir("user")
    name_list = []
    
    for user in user_list:
        f = open("user/" + user, "r")
        text_file = f.readlines()
        firstname = text_file[0]
        surname = text_file[1]
        username = firstname + surname
        name_list.append(username)
    
    return template("nabos", user_list=user_list, name_list=name_list)

run(host="localhost", port=8080, debug=True)

    

    
    
