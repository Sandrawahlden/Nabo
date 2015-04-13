def read_name():
    """
    list the sign in names
    """
    f = open("user/hannesdb@gmail.com.txt", "r")
    text_file = f.readlines()
    name = text_file[:2]
    f.close()
    
      
    print name

read_name()
