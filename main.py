import datetime
#import tkMessageBox
import webbrowser
# from Tkinter import Tk
# from copy import t
from tkinter.colorchooser import askcolor
import background as background
#import self as self
# import tk as Tk
#import tkinter as tk
from tkinter.filedialog import *
import speech_recognition as sr
def line():
 lin = "_" * 60
 text.insert(INSERT, lin)
def date():
 data = datetime.date.today()
 text.insert(INSERT, data)
def normal():
 text.config(font=("Arial", 10))
def bold():
 text.config(font=("Arial", 10, "bold"))
def underline():
 text.config(font=("Arial", 10, "underline"))
def italic():
 text.config(font=("Arial", 10, "italic"))
def font():
 (triple, color) = askcolor()
 if color:
 text.config(foreground=color)
def kill():
 root.destroy()
def about():
 pass
def nw():
 root.title("Untitled Notepad")
 text.delete(1.0, END)
def opn():
 text.delete(1.0, END)
 file = open(askopenfilename(), 'r')
 if file != '':
 txt = file.read()
 text.insert(INSERT, txt)
 else:
 pass
def save():
 filename = asksaveasfilename()
 if filename:
 alltext = text.get(1.0, END)
 open(filename, 'w').write(alltext)
def copy():
 text.clipboard_clear()
 text.clipboard_append(text.selection_get())
def paste():
 try:
 teext = text.selection_get(selection='CLIPBOARD')
 text.insert(INSERT, teext)
 except:
 tkMessageBox.showerror("error", "Can't Paste your text!")
def clear():
 text.delete(SEL_FIRST, SEL_LAST)
def clearall():
 text.delete(1.0, END)
def askcolor(color=None):
 if color:
 text.config(background=color)
def about():
 ab = Toplevel(root)
 txt = "Hello this is special wishes to 'You' thanks for being here"
 la = Label(ab, text=txt, foreground='black')
 la.pack()
def web():
 webbrowser.open('http://www.siot.org.in')
def rec():
 re = Toplevel(root)
 txt = "Hello this is special wishes to 'You' thanks for being here"
 la = Label(re, text=txt, foreground='black')
 la.pack()
def mic():
 r = sr.Recognizer()
 #msg.configure(text="Say something")
 while True:
 with sr.Microphone() as source:
 r.adjust_for_ambient_noise(source)
 audio = r.listen(source)
 try:
 txt = r.recognize_google(audio)
 #msg.configure(text=txt)
 #print(txt)
 #var = StringVar()
 #Label(root, textvariable=var, bg="white", relief=RAISED).place(x=7,
y=30)
 #var.set("did you said" + txt)
 text.insert(INSERT, txt)
 except Exception as e:
 print(e)
 break
root = Tk()
root.title("Panda Notepad")
menu = Menu(root)
filemenu = Menu(root)
root.config(menu=menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New...", command=nw)
filemenu.add_command(label="Open...", command=opn)
filemenu.add_command(label="Save...", command=save)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=kill)
modmenu = Menu(root)
menu.add_cascade(label="Mode", menu=modmenu)
modmenu.add_command(label="Copy", command=copy)
modmenu.add_command(label="paste", command=paste)
modmenu.add_separator()
modmenu.add_command(label="Clear selected", command=clear)
modmenu.add_command(label="Clear all", command=clearall)
insmenu = Menu(root)
menu.add_cascade(label="Insert", menu=insmenu)
insmenu.add_command(label="Date", command=date)
insmenu.add_command(label="Line", command=line)
formatmenu = Menu(menu)
menu.add_cascade(label="Format", menu=formatmenu)
formatmenu.add_cascade(label="Times New Roman...", command=font)
formatmenu.add_separator()
formatmenu.add_radiobutton(label='Normal', command=normal)
formatmenu.add_radiobutton(label='bold', command=bold)
formatmenu.add_radiobutton(label='underline', command=underline)
formatmenu.add_radiobutton(label='italic', command=italic)
persomenu = Menu(root)
menu.add_cascade(label="Personalize", menu=persomenu)
persomenu.add_command(label="background...", command=background)
Featuresmenu = Menu(menu)
menu.add_cascade(label="Features", menu=Featuresmenu)
Featuresmenu.add_command(label="mic", command=mic)
Helpmenu = Menu(menu)
menu.add_cascade(label="Help?", menu=Helpmenu)
Helpmenu.add_command(label="Click ME", command=about)
Helpmenu.add_command(label="Website", command=web)
text = Text(root, height=150, width=300, font=("Arial", 10))
scroll = Scrollbar(root, command=text.yview())
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)
scroll.pack(side=RIGHT, fill=Y)
text.pack()
root.mainloop()