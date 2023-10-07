import socket
import random
from tkinter import *
from threading import Thread
from PIL import ImageTk, Image

screen_width = None
screen_height = None

SERVER = None
PORT = None
IP_ADDRESS = None


canvas1 = None

playerName = None
nameEntry = None
nameWindow = None

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    PORT  = 5000
    IP_ADDRESS = '127.0.0.1'

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))
    askPlayerName()

def askPlayerName():
    global playerName
    global nameEntry
    global nameWindow
    global canvas1
    global screen_height
    global screen_width

    nameWindow = Tk()
    nameWindow.title("  Tambola Family Fun")
    nameWindow.geometry('800x600')

    screen_height = nameWindow.winfo_screenheight()
    screen_width = nameWindow.winfo_screenwidth()

    bg = ImageTk.PhotoImage(file="./assets/background.png")

    canvas1 = Canvas(nameWindow , width=500 , height=500)
    canvas1.pack(fill="both", expand = True)
    canvas1.create_image(0,0, image = bg,anchor="nw")
    canvas1.create_text(screen_width/4.5,screen_height/8,text="Enter your name", font=("Chalkboard SE", 100), fill="black")

    nameEntry = Entry(nameWindow ,width=15,justify="center", font=("Chalkboard SE", 12),bg="white",bd=5)
    nameEntry.place(x=screen_width/7 ,y = screen_height/5.5)


    button = Button(nameWindow , text="SAVE",font=("Chalkboard SE", 30), width=11, height=2, bg="#80deea",bd=3, command = saveName)
    button.place(x=screen_width/6, y = screen_height/4)

def saveName():
    global SERVER, playerName, nameWindow, nameEntry
    playerName = nameEntry.get()
    nameEntry.delete(0, END)
    nameWindow.destroy()
    SERVER.send(playerName.encode())


    nameWindow.resizable(True, True)
    nameWindow.mainloop()

setup()
