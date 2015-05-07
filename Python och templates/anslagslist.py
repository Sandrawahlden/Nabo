from os import listdir
from datetime import datetime

def create_anslag():
    """create anslag with date as filename"""
    #Raw input below must be replaced with POST-information
    name = raw_input("name: ")
    pic = raw_input("Picture URL: ")
    anslag_content = raw_input("Ditt meddelande: ")
    #Raw input above must be replaced with POST-information
    
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
    if len(day) < 2:
        day = "0" + day
    
    anslag_file = open("anslagsfolder/" + year + "-" + month + "-" + day + " kl." + hour + "." + minute + ".txt", "w") 

    """writes name, pic and content in file"""
    anslag_file.write(name)
    anslag_file.write("\n")
    anslag_file.write(pic)
    anslag_file.write("\n")
    anslag_file.write(anslag_content)
    anslag_file.close()

def show_anslag():
    """Lists for all lines in anslag_file"""
    anslag_list = listdir("anslagsfolder")
    name_list = []
    pic_list = []
    content_list = []
    time_list = []

    """prints anslag"""
    for anslag in anslag_list:
        f = open("anslagsfolder/" + anslag, "r")
        text_file = f.readlines()
        try:
            name = text_file[0]
        except IndexError:
            name = "Namn saknas"

        try:
            pic = text_file[1]
        except IndexError:
            pic = "Bild saknas"

        try:
            content = text_file[2]
        except IndexError:
            content = "Content saknas"
        time_list.append(anslag)
        name_list.append(name)
        pic_list.append(pic)
        content_list.append(content)
        
    
    for name, pic, content, time in zip(name_list, pic_list, content_list, time_list):
        print "Skrivet av:",name
        print "Bild:",pic
        print "Uppladdat:",time[:-4]
        print "Anslag:",content
        print "\n"

show_anslag()
create_anslag()

