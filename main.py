import tkinter as tk
from tkinter import *
import tkinter.font as tkF
import tkinter as GUI
from tkinter import messagebox
import sqlite3
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

def exit_program():
    main_screen.destroy()

main_screen = tk.Tk()
main_screen.title("Progam Draft")
main_screen.iconbitmap('bunny.ico')


main_screen.geometry("750x750")
font1 = tkF.Font(family="Calibri", size=40)
font2 = tkF.Font(family="Calibri", size=15)

frame_1= Frame(main_screen)
frame_2 = Frame(main_screen)
frame_3 = Frame(main_screen)
frame_4 = Frame(main_screen)
frame_5 = Frame(main_screen)

main_screen.grid_columnconfigure(1, weight=1)

for frame in (frame_1, frame_2, frame_3, frame_4, frame_5):
    frame.grid(row=1, column=1, sticky='news')

#FRAME 1
label_title = tk.Label(frame_1, text="Title screen draft",padx=0, pady=10, font=font1)
label_title.pack()
button_menu = tk.Button(frame_1, text="Menu", padx=20,pady=10, font=font2, command=lambda:raise_frame(frame_2))
button_menu.pack()
button_settings = tk.Button(frame_1, text="Settings", padx=11, pady=10, font=font2)
button_settings.pack()
button_exit = tk.Button(frame_1, text="Exit", padx=28, pady=10, font=font2, command=exit_program)
button_exit.pack()


#FRAME 2
label_1 = tk.Label(frame_2, text="Selection draft", font=font1)
label_1.pack()
button_1 = tk.Button(frame_2, text="Add entry", font=font2, padx=68, pady=10, command=lambda:raise_frame(frame_3))
button_1.pack()
button_2 = tk.Button(frame_2, text="Modify/Delete entry", padx=25, pady=10, font=font2, command=lambda:raise_frame(frame_4))
button_2.pack()
button_3  = tk.Button(frame_2,text="Show records", padx=54, pady=10, font=font2, command=lambda:raise_frame(frame_5))
button_3.pack()
button_back = tk.Button(frame_2, text="Back to title screen",padx=30, pady=10, font=font2, command=lambda:raise_frame(frame_1))
button_back.pack()

#FRAME 3

label_master1 = tk.Label(frame_3, text="Add entry", font=font1)
label_master1.pack()

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

#DATABASE FUNCTION FRAME3 3
def insert():
    connectivity = sqlite3.connect('Pass.db')

    cursor = connectivity.cursor()
 
    if len(entry_platform.get())==0 or len(entry_URL.get())==0 or len(entry_pass.get())==0:
        messagebox.showwarning("Warning", "Must complete all available fields!")
    else:
        cursor.execute("INSERT INTO Passes VALUES (:Platform, :URL, :Password)",
            {
                'Platform': entry_platform.get(),
                'URL': entry_URL.get(),
                'Password': entry_pass.get()
            })

        entry_platform.delete(0, 'end')
        entry_URL.delete(0, 'end')
        entry_pass.delete(0, 'end')

        messagebox.showinfo("Info", "Successfully added to database")

    connectivity.commit()
    connectivity.close()
#FRAME 3
label_space1 = tk.Label(frame_3, text="    ", padx=105, pady=1, font=font2)
label_space1.pack()
button_insert = tk.Button(frame_3, text="Add entry to database", font=font2, padx=30, pady=10, command=insert)
button_insert.pack()
button_back = tk.Button(frame_3, text="Back", font=font2, padx=105, pady=10, command=lambda:raise_frame(frame_2))
button_back.pack()

#FRAME 4
label_master2 = tk.Label(frame_4, text="Delete or modify entry", font=font1)
label_master2.pack()
label_select = tk.Label(frame_4, text="Record ID: ", font=font2)
label_select.pack()
entry_select = tk.Entry(frame_4, borderwidth=2.5, width=40 )
entry_select.pack()
label_space1 = tk.Label(frame_4, text="    ", padx=105, pady=1, font=font2)
label_space1.pack()
#DATABESE FUNCTIONS FRAME 4 
def show_records():
    connectivity = sqlite3.connect('Pass.db')

    cursor = connectivity.cursor()

    select = """SELECT *, oid from Passes"""
    cursor.execute(select)
    values = cursor.fetchall()
    global label_show_records
    label_show_records = tk.Label(frame_4, text="Number of records: " + str(len(values)), font=font2)
    label_show_records.pack()
    button_show_records['state'] = GUI.DISABLED

    cursor.close()

    connectivity.commit()
    connectivity.close()


def delete():
    connectivity = sqlite3.connect('Pass.db')

    cursor = connectivity.cursor()

    select1 = """SELECT oid from Passes"""
    cursor.execute(select1)
    values1 = cursor.fetchall()
    if entry_select.get().isnumeric() == True:
        test = int(entry_select.get())
        test_list=[]
        test_list.append(test)
        test_tuple = tuple(test_list)
        bool_select = False
        for value in values1:
            if sorted(test_tuple) == sorted(value):
                bool_select = True
                break
          


    if len(entry_select.get()) == 0:
        messagebox.showwarning("Warning", "Must specify record ID")
    elif entry_select.get().isnumeric() == False: 
        messagebox.showwarning("Warning", "Input must be a positive integer")
    elif bool_select == False:
        messagebox.showwarning("Warning", "Record ID outside of range")
    else:
        delete = "DELETE from Passes WHERE oid= " + entry_select.get()
        cursor.execute(delete)
        messagebox.showinfo("Info", "Record successfully deleted")

    cursor.close()

    entry_select.delete(0, 'end')

    connectivity.commit()
    connectivity.close()


def hide_records():
    label_show_records.pack_forget()
    button_show_records['state'] = GUI.NORMAL

button_delete = tk.Button(frame_4, text="Delete record", padx=67, pady=10, font=font2, command=delete)
button_delete.pack()
button_modify = tk.Button(frame_4, text="Modify record", padx=65, pady=10, font=font2)
button_modify.pack()
button_show_records = tk.Button(frame_4, text="Show number of records", padx=22, pady=10, font=font2, command=show_records)
button_show_records.pack()
button_hide_records  = tk.Button(frame_4, text="Hide number of records", padx=25, pady=10, font=font2, command=hide_records)
button_hide_records.pack()
button_back1 = tk.Button(frame_4, text="Back", padx=105, pady=10, font=font2, command=lambda:raise_frame(frame_2))
button_back1.pack()

#FRAME 5
label_master3 = tk.Label(frame_5, text="View records", font=font1)
label_master3.pack()

button_show_all = tk.Button(frame_5, text="Show all records", padx=10, pady=10, font=font2)
button_show_all.pack()

label_select1 = tk.Label(frame_5, text="Record ID:", font=font2)
label_select1.pack()

entry_show_ID = tk.Entry(frame_5)
entry_show_ID.pack()

#DATABASE FUNCTION FRAME 5
def show_one():
    connectivity = sqlite3.connect('Pass.db')

    cursor = connectivity.cursor()

    select = ("SELECT *, oid from Passes WHERE oid = " + entry_show_ID.get())
    cursor.execute(select)
    values = cursor.fetchall()

    print_value = ''
    for value in values:
        print_value += "Platform/Username: " + str(value[0]) + ", " + "URL: " + str(value[1]) + ", " + "Password: " + str(value[2]) + "\n" + "ID Number: " + str(value[3]) + "\n"  

    if entry_show_ID.get() == 0:
        messagebox.showwarning("Warning", "Must complete all fields")
    elif entry_show_ID.get().isalnumeric() == True:
        messagebox.showwarning("Warning")

    global label_value
    label_value = tk.Label(frame_5, text=print_value, pady=10, font=font2)
    label_value.pack()

    cursor.close()

    connectivity.commit()
    connectivity.close()


def hide_one():
    label_value.pack_forget()
    button_show_one['state'] = GUI.NORMAL

label_space2 = tk.Label(frame_5, text="    ", padx=64, pady=0, font=font2)
label_space2.pack()

button_show_one = tk.Button(frame_5, text="Show record", padx=30, pady=10, font=font2, command=show_one)
button_show_one.pack()

button_hide_one = tk.Button(frame_5, text="Hide record", padx=30, pady=10, font=font2, command=hide_one)
button_hide_one.pack()

button_back2 = tk.Button(frame_5, text="Back", padx=64, pady=10, font=font2, command=lambda:raise_frame(frame_2))
button_back2.pack()

connectivity.commit()
connectivity.close()

main_screen.resizable(False, False)
raise_frame(frame_1)

main_screen.mainloop()



