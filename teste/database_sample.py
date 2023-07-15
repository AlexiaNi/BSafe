import tkinter as tk
import tkinter as GUI
from tkinter import messagebox
import sqlite3

main_screen = tk.Tk()
main_screen.geometry("750x750")

connectivity = sqlite3.connect('test.db')

cursor = connectivity.cursor()

Label = tk.Label(main_screen, text="Sample Database")
Label.pack()

#cursor.execute("""CREATE TABLE test(
#        Platform text,
#        Password text     


#    )""")

entry_1 = tk.Entry(main_screen)
entry_1.pack()

entry_2 = tk.Entry(main_screen)
entry_2.pack()

label_delete = tk.Label(main_screen, text="If you wish to delete a record insert ID Number: ")
label_delete.pack()

entry_3 = tk.Entry(main_screen)
entry_3.pack()

def put_in():
    connectivity = sqlite3.connect('test.db')

    cursor = connectivity.cursor()

    cursor.execute("INSERT INTO test VALUES (:Platform, :Password)",
            {
                'Platform': entry_1.get(),
                'Password': entry_2.get()
            }
            )

    entry_1.delete(0, 'end')
    entry_2.delete(0, 'end')

    connectivity.commit()
    connectivity.close()


               
def show():
    connectivity = sqlite3.connect('test.db')

    cursor = connectivity.cursor()

    select = """SELECT *, oid from test"""
    cursor.execute(select)
    values = cursor.fetchall()

    print_value = ''
    for value in values:
        print_value += str(value[0]) + " " + str(value[1]) + "\n" + "ID Number: " + str(value[2]) + "\n"

    if len(print_value) == 0:  
        button_2['state'] = GUI.NORMAL
    else:
         button_2['state'] = GUI.DISABLED    

    global label_value
    label_value = tk.Label(main_screen, text=print_value, pady=10)
    label_value.pack()

    cursor.close()

    connectivity.commit()
    connectivity.close()



def delete():
    connectivity = sqlite3.connect('test.db')

    cursor = connectivity.cursor()

    if len(entry_3.get()) == 0:
        messagebox.showwarning("Warning", "Must specify record ID")
    else:
        delete = "DELETE from test WHERE oid= " + entry_3.get()
        cursor.execute(delete)

    cursor.close()

    entry_3.delete(0, 'end')

    connectivity.commit()
    connectivity.close()


def hide_records():
    label_value.pack_forget()
    button_2['state'] = GUI.NORMAL

button_1 = tk.Button(main_screen, text="Submit", command=put_in)
button_1.pack()

button_2 =tk.Button(main_screen, text="Show records", command=show)
button_2.pack()

button_3 = tk.Button(main_screen, text="Delete record", command=delete)
button_3.pack()

button_4 = tk.Button(main_screen, text="Hide records", command=hide_records)
button_4.pack()

connectivity.commit()
connectivity.close()

main_screen.resizable(False, False)
main_screen.mainloop()
