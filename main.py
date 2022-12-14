from tkinter import *
from tkinter import ttk
import os
import getpass

def top_bar(frame):
    header_frame = Frame(frame, background='#E4DDF4', highlightbackground="black", highlightthickness=1)
    header_frame.place(in_=frame, width=1280, height=50)

    menuLabel = ttk.Label(header_frame, text="Flashcards for Free", background='#E4DDF4', font=('Inter', '15'))
    homeButton = ttk.Button(header_frame, text='Home', command=home_screen)
    createButton = ttk.Button(header_frame, text='Create', comman=create_screen)
    logoutButton = ttk.Button(header_frame, text='Logout', command=login_screen)

    menuLabel.place(in_=header_frame, relx=0.02, rely=0.25, width=210, height=25)
    homeButton.place(in_=header_frame, relx=0.15, rely=0.25, width=75, height=25)
    createButton.place(in_=header_frame, relx=0.23, rely=0.25,width=80, height=25)
    logoutButton.place(in_=header_frame, relx=0.92, rely=0.25, width=80, height=25)

def get_user_loop():
    with open('workinguser.txt', 'r') as file:
        lines = file.readlines()
        welcomeLabel.config(text='Welcome, {}'.format(lines[0]))
    root.after(500, get_user_loop)

def get_folder():
    with open('workinguser.txt', 'r') as file:
        lines = file.readlines()
        fileLocation = lines[1].split('\n')
    return fileLocation[0]

def set_buttons_loop():
    fileLocation = get_folder()
    tempFiles = os.listdir(fileLocation)
    files = ['','','','','','']
    
    for i in range(len(tempFiles)-1):
        if tempFiles[i] == ('.DS_Store'):
            tempFiles.remove('.DS_Store')
    for i in range(0,len(tempFiles)):
        files[i] = tempFiles[i].strip('.txt')
    files.sort()

    set1 = ttk.Button(home_frame, text=files[0])
    set2 = ttk.Button(home_frame, text=files[1])
    set3 = ttk.Button(home_frame, text=files[2])
    set4 = ttk.Button(home_frame, text=files[3])
    set5 = ttk.Button(home_frame, text=files[4])
    set6 = ttk.Button(home_frame, text=files[5])

    set1.place(relx=0.2, rely=0.3, width=250, height=120)
    set2.place(relx=0.45, rely=0.3, width=250, height=120)
    set3.place(relx=0.7, rely=0.3, width=250, height=120)
    set4.place(relx=0.2, rely=0.55, width=250, height=120)
    set5.place(relx=0.45, rely=0.55, width=250, height=120)
    set6.place(relx=0.7, rely=0.55, width=250, height=120)
    root.after(1000, set_buttons_loop)

def login_user():
    #Without this if-statement, the blank input is captured and goes to the second frame
    uInput = loginString.get()
    if uInput == '':
        return loginString.get()
    with open('username.txt', 'r') as searchUsername:
        textFileSearch = searchUsername.readlines()
        for row in textFileSearch:
            findUserName = row.find(uInput)
            if findUserName == 0:
                raise_frame(home_frame)
                break
        else:
            print('Your username does not exist')
            return
    with open('workinguser.txt', 'w') as workingUser:
        workingUser.write(uInput + '\n')
        workingUser.write(r'/Users/' + getpass.getuser() + r'/Documents/Flashcards Program/Users/' + uInput + '\n')

def create_user():
    uInput = createString.get()
    if uInput == '':
        return
    with open('username.txt', 'a') as userFile:
        userFile.write(uInput + '\n')
    os.makedirs(r'/Users/' + getpass.getuser() + r'/Documents/Flashcards Program/Users/' + uInput)

def create_set():
    setName = setNameEntry.get()
    if setName == '':
        return
    filepath = r'/Users/' + getpass.getuser() + r'/Documents/Flashcards Program/Users/' + loginString.get() + r'/' + setName + r'.txt'
    with open(filepath, 'a') as newSet:
        print('success')

def raise_frame(frame):
    frame.tkraise()

def login_screen():
    usernameEntry.delete(0, END)
    raise_frame(gray_background)
    raise_frame(login_frame)

def home_screen():
    raise_frame(home_frame)
    top_bar(home_frame)

def create_screen():
    raise_frame(create_set_frame)
    top_bar(create_set_frame)

def create_user_frame():
    raise_frame(gray_background)
    raise_frame(create_frame)

root = Tk()
root.title("FLASHCARDS PROGRAM")
root.geometry("1280x720")

style = ttk.Style()
style.theme_use('default')

#Gray Background
gray_background = Frame(root, background='#939393')
gray_background.place(relx=0, rely=0, width=10000, height=10000)

#Login Frame
login_frame = Frame(root, background = '#BACDAF', highlightbackground="black", highlightthickness=1)
login_frame.place(relx=0.5, rely=0.5, width=575, height=260, anchor=CENTER)
login_top_frame = Frame(login_frame, background='#468D70')
login_top_frame.place(in_=login_frame, width=573, height=75)

loginHeader = ttk.Label(login_top_frame, text = "Flashcards For Free", background = '#468D70', font=('Inter','28','bold'))
usernameLabel = ttk.Label(login_frame, text = "Username:", font=('Inter', '15'), background='#BACDAF')
loginString = StringVar()
usernameEntry = ttk.Entry(login_frame, width=10, textvariable=loginString, background='green')
loginButton = ttk.Button(login_frame, text="LOGIN", width = 8,  command=login_user)
createAccount = ttk.Button(login_frame, text="No Account? Click Here", command=create_user_frame)

loginHeader.place(in_=login_top_frame, relx=0.05, rely=0.25)
usernameLabel.place(in_=login_frame, relx=0.05, rely=0.35)
usernameEntry.place(in_=login_frame, height=35, relx=0.05, rely=0.45)
loginButton.place(in_=login_frame, relx=0.05, rely=0.6)
createAccount.place(in_=login_frame, relx=0.35, rely=0.85)

#Create Frame
create_frame = Frame(root, background = '#BACDAF', highlightbackground="black", highlightthickness=1)
create_frame.place(relx=0.5, rely=0.5, width=575, height=260, anchor=CENTER)
create_top_frame = Frame(create_frame, background='#468D70')
create_top_frame.place(in_=create_frame, width=573, height=75)

createHeader = ttk.Label(create_top_frame, text = "Flashcards For Free", background = '#468D70', font=('Inter','28','bold'))
newUserLabel = ttk.Label(create_frame, text = "Create a username:", font=('Inter', '15'), background='#BACDAF')
createString = StringVar()
createEntry = ttk.Entry(create_frame, width=10, textvariable=createString, background='green')
createButton = ttk.Button(create_frame, text="CREATE ACCOUNT", command=create_user)
createAccount = ttk.Button(create_frame, text="Have an account? Click Here", command=login_screen)

createHeader.place(in_=create_top_frame, relx=0.05, rely=0.25)
newUserLabel.place(in_=create_frame, relx=0.05, rely=0.35)
createEntry.place(in_=create_frame, height=35, relx=0.05, rely=0.45)
createButton.place(in_=create_frame, relx=0.05, rely=0.6)
createAccount.place(in_=create_frame, relx=0.35, rely=0.85)

#Home Frame Widget
home_frame = Frame(root, width=1280, height=720, background='#EAE2E2')
home_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
top_bar(home_frame)

welcomeLabel = ttk.Label(home_frame, background='#EAE2E2', font=('Inter', '20'))
setsLabel = ttk.Label(home_frame, text="Flashcard Sets", background='#EAE2E2', font='Inter, 20')
viewAllSets = ttk.Button(home_frame, text='View All')
welcomeLabel.place(relx=0.5, rely=0.15, anchor=CENTER)
setsLabel.place(relx=0.25, rely=0.25, anchor=CENTER)
viewAllSets.place(relx=0.832, rely=0.75, width=80, height=25)

#Create Frame
create_set_frame = Frame(root, width=1280, height=720, background='#EAE2E2')
create_set_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
top_bar(create_set_frame)

set_display_frame = Frame(create_set_frame, width=600, height=300, background='#D9D9D9', highlightbackground="black", highlightthickness=1)
set_display_frame.place(in_=create_set_frame, relx=0.5, rely=0.6, anchor=CENTER)

createSetLabel = ttk.Label(create_set_frame, text='Create Set', background='#EAE2E2', font='Inter, 21')
setNameLabel = ttk.Label(create_set_frame, text='Set Name', background='#EAE2E2', font='Inter, 17')
termLabel = ttk.Label(create_set_frame, text='Term', background='#EAE2E2', font='Inter, 17')
definitionLabel = ttk.Label(create_set_frame, text='Definition', background='#EAE2E2', font='Inter, 17')
addTermDefButton = ttk.Button(create_set_frame, text='Add Term/Definition Pair', command=create_set)
setNameVar = StringVar()
termVar = StringVar()
definitionVar = StringVar()
setNameEntry = ttk.Entry(create_set_frame, textvariable=setNameVar)
termInput = ttk.Entry(create_set_frame, textvariable= termVar)
definitionInput = ttk.Entry(create_set_frame, textvariable=definitionVar)

createSetLabel.place(relx=0.5, rely=0.1, anchor=CENTER)
setNameLabel.place(relx=0.5, rely=0.15, anchor=CENTER)
termLabel.place(relx=0.35,rely=0.25, anchor=CENTER)
definitionLabel.place(relx=0.65,rely=0.25, anchor=CENTER)
setNameEntry.place(relx=0.5, rely=0.2, width=140, height=30, anchor=CENTER)
addTermDefButton.place(relx=0.5, rely=0.35, height=25, anchor=CENTER)
termInput.place(relx=0.35,rely=0.3, anchor=CENTER)
definitionInput.place(relx=0.65,rely=0.3, anchor=CENTER)

raise_frame(gray_background)
raise_frame(create_set_frame)

set_buttons_loop()
get_user_loop()
root.mainloop()