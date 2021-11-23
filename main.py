import tkinter as tk
from tkinter import *
import tkinter.font as tkF
from PIL import *


def raise_frame(frame):
    frame.tkraise()

main_screen = tk.Tk()
main_screen.title("Progam Draft")
main_screen.iconbitmap('bunny.ico')

main_screen.geometry("500x500")
font1 = tkF.Font(family="Calibri", size=40)
font2 = tkF.Font(family="Calibri", size=15)

frame_1= Frame(main_screen, width=500, height=500)
frame_2 = Frame(main_screen, width=500, height=500)
frame_3 = Frame(main_screen, width=500, height=500)

main_screen.grid_columnconfigure(1, weight=1)

for frame in (frame_1, frame_2, frame_3):
    frame.grid(row=1, column=1, sticky='news')

#frame 1
label_title = tk.Label(frame_1, text="Title screen draft",padx=0, pady=10, font=font1)
label_title.pack()
button_menu = tk.Button(frame_1, text="Menu", padx=0,pady=10, font=font2, command=lambda:raise_frame(frame_2))
button_menu.pack()

#frame 2
label_1 = tk.Label(frame_2, text="Selection draft", padx=0, pady=10, font=font1)
label_1.pack()
button_1 = tk.Button(frame_2, text="Option", font=font2, command=lambda:raise_frame(frame_3))
button_1.pack()
button_back = tk.Button(frame_2, text="Back to title screen",padx=0, pady=10, font=font2, command=lambda:raise_frame(frame_1))
button_back.pack()

#frame 3
label_option_1 = tk.Label(frame_3, text="Enter option 1", font=font2)
label_option_1.pack()
entry_option_1 = tk.Entry(frame_3, borderwidth=2.5)
entry_option_1.pack()

label_pass1= tk.Label(frame_3, text="Enter pass 1", font=font2)
label_pass1.pack()
entry_pass1 = tk.Entry(frame_3, borderwidth=2.5)
entry_pass1.pack()

button_back1 = tk.Button(frame_3, text="Back", font=font2, command=lambda:raise_frame(frame_2))
button_back1.pack()


main_screen.resizable(False, False)
raise_frame(frame_1)
main_screen.mainloop()

