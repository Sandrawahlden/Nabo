def test():
  pwd_1 = "då"

  f = open("user/testmail.txt", "r")
  text_file = f.readlines()
  pwd_2 = text_file[3]
  f.close()

  print pwd_2

test()
