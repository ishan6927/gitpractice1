import tkinter as tk
from tkinter import *
r = tk.Tk()
r.title('Counting Seconds')

r.config(padx=50, pady=50)

# website_label = r.Label(text="website:")
# website_label.grid(row=1, column=0)

# master = Tk()

Label(r, text='First Name').grid(row=0,column=2)
Label(r, text='Last Name').grid(row=1, column=2)

button = tk.Button(r, text='Stop', width=25, command=r.destroy).grid(row=2)

var1 = IntVar()
Checkbutton(r, text='male', variable=var1).grid(row=3, sticky=W)
var2 = IntVar()
Checkbutton(r, text='female', variable=var2).grid(row=4, sticky=W)

e1 = Entry(r)
e2 = Entry(r)
e1.grid(row=0, column=2)
e2.grid(row=1, column=2)

# window = Tk()
# window.title("Password Manager")
#
frame = Frame(r)
frame.grid(row=5, column=0)
bottomframe = Frame(r)
bottomframe.grid(row=5, column=1)
redbutton = Button(frame, text='Red', fg ='red')
redbutton.grid(row=5, column=2)
greenbutton = Button(frame, text = 'Brown', fg='brown')
greenbutton.grid(row=5, column=3)
bluebutton = Button(frame, text ='Blue', fg ='blue')
bluebutton.grid(row=5, column=4)
blackbutton = Button(bottomframe, text='Black', fg='black')
blackbutton.grid(row=5, column=5)




Lb = Listbox(r)
Lb.insert(1, 'Python')
Lb.insert(2, 'Java')
Lb.insert(3, 'C++')
Lb.insert(4, 'Any other')
Lb.grid(row=0, column=0)


menu = Menu(r)
r.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=r.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')


w = Scale(r, from_=0, to=42)
w.grid()
w = Scale(r, from_=0, to=200, orient=HORIZONTAL)
w.grid()



w = Spinbox(r, from_ = 0, to = 100)
w.grid()

r.mainloop()




















# from tkinter import *
# from tkinter import PhotoImage ,Label
#

# canvas = Canvas(height=200, width=200)
# logo_img = PhotoImage(file="logo.png")



# # logo_img = PIL.Image.open(file="logo.png")
# canvas.create_image(100, 100, image=logo_img)
# canvas.grid(row=0, coloumn=1)

# email_label = Tk.Label(text="Email/Username")
# email_label.Tk.grid(row=2, column=0)
# password_label = Tk.Label(text="password")
# password_label.Tk.grid(row=3, coloumn=0)

# Enteries

# website_entry = tkinter.Entry(width=35)
# email_entry = tkinter.Entry(width=35)
# password_entry = tkinter.Entry(width=21)


#button

# generate_passowrd_botton = tkinter.Button(test="Text Generator")
# generate_passowrd_botton.grid(row=3, coloumn=2)
# add_button = tkinter.Button(text="Add", width=36)
# add_button.grid(row=4, column=1, columnspan=2)

# window.mainloop()
