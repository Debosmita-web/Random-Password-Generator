from tkinter import * 
import random, string
import pyperclip

root=Tk()#Tk() initialized tkinter which means window created
root.geometry("400x400")#geometry() set the width and height of the window
root.resizable(0,0)#resizable(0,0) set the fixed size of the window
root.title("DataFlair - PASSWORD GENERATOR")#title() set the title of the window

#Label() widget use to display one or more than one line of text that users can’t able to modify.
Label(root, text = 'PASSWORD GENERATOR' , font ='arial 15 bold').pack()
Label(root, text ='DataFlair', font ='arial 15 bold').pack(side = BOTTOM)
pass_label = Label(root, text = 'PASSWORD LENGTH', font = 'arial 10 bold').pack() 
pass_len = IntVar() #pass_len is an integer type variable that stores the length of a pass 
length = Spinbox(root, from_ = 8, to_ = 32 , textvariable = pass_len , width = 15).pack() #Spinbox() widget is used to select from a fixed number of values. Here the value from 8 to 32words.

#Function to generate password
pass_str = StringVar()
def Generator():
	password = ''
	for x in range (0,4):
		password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)
	for y in range(pass_len.get()- 4):
		password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
	pass_str.set(password)

	
Button(root, text = "GENERATE PASSWORD" , command = Generator ).pack(pady= 5) #Button() widget used to display button on our window
Entry(root , textvariable = pass_str).pack() #Entry() widget used to create an input text field

#Function to Copy Password
def Copy_password():
        pyperclip.copy(pass_str.get())

Button(root, text = 'COPY TO CLIPBOARD', command = Copy_password).pack(pady=5)
