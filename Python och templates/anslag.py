from datetime import datetime

user = raw_input("user: ")
anslag = raw_input("anslag: ")
anslag_time = datetime.now()


print user, anslag, anslag_time.year, anslag_time.month, anslag_time.day
