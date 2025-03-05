from datetime import date
f = open("DailyNotes.txt", "a")
userNote = input("What would you like to note down today?\n");
f.write(str(date.today())+"\n")
f.write(userNote+"\n")


