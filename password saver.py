from tkinter import *
from functools import partial

def valid(first_name,last_name,email, password):
	print("first_name entered :", first_name.get())
	print("last_name entered :", last_name.get())
	print("email entered :", email.get())
	print("password entered :", password.get())
	return

#window
tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('Password-Saver Form')

#username label and text entry box
first_nameLabel = Label(tkWindow, text="First Name").grid(row=0, column=0)
first_name = StringVar()
first_nameEntry = Entry(tkWindow, textvariable=first_name).grid(row=0, column=1)  

last_nameLabel = Label(tkWindow, text="Last Name").grid(row=1, column=0)
last_name = StringVar()
last_nameEntry = Entry(tkWindow, textvariable=last_name).grid(row=1, column=1)  

#email label and email entry box
emailLabel = Label(tkWindow,text="Email").grid(row=2, column=0)  
email = StringVar()
emailEntry = Entry(tkWindow, textvariable=email, show='*').grid(row=2, column=1)  

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=3, column=0)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=3, column=1)  


validateLogin = partial(valid, first_name,last_name,email, password)

loginButton = Button(tkWindow, text="Submit", command=valid).grid(row=6, column=0)  

tkWindow.mainloop()
