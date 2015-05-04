from os import listdir
from datetime import datetime

def create_anslag():
    """create anslag with date as filename"""
    #Raw input here must be replaced with POST-information
    name = raw_input("name: ")
    pic = raw_input("Picture URL: ")
    anslag_content = raw_input("Ditt meddelande: ")
    anslag_title = datetime.now()
    anslag_file = open("anslagsfolder/" + str(anslag_title.year) + "-" +
    str(anslag_title.month) + "-" + str(anslag_title.day) + " kl." +
    str(anslag_title.hour) + "." + str(anslag_title.minute) + ".txt", "w") 

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

    #prints anslag
    for anslag in anslag_list:
        f = open("anslagsfolder/" + anslag, "r")
        text_file = f.readlines()
        name = text_file[0]
        pic = text_file[1]
        content = text_file[2]
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

