from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
def searchfunc():
    pass
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generatepass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    passw = ""
    for char in password_list:
        passw += char
    password.insert(END,passw)
    pyperclip.copy(passw)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    webdata=website.get()
    emaildata=email.get()
    passworddata=password.get()
   
    new_data = {
        webdata: {
            "email": emaildata,
            "password": passworddata,
        }
    }

    if len(webdata) == 0 or len(passworddata) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("day29\data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("day29\data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("day29\data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website.delete(0, END)
def find_password():
    websitedat = website.get()
    try:
        with open("day29\data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if websitedat in data:
            email = data[websitedat]["email"]
            password = data[websitedat]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")       
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas=Canvas(width=200,height=200)
lock_img=PhotoImage(file="D:\code\python\\100 days of python\day29\logo.png")
canvas.create_image(100,100,image=lock_img)
canvas.grid(column=1,row=0)

websitetext=Label(text="Website:")
websitetext.grid(column=0,row=1)
website=Entry(width=21)
website.focus()
website.grid(column=1,row=1,sticky=(W))

emailtext=Label(text="Email/Username:")
emailtext.grid(column=0,row=2)
email=Entry(width=35)
email.insert(END,string="example@gmail.com")
email.grid(column=1,row=2,sticky=(W),columnspan=2)

passwordtext=Label(text="Password:")
passwordtext.grid(column=0,row=3)
password=Entry(width=21)
password.grid(column=1,row=3,sticky=(W))

search=Button(text="Search",command=find_password)
search.grid(column=2,row=1,sticky=(W))

generate=Button(text="Generate Password",command=generatepass)
generate.grid(column=1,row=3,sticky=(E))

add=Button(text="Add",width=35,command=save)
add.grid(column=1,row=4,sticky=(W),columnspan=2)

window.mainloop()