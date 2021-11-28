import tkinter as tk
from tkinter import *
import tkinter.font as tkF
import tkinter as GUI
from tkinter import messagebox
import sqlite3
from tkinter import *
from PIL import *

connectivity = sqlite3.connect('Pass.db')
cursor = connectivity.cursor()

#cursor.execute("""CREATE TABLE Passes(
#       Platform text,
#       URL text,
#       Password text     


#  )""")

def raise_frame(frame):
    frame.tkraise()

main_screen = tk.Tk()
main_screen.title("Progam Draft")
main_screen.iconbitmap('bunny.ico')


main_screen.geometry("750x750")
font1 = tkF.Font(family="Calibri", size=40)
font2 = tkF.Font(family="Calibri", size=15)

frame_1= Frame(main_screen)
frame_2 = Frame(main_screen)
frame_3 = Frame(main_screen)

main_screen.grid_columnconfigure(1, weight=1)

for frame in (frame_1, frame_2, frame_3):
    frame.grid(row=1, column=1, sticky='news')

#FRAME 1
label_title = tk.Label(frame_1, text="Title screen draft",padx=0, pady=10, font=font1)
label_title.pack()
button_menu = tk.Button(frame_1, text="Menu", padx=20,pady=10, font=font2, command=lambda:raise_frame(frame_2))
button_menu.pack()


#FRAME 2
label_1 = tk.Label(frame_2, text="Selection draft", padx=0, pady=10, font=font1)
label_1.pack()
button_1 = tk.Button(frame_2, text="Add entry", font=font2, padx=38, pady=10, command=lambda:raise_frame(frame_3))
button_1.pack()
button_back = tk.Button(frame_2, text="Back to title screen",padx=0, pady=10, font=font2, command=lambda:raise_frame(frame_1))
button_back.pack()

#FRAME 3
label_master = tk.Label(frame_3, text="Update records", font=font1)
label_master.pack()

label_platform = tk.Label(frame_3, text="Enter Platform: ", font=font2)
label_platform.pack()
entry_platform = tk.Entry(frame_3, borderwidth=2.5, width=40)
entry_platform.pack()

label_URL= tk.Label(frame_3, text="Enter URL: ", font=font2)
label_URL.pack()
entry_URL = tk.Entry(frame_3, borderwidth=2.5, width=40)
entry_URL.pack()

label_pass = tk.Label(frame_3, text="Enter password: ", font=font2)
label_pass.pack()
entry_pass = tk.Entry(frame_3, borderwidth=2.5, width=40)
entry_pass.pack()

#DATABASE FUNCTIONS
def insert():
    connectivity = sqlite3.connect('Pass.db')

    cursor = connectivity.cursor()

    cursor.execute("INSERT INTO Passes VALUES (:Platform, :URL, :Password)",
            {
                'Platform': entry_platform.get(),
                'URL': entry_URL.get(),
                'Password': entry_pass.get()
            })

    entry_platform.delete(0, 'end')
    entry_URL.delete(0, 'end')
    entry_pass.delete(0, 'end')

    connectivity.commit()
    connectivity.close()


def show():
    connectivity = sqlite3.connect('Pass.db')

    cursor = connectivity.cursor()

    select = """SELECT *, oid from Passes"""
    cursor.execute(select)
    values = cursor.fetchall()

    print_value = ''
    for value in values:
        print_value += "PLatform: " + str(value[0]) + ", " + "URL: " + str(value[1]) + ", " + "Password: " + str(value[2]) + "\n" + "ID Number: " + str(value[2]) + "\n"

    if len(print_value) == 0:  
        button_show['state'] = GUI.NORMAL
    else:
         button_show['state'] = GUI.DISABLED    

    global label_value
    label_value = tk.Label(frame_3, text=print_value, pady=10, font=font2)
    label_value.pack()

    cursor.close()

    connectivity.commit()
    connectivity.close()


def hide_records():
    label_value.pack_forget()
    button_show['state'] = GUI.NORMAL


button_insert = tk.Button(frame_3, text="Add entry to database", font=font2, padx=30, pady=10, command=insert)
button_insert.pack()

button_show = tk.Button(frame_3, text="Show records", font=font2, padx=68, pady=10, command=show)
button_show.pack()

button_hide = tk.Button(frame_3, text="Hide records", font=font2, padx=72, pady=10, command=hide_records)
button_hide.pack()

button_back = tk.Button(frame_3, text="Back", font=font2, padx=105, pady=10, command=raise_frame(frame_2))
button_back.pack()

connectivity.commit()
connectivity.close()

main_screen.resizable(False, False)
raise_frame(frame_1)

main_screen.mainloop()

