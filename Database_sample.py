import tkinter as tk
import sqlite3

main_screen = tk.Tk()
main_screen.geometry("750x750")

connectivity = sqlite3.connect('test.db')

c = connectivity.cursor()

#c.execute('''CREATE TABLE test (
#   web text,
#   hex integer
#    )''')

entry_1 = tk.Entry(main_screen)
entry_1.pack()

entry_2 = tk.Entry(main_screen)
entry_2.pack()

def put_in():
    connectivity = sqlite3.connect('test.db')

    c = connectivity.cursor()

    c.execute("INSERT INTO test VALUES (:web, :hex)",
            {
                'web': entry_1.get(),
                'hex': entry_2.get()
            }
            )

    

    connectivity.commit()
    connectivity.close()


               
def show():
    connectivity = sqlite3.connect('test.db')

    c = connectivity.cursor()

    c.execute("SELECT *, oid FROM test")
    values = c.fetchall()
    print(type(values))
    print(values)

    connectivity.commit()
    connectivity.close()

button_1 = tk.Button(main_screen, text="Submit", command=put_in())
button_1.pack()

button_2 =tk.Button(main_screen, text="Show records", command=show())
button_2.pack()

connectivity.commit()
connectivity.close()

main_screen.resizable(False, False)
main_screen.mainloop()