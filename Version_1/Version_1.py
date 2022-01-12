import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.font as tkF
import tkinter as GUI
from tkinter import messagebox
import sqlite3
from PIL import *
from configparser import ConfigParser
import os
import hashlib
from colorama import *

#CHECK IF MAIN PASSWORD TABLE EXISTS 
try:
    os.system("python Password_Database.py")
except:
    print("Table exists")
#END CHECK

def raise_frame(frame):
    frame.tkraise()

def exit_program():
    main_screen.destroy()

main_screen = tk.Tk()
main_screen.title("Password Manager")
main_screen.iconbitmap('bunny.ico')


main_screen.geometry("750x600")
main_screen.resizable(False, False)
font1 = tkF.Font(family="Calibri", size=40)
font2 = tkF.Font(family="Calibri", size=15)


frame_67 = Frame(main_screen)
frame_68 = Frame(main_screen)
frame_69 = Frame(main_screen)
frame_0 = Frame(main_screen)
frame_1 = Frame(main_screen)
frame_2 = Frame(main_screen)
frame_3 = Frame(main_screen)
frame_4 = Frame(main_screen)
frame_5 = Frame(main_screen)

main_screen.grid_columnconfigure(1, weight=1)

for frame in (frame_67, frame_68, frame_69, frame_0, frame_1, frame_2, frame_3, frame_4, frame_5):
    frame.grid(row=1, column=1, sticky='news')

#CHECK IF MAIN PASSWORD TABLE EXISTS 
try:
    os.system("python Main_Database.py")
except:
    print("Table exists")
#END CHECK

#MODULE 2 DTABASE FUNCTION

def verify():
    connectivity = sqlite3.connect('Master.db')
    cursor = connectivity.cursor()

    cursor.execute("""SELECT *, oid from Master_password""")
    your_mom = cursor.fetchall()
    if len(your_mom)==0:
        messagebox.showwarning("Warning", "Please configure master password")
    else:
        raise_frame(frame_67)


    connectivity.commit()
    connectivity.close()

def register():
    connectivity = sqlite3.connect('Master.db')
    cursor = connectivity.cursor()

    cursor.execute("""Select *, oid from Master_password""")
    your_mom2 = cursor.fetchall()
    if len (your_mom2)==0:
        raise_frame(frame_68)
    else:
        messagebox.showinfo("Info", "Master password already exists. Please verify password.")


#FRAME 68 REGISTER SCREEN
label_big = tk.Label(frame_68, text="Configure master password", font=font1).pack()
label_enter = tk.Label(frame_68, text="Create new password: ", font=font2).pack()
entry_enter = tk.Entry(frame_68, borderwidth=2.5, width=40, show='*')
entry_enter.pack()
label_2 = tk.Label(frame_68, text="Enter new password again: ", font=font2).pack()
entry_2 = tk.Entry(frame_68, borderwidth=2.5, width=40, show='*')
entry_2.pack()

#FRAME 68 BUTTON FUNCTION
def configure():
    global hash_value
    hash_value = hashlib.sha256(entry_enter.get().encode('utf-8')).hexdigest()
    connectivity = sqlite3.connect('Master.db')
    cursor = connectivity.cursor()

    if len(entry_enter.get())==0 or len(entry_2.get())==0:
        messagebox.showwarning("Warning", "Must complete all available fields")
    elif len(entry_enter.get())<10:
        messagebox.showwarning("Warning", "Password must be at least 10 characters long")
    elif entry_enter.get() != entry_2.get():
        messagebox.showwarning("Warning", "Passwords do not match")
    else:
        question = messagebox.askyesno("Proceed", "Are you sure you would like to preceed? The master password cannot be recovered or reset.")
        if question == 1:
            cursor.execute("INSERT INTO Master_password VALUES (:Password_1)",
            {
                'Password_1': hash_value
            }
            )
            raise_frame(frame_1)
            import string    
            import random 
            ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10))    
            randon_value = str(ran)
            messagebox.showwarning("Backup key", "Attention! This is your one time password retrieval key. This data will not be saved. Once you reconfigure your password, this key will change:")
            messagebox.showinfo("Succes", "Master password successfully configured. I hope you enjoy the program!")


    connectivity.commit()
    connectivity.close()

#FRAME 68
button_register2 = tk.Button(frame_68, text="Configure password", pady=10, font=font2, width=20, command=configure).pack()

def exit_2():
    main_screen.destroy()

#FRAME 69 LOGIN SCREEN
label_password = tk.Label(frame_69, text="Master Window", font=font1)
label_password.pack()
button_login = tk.Button(frame_69, text="Verify password", pady=10, font=font2, command=verify)
button_login.pack()
button_register = tk.Button(frame_69, text="Register",padx=34, pady=10, font=font2, command=register)
button_register.pack()
button_exit2 = tk.Button(frame_69, text="Exit", padx=52, pady=10, font=font2, command=exit_2)
button_exit2.pack()


#FRAME 67
label_verify = tk.Label(frame_67, text="Verify master password", font=font1).pack()
label_enter2 = tk.Label(frame_67, text="Enter master password: ", font=font2).pack()
entry_enter2 = tk.Entry(frame_67, borderwidth=2.5, width=40, show='*')
entry_enter2.pack()

def verify_2():
    hash_value_2 = hashlib.sha256(entry_enter2.get().encode('utf-8')).hexdigest()
    connectivity = sqlite3.connect('Master.db')
    cursor = connectivity.cursor()

    if len(entry_enter2.get())==0:
        messagebox.showwarning("Warning", "Must complete all available fields")
    else:
        entry_copyl = []
        entry_copyl.append(hash_value_2)
        entry_copyt = tuple(entry_copyl)

        select_3 = """SELECT * from Master_password"""
        cursor.execute(select_3)
        your_mom3 = cursor.fetchall()
        for moms in your_mom3:
            if moms == entry_copyt:
                raise_frame(frame_1)
            else:
                messagebox.showwarning("Warning", "Incorrect password")

    connectivity.commit()
    connectivity.close()

button_enter = tk.Button(frame_67, text="Verify", pady=10, width=15, font=font2, command=verify_2).pack()
button_back3 = tk.Button(frame_67, text="Back", pady=10, width=15, font=font2, command=lambda:raise_frame(frame_69))
button_back3.pack()


#parser = ConfigParser()
#parser.read("dark_mode_settungs.ini")
#saved_color = parser.get('backgroundcolor', 'color' )

#SETTINGS FUNCTIONS
def background_color():
    #parser = ConfigParser()
    #parser.read("dark_mode_settungs.ini")
    #parser.set('backgroundcolor', 'color', 'dark blue')
    #with open("dark_mode_settungs.ini", "w") as configfile:
        #parser.write(configfile)
    for frame in (frame_0, frame_1, frame_2, frame_3, frame_4, frame_5):
        frame.configure(background='dark blue')
        for widget in frame.winfo_children():
            widget.configure(background='dark blue')
    main_screen.configure(background='dark blue')


def off():
    #parser = ConfigParser()
    #parser.read("dark_mode_settungs.ini")
    #parser.set('backgroundcolor', 'color', 'grey94')
    #with open("dark_mode_settungs.ini", "w") as configfile:
        #parser.write(configfile)
    for frame in (frame_0, frame_1, frame_2, frame_3, frame_4, frame_5):
        frame.configure(background='grey94')
        for widget in frame.winfo_children():
            widget.configure(background='grey94')
    main_screen.configure(background='grey94')

#FRAME 0 (SETTINGS MENU)
label_title0 = tk.Label(frame_0, text="Settings Menu", font=font1)
label_title0.place(x=220, y=0)
label_resizable = tk.Label(frame_0, text="Dark mode: ", font=font2).place(x=220, y=80)
button_on = tk.Button(frame_0, text="On", font=font2, command=background_color).place(x=340, y=75)
button_on = tk.Button(frame_0, text="Off", font=font2, command=off).place(x=400, y=75)
button_back0 = tk.Button(frame_0, text="Back to title screen", padx=10, pady=10, font=font2, command=lambda:raise_frame(frame_1)).place(x=300, y=150)

#FRAME 1

label_title = tk.Label(frame_1, text="Password Manager",padx=0, pady=10, font=font1)
label_title.pack()
button_menu = tk.Button(frame_1, text="Menu", padx=20,pady=10, font=font2, command=lambda:raise_frame(frame_2))
button_menu.pack()
button_settings = tk.Button(frame_1, text="Settings", padx=11, pady=10, font=font2, command=lambda:raise_frame(frame_0))
button_settings.pack()
button_reset = tk.Button(frame_1, text="Reset ptogram", font=font2, padx=10, pady=10)
button_reset.pack()
button_exit = tk.Button(frame_1, text="Exit", padx=28, pady=10, font=font2, command=exit_program)
button_exit.pack()

#FRAME 2
label_1 = tk.Label(frame_2, text="Options", font=font1)
label_1.pack()
button_1 = tk.Button(frame_2, text="Add record", font=font2, padx=68, pady=10, command=lambda:raise_frame(frame_3))
button_1.pack()
button_2 = tk.Button(frame_2, text="Modify/Delete record", padx=25, pady=10, font=font2, command=lambda:raise_frame(frame_4))
button_2.pack()
button_3  = tk.Button(frame_2,text="Show records", padx=60, pady=10, font=font2, command=lambda:raise_frame(frame_5))
button_3.pack()
button_back = tk.Button(frame_2, text="Back to title screen",padx=38, pady=10, font=font2, command=lambda:raise_frame(frame_1))
button_back.pack()

#FRAME 3

label_master1 = tk.Label(frame_3, text="Add record", font=font1)
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
entry_pass = tk.Entry(frame_3, borderwidth=2.5, width=40, show='*')
entry_pass.pack()

#DATABASE FUNCTION FRAME 3
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
button_insert = tk.Button(frame_3, text="Add record to database", font=font2, padx=30, pady=10, command=insert)
button_insert.pack()
button_back = tk.Button(frame_3, text="Back", font=font2, padx=111, pady=10, command=lambda:raise_frame(frame_2))
button_back.pack()

#FRAME 4
label_master2 = tk.Label(frame_4, text="Delete or modify record", font=font1)
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

def show_all():
    top = tk.Toplevel()
    top.geometry("1000x400")
    top.resizable(False, False)
    top.title("All records")
    top.iconbitmap('bunny.ico')

    frame_scrollbar = tk.Frame(top)
    frame_scrollbar.pack(fill=BOTH, expand=1)
    canvas_scrollbar = tk.Canvas(frame_scrollbar)
    canvas_scrollbar.pack(side=LEFT, fill=BOTH, expand=1)
    scrollbar = ttk.Scrollbar(frame_scrollbar, orient=VERTICAL, command=canvas_scrollbar.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    canvas_scrollbar.configure(yscrollcommand=scrollbar.set)
    canvas_scrollbar.bind('<Configure>', lambda e: canvas_scrollbar.configure(scrollregion = canvas_scrollbar.bbox("all")))
    frame_scrollbar2 = tk.Frame(canvas_scrollbar)
    canvas_scrollbar.create_window((0,0), window=frame_scrollbar2, anchor="nw")

    connectivity = sqlite3.connect('Pass.db')

    cursor = connectivity.cursor()

    
    select_all = """SELECT *, oid from Passes"""
    cursor.execute(select_all)
    values3 = cursor.fetchall()

    print_value3 = ''
    for value in values3:
        print_value3 = ''
        print_value3 +=  "Platform/Username: " + str(value[0]) + ", " + "URL: " + str(value[1]) + ", " + "Password: " + str(value[2]) + ", "  + "ID Number: " + str(value[3])
        label_value3 = tk.Label(frame_scrollbar2, text=print_value3, pady=10)
        label_value3.pack() 

    cursor.close()

    connectivity.commit()
    connectivity.close()

button_show_all = tk.Button(frame_5, text="Show all records", padx=10, pady=10, font=font2, command=show_all)
button_show_all.pack()

label_select1 = tk.Label(frame_5, text="Record ID:", font=font2)
label_select1.pack()

entry_show_ID = tk.Entry(frame_5)
entry_show_ID.pack()

#DATABASE FUNCTION FRAME 5
global label_value
def show_one():
    connectivity = sqlite3.connect('Pass.db')

    cursor = connectivity.cursor()

    select_copy = """SELECT oid from Passes"""
    cursor.execute(select_copy)
    values = cursor.fetchall()
    if entry_show_ID.get().isnumeric() == True:
        test2 = int(entry_show_ID.get())
        test2_list=[]
        test2_list.append(test2)
        test2_tuple = tuple(test2_list)
        bool2_select = False
        for value in values:
            if sorted(test2_tuple) == sorted(value):
                bool2_select = True
                break   
    cursor.close()

    connectivity.commit()
    connectivity.close()        

    if len(entry_show_ID.get()) == 0:
        messagebox.showwarning("Warning", "Must complete all fields")
    elif entry_show_ID.get().isnumeric() == False:
        messagebox.showwarning("Warning", "Input must be a positive integer")
    elif bool2_select == False:
        messagebox.showwarning("Warning", "Record ID outside of range")
    else:
        connectivity = sqlite3.connect('Pass.db')

        cursor = connectivity.cursor()

        select = ("SELECT *, oid from Passes WHERE oid = " + entry_show_ID.get())
        cursor.execute(select)
        values2 = cursor.fetchall()
        global label_value
        print_value = ''
        for value in values2:
            print_value += "Platform/Username: " + str(value[0]) + ", " + "URL: " + str(value[1]) + ", " + "Password: " + str(value[2]) + "\n" + "ID Number: " + str(value[3]) + "\n"  
        label_value = tk.Label(frame_5, text=print_value, pady=10, font=font2)
        label_value.pack()

        cursor.close()

        connectivity.commit()
        connectivity.close()
        button_show_one['state'] = GUI.DISABLED


def hide_one():
    button_show_one['state'] = GUI.NORMAL
    label_value.pack_forget()

label_space2 = tk.Label(frame_5, text="    ", padx=64, pady=0, font=font2)
label_space2.pack()

button_show_one = tk.Button(frame_5, text="Show record", padx=30, pady=10, font=font2, command=show_one)
button_show_one.pack()

button_hide_one = tk.Button(frame_5, text="Hide record", padx=34, pady=10, font=font2, command=hide_one)
button_hide_one.pack()

button_back2 = tk.Button(frame_5, text="Back", padx=64, pady=10, font=font2, command=lambda:raise_frame(frame_2))
button_back2.pack()


main_screen.resizable(False, False)
raise_frame(frame_69)

main_screen.mainloop()


