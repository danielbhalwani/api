import requests
from tkinter import *
import webbrowser
import tkinter as tk


def grab():
 myurl = "https://swapi.co/api/people/" + etr.get()
 response = requests.get(myurl)
 datajson = response.json()
 writeto(datajson)

def writeto(datajson):
 file_o = open("starwars.html", "w")
 file_o.write("<link rel='stylesheet' type='text/css' href='danielstyle.css'>")
 file_o.write("<body style='margin:0;'> <img src='war.jpg' width=100%></body>")
 file_o.write("<h1>""Facts about " + str((datajson['name'])) + ":" + "</h1>")
 file_o.write("<table><tr>")
 file_o.write("<td>" + "Height: " + "</td><td>" + str(datajson['height']) + " inches" + "</td></tr>")
 file_o.write("<tr><td>" + "Mass: " + "</td><td>" + str(datajson['mass']) + " kilograms" + "</td></tr>")
 file_o.write("<tr><td>" + "Hair color: " + "</td><td>" + str(datajson['hair_color']) + "</td></tr>")
 file_o.write("<tr><td>" + "Skin color: " + "</td><td>" + str(datajson['skin_color']) + "</td></tr>")
 file_o.write("<tr><td>" + "Eye color: " + "</td><td>" + str(datajson['eye_color']) + "</td></tr>")
 file_o.write("<tr><td>" + "Gender: " + "</td><td>" + str(datajson['gender']) + "</td></tr>")
 file_o.write("</table>")
 file_o.close()

root = Tk()
root.title('Starwars API')
root.geometry("600x350")

lab = Label(root, text = "Welcome to Starwars Database!", background = "yellow")
lab.config(font=("Verdana",35))
lab.place(x=10, y=10)

OPTIONS = [
	"1 = Luke Skywalker",
	"2 = C-3PO",
	"3 = R2-D2",
	"4 = Darth Vader",
	"5 = Leia Organa",
	"6 = Owen Lars",
	"7 = Beru Whitesun lars",
	"8 = R5-D4",
	"9 = Biggs Darklighter",
	"10 = Obi-Wan Kenobi",
	

	
]
variable = tk.StringVar(root)
variable.set(OPTIONS[0])
dropDownMenu1 = tk.OptionMenu(root,variable, OPTIONS[0],OPTIONS[1], OPTIONS[2], OPTIONS[3],OPTIONS[4],OPTIONS[5],OPTIONS[6],OPTIONS[7],OPTIONS[8], OPTIONS[9])
dropDownMenu1.grid(sticky="W,E")
dropDownMenu1.place(x=30, y=300)
dropDownMenu1.place()

OPTIONS = [
	"11 = Anakin Skywalker",
	"12 = Wilhuff Tarkin",
	"13 = Chewbacca",
	"14 = Han Solo",
	"15 = Greedo",
	"16 = Jabba Desilijic Tiure",
	"17 = NA",
	"18 = Wedge Antilles",
	"19 = Jek Tono Porkins",
	"20 = Yoda",
	

	
]
variable = tk.StringVar(root)
variable.set(OPTIONS[0])
dropDownMenu1 = tk.OptionMenu(root,variable, OPTIONS[0],OPTIONS[1], OPTIONS[2], OPTIONS[3],OPTIONS[4],OPTIONS[5],OPTIONS[6],OPTIONS[7],OPTIONS[8], OPTIONS[9])
dropDownMenu1.grid(sticky="W,E")
dropDownMenu1.place(x=190, y=300)
dropDownMenu1.place()


OPTIONS = [
	"21 = Palpatine",
	"22 = Boba Fett",
	"23 = IG-88",
	"24 = Bossk",
	"25 = Lando Calrissian",
	"26 = Lobot",
	"27 = Ackbar",
	"28 = Mon Mothma",
	"29 = Arvel Crynyd",
	"30 = Wicket Systri Warrick",
	

	
]
variable = tk.StringVar(root)
variable.set(OPTIONS[0])
dropDownMenu1 = tk.OptionMenu(root,variable, OPTIONS[0],OPTIONS[1], OPTIONS[2], OPTIONS[3],OPTIONS[4],OPTIONS[5],OPTIONS[6],OPTIONS[7],OPTIONS[8], OPTIONS[9])
dropDownMenu1.place(x=375, y=300)
dropDownMenu1.place()



lab1 = Label(root, text = "Enter a number between 1-30:")
lab1.config(font=("Verdana",15))
lab1.place(x=30, y=90)

lab1 = Label(root, text = "(HTML file on hard drive...)")
lab1.config(font=("Verdana",10))
lab1.place(x=70, y=200)

btn = Button(root, text = "Head to website!", background = "white",command = grab)
btn.place(x=82, y=170)
btn.config(font=("Helvetica", 15 , "bold"))

etr = Entry(root, width=20)
etr.place(x=50, y=120)

img = PhotoImage(file = "stardestroyer.jpg")
imglabel = Label(root, image=img)
imglabel.place(x=300, y=70, width=280, height=170)

mainloop()