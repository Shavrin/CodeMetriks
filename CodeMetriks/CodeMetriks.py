from appJar import gui
import string
import os

def press(button):
    global path
    global extensions
    if button == "Cancel":
        app.stop()
    if button == "Calculate!":
        path = app.getEntry("PATH")
        extensions = app.getEntry("extensions")

        app.stop()



path = ""
extensions = ""


app = gui("CodeMetriks","400x200")
app.addLabel("title","Select a directory to run CodeMetriks on:")
app.setFont(15)
app.setLabelBg("title","green")

app.addLabelEntry("PATH")
app.setEntryDefault("PATH",os.getcwd())
app.setEntry("PATH",os.getcwd() + '\\',callFunction=False)
app.addButtons(["Calculate!","Cancel"],press)

app.addLabelEntry("extensions")
app.setEntryDefault("extensions",'py,cpp')
app.setEntry("extensions",'py',callFunction=False)

app.go()


fileList = os.listdir()
for fileName in fileList:
    splittedFile = fileName.split('.')
    exts = extensions.split(",")
    numberOfExtensions = len(exts)
    for ext in exts:
        if splittedFile[len(splittedFile) - 1] == ext:
            print(fileName)
            file = open(path + fileName,'r')
            lines = len(file.readlines())
            file.seek(0)
            characters = len(file.read())
            file.close()
            print("Number of lines: " , lines)
            print(lines)
            print("Number of characters: " , characters)
            print(characters)



