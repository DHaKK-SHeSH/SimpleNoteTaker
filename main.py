from datetime import date
def dateSearch(file,dateString):
    for line in open(file, "r"):
        if dateString in line:
            return True

fileName = "DailyNotes.txt"
fWriter = open(fileName, "a")
userNote = input("What would you like to note down today?\n");
dateToday = str(date.today())
if not dateSearch(fileName,dateToday):
    fWriter.write(dateToday + "\n")
fWriter.write(userNote+"\n")
fReader = open(fileName, "r")
notes = fReader.read()
print(notes)



