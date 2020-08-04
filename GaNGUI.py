##############################################
## Globe at Night Graphical Interface
## Sophie McGrady
##############################################

from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox 

root = Tk()
root.title("Globe at Night")
canvas = Canvas(root, width = 950, height = 600)
canvas.pack()

def generalInformation():
    #prints information at the top of the screen so users know how to use the interface
    fontSize = "15"
    fontType = "Times "
    canvas.create_text(475, 15, text = "Welcome to the Globe at Night Campaign!",
                        font = fontType + "18 bold underline")
    canvas.create_text(10, 40, anchor = "nw", text = "Please enter the information below to update activity guides.",
                        font = fontType + fontSize)
    canvas.create_text(10, 80, anchor = "nw", text = "Complete all areas, even if some information is not being updated.",
                        font = fontType + fontSize)
    canvas.create_text(10, 120, anchor = "nw", text = "When you have finished, press the OK button.",
                        font = fontType + fontSize)
    canvas.create_text(10, 160, anchor = "nw", text = "Thank you for your help in protecting dark skies!",
                        font = fontType + fontSize)
    canvas.create_text(475, 240, text = "--" * 65,
                        font = fontType + fontSize)

def darkSkyImage():
    #used information from https://pythonbasics.org/tkinter-image/ to upload an image
    img = Image.open("globeAtNightLogo.png")
    scaled = img.resize((240, 180), Image.ANTIALIAS)
    render = ImageTk.PhotoImage(scaled)
    finalImg = Label(image = render)
    finalImg.image = render
    finalImg.place(x = 705, y = 5)

def yearTextBox():
    #allows the user to update the year
    fontSize = "14"
    fontType = "Times "
    canvas.create_text(10, 290, text = "Year:", anchor = "nw",
                        font = fontType + fontSize)
    global year
    year = Entry(root)
    year.place(x = 55, y = 290)

def northConstellationTextBox():
    #allows the user to update the northern constellation
    fontSize = "14"
    fontType = "Times "
    canvas.create_text(10, 320, text = "Northern Constellation:", anchor = "nw",
                        font = fontType + fontSize)
    global northCon
    northCon = Entry(root)
    northCon.place(x = 185, y = 320)

def southConstellationTextBox():
    #allows the user to update the southern constellation
    fontSize = "14"
    fontType = "Times "
    canvas.create_text(10, 350, text = "Southern Constellation:", anchor = "nw",
                        font = fontType + fontSize)
    global southCon
    southCon = Entry(root)
    southCon.place(x = 185, y = 350)

def northConstellationDates():
    #allows the user to update the north constellation dates
    fontSize = "14"
    fontType = "Times "
    canvas.create_text(10, 440, text = "North Dates (Format: Month ## - ## and Month ## - ##):", anchor = "nw",
                        font = fontType + fontSize)
    global northDates
    northDates = Entry(root)
    northDates.place(x = 445, y = 440, width = 250)

def southConstellationDates():
    #allows the user to update the south constellation dates
    fontSize = "14"
    fontType = "Times "
    canvas.create_text(10, 470, text = "South Dates (Format: Month ## - ## and Month ## - ##):", anchor = "nw",
                        font = fontType + fontSize)
    global southDates
    southDates = Entry(root)
    southDates.place(x = 445, y = 470, width = 250)

def picture1():
    #allows the user to update the first picture
    fontSize = "14"
    fontType = "Times "
    canvas.create_text(10, 380, text = "Picture 1 (Format: fileName.fileType):", anchor = "nw",
                        font = fontType + fontSize)
    global picture1
    picture1 = Entry(root)
    picture1.place(x = 295, y = 380, width = 200)

def picture2():
    #allows the user to update the second picture
    fontSize = "14"
    fontType = "Times "
    canvas.create_text(10, 410, text = "Picture 2 (Format: fileName.fileType):", anchor = "nw",
                        font = fontType + fontSize)
    global picture2
    picture2 = Entry(root)
    picture2.place(x = 295, y = 410, width = 200)

def okayButton():
    #closes the window and prints all entered information
    okay = Button(text = "OK", command = presentEnteredInfo, bg = "green")
    okay.place(x = 880, y = 570, width = 60)

def presentEnteredInfo():
    #executed when button is clicked 
    #https://www.codespeedy.com/create-a-popup-window-in-tkinter-python/ info about
    #popup windows found here
    if (year.get() == "" or northCon.get == "" or southCon.get() == "" or northDates.get() == "" or
        southDates.get() == "" or picture1.get() == "" or picture2.get() == "get"):
        tkinter.messagebox.showinfo("Error", "Please complete all areas before pressing OK. Thank you!")
    elif year.get() != "":
        #checks for user error for the year
        try:
            int(year.get())
            if int(year.get()) >= 2020 and int(year.get()) <= 3000:
                print(year.get())
                print(northCon.get())
                print(southCon.get())
                print(northDates.get())
                print(southDates.get())
                print(picture1.get())
                print(picture2.get())
                root.destroy()
                print("******Thank you for the information! Activity guides should be updating******")
            else:
                tkinter.messagebox.showinfo("Error", "Please enter a valid year. Thank you!")
        except:
            tkinter.messagebox.showinfo("Error", "Please enter a valid year. Thank you!")

def main():
    #runs all the main functions
    generalInformation()
    darkSkyImage()
    yearTextBox()
    northConstellationTextBox()
    southConstellationTextBox()
    northConstellationDates()
    southConstellationDates()
    picture1()
    picture2()
    okayButton()


main()
root.mainloop()