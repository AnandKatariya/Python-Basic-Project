# Import required modules
from tkinter import *
import rotatescreen


# User defined function
# for rotating screen
def Screen_rotation(temp):
	screen = rotatescreen.get_primary_display()
	if temp == "up":
		screen.set_landscape()
	elif temp == "right":
		screen.set_portrait_flipped()
	elif temp == "down":
		screen.set_landscape_flipped()
	elif temp == "left":
		screen.set_portrait()


# Creating tkinter object
master = Tk()
master.geometry("100x100")
master.title("Screen Rotation")
master.configure(bg='light grey')


# Variable classes in tkinter
result = StringVar()


# Creating buttons to change orientation
Button(master, text="Up", command=lambda: Screen_rotation(
	"up"), bg="white").grid(row=0, column=3)
Button(master, text="Right", command=lambda: Screen_rotation(
	"right"), bg="white").grid(row=1, column=6)
Button(master, text="Left", command=lambda: Screen_rotation(
	"left"), bg="white").grid(row=1, column=2)
Button(master, text="Down", command=lambda: Screen_rotation(
	"down"), bg="white").grid(row=3, column=3)


mainloop()
