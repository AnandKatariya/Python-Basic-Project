# Import required modules
from tkinter import *
import requests
from bs4 import BeautifulSoup



# user defined function
# to extract currency details
def getdata(url):
	r = requests.get(url)
	return r.text



# Function to compute and display currency details
def get_info():
	try:
		htmldata = getdata("https://finance.yahoo.com/quote/usdinr=X?ltr=1")
		soup = BeautifulSoup(htmldata, 'html.parser')
		mydatastr = ''
		for table in soup.find_all("div", class_="D(ib) Va(m) Maw(65%) Ov(h)"):
			mydatastr += table.get_text()
		list_data = mydatastr.split()
		temp = list_data[0].split("-")
		rate.set(temp[0])
		inc.set(temp[1])
		per_rate.set(list_data[1])
		time.set(list_data[3])
		result.set("success")
	except:
		result.set("Opps! something wrong")



# Driver Code	
# Create tkinter object
master = Tk()

# Set background color
master.configure(bg='light grey')

# Variable Classes in tkinter
result = StringVar()
rate = StringVar()
per_rate = StringVar()
time = StringVar()
inc = StringVar()

# Creating label for each information
Label(master, text="Status :", bg="light grey").grid(row=2, sticky=W)
Label(master, text="Current rate of INR :",
	bg="light grey").grid(row=3, sticky=W)
Label(master, text="Increase/decrease by :",
	bg="light grey").grid(row=4, sticky=W)
Label(master, text="Rate change :", bg="light grey").grid(row=5, sticky=W)
Label(master, text="Rate of time :", bg="light grey").grid(row=6, sticky=W)

# Creating label for class variable
Label(master, text="", textvariable=result,
	bg="light grey").grid(row=2, column=1, sticky=W)
Label(master, text="", textvariable=rate,
	bg="light grey").grid(row=3, column=1, sticky=W)
Label(master, text="", textvariable=inc, bg="light grey").grid(
	row=4, column=1, sticky=W)
Label(master, text="", textvariable=per_rate,
	bg="light grey").grid(row=5, column=1, sticky=W)
Label(master, text="", textvariable=time,
	bg="light grey").grid(row=6, column=1, sticky=W)

# Create submit button
b = Button(master, text="Show", command=get_info, bg="Blue").grid(row=0)

mainloop()
