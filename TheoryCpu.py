from tkinter import *

def three():
    photo_root = Toplevel()
    photo_root.title("Shortest Response Time First")
    photo_root.resizable(False, False)
    photo = PhotoImage(file="Theory/SRTF.png")
    photo_label = Label(photo_root, image=photo)
    photo_label.pack()
    photo_root.mainloop()


def four():
    photo_root = Toplevel()
    photo_root.title("Least Response Ratio Next")
    photo_root.resizable(False, False)
    photo = PhotoImage(file="Theory/LRRN.png")
    photo_label = Label(photo_root, image=photo)
    photo_label.pack()
    photo_root.mainloop()


def five():
    photo_root = Toplevel()
    photo_root.title("Highest Response Ratio Next")
    photo_root.resizable(False, False)
    photo = PhotoImage(file="Theory/HRRN2.PNG")
    photo_label = Label(photo_root, image=photo)
    photo_label.pack()
    photo_root.mainloop()


def six():
    photo_root = Toplevel()
    photo_root.title("Round Robin")
    photo_root.resizable(False, False)
    photo = PhotoImage(file="Theory/RR.png")
    photo_label = Label(photo_root, image=photo)
    photo_label.pack()
    photo_root.mainloop()


def seven():
    photo_root = Toplevel()
    photo_root.title("First Come First Serve")
    photo_root.resizable(False, False)
    photo = PhotoImage(file="Theory/FCFS.png")
    photo_label = Label(photo_root, image=photo)
    photo_label.pack()
    photo_root.mainloop()


def eight():
    photo_root = Toplevel()
    photo_root.title("Shortest Job First")
    photo_root.resizable(True, True)
    photo = PhotoImage(file="Theory/SJF.PNG")
    photo_label = Label(photo_root, image=photo)
    photo_label.pack()
    photo_root.mainloop()


# -----------------------------------------------------------------------------------------------------------------------
# Home Pag
Menu = Tk()

Menu.title("CPU Scheduling Theory")
Menu.overrideredirect(False)
Menu.geometry("800x750")
Menu.resizable(False, False)

L1 = Label(bg="black", text="CPU Scheduling Theory", fg="white", font=("Century Gothic", 35), width="900",
           height="1")
L1.pack()
f1 = Frame(bg="white").pack()
l1 = Label(text="Choose Theory: ", font=("Century Gothic", 15))
l1.pack(pady="40")
button7 = Button(f1, text="FCFS", borderwidth="0", bg="#e8e8e8", fg="green", font=("Century Gothic", 18),
                 activeforeground="black", activebackground="#bbbfca", command=seven).pack(padx=15)
button8 = Button(f1, text="SJF", borderwidth="0", bg="#e8e8e8", fg="green", font=("Century Gothic", 18),
                 activeforeground="black", activebackground="#bbbfca", command=eight).pack(pady=15)
button9 = Button(f1, text="RR", borderwidth="0", bg="#e8e8e8", fg="green", font=("Century Gothic", 18),
                 activeforeground="black", activebackground="#bbbfca", command=six).pack(pady=15)
button10 = Button(f1, text="HRRN", borderwidth="0", bg="#e8e8e8", fg="green", font=("Century Gothic", 18),
                  activeforeground="black", activebackground="#bbbfca", command=five).pack(pady=15)
button11 = Button(f1, text="LRRN", borderwidth="0", bg="#e8e8e8", fg="green", font=("Century Gothic", 18),
                  activeforeground="black", activebackground="#bbbfca", command=four).pack(pady=15)
button12 = Button(f1, text="SRTF", borderwidth="0", bg="#e8e8e8", fg="green", font=("Century Gothic", 18),
                  activeforeground="black", activebackground="#bbbfca", command=three).pack(pady=15)
Button9 = Button(f1, text="Back", borderwidth="0", bg="#e8e8e8", fg="green", font=("Century Gothic", 18),
                 activeforeground="black", activebackground="#bbbfca", command=Menu.destroy).pack(pady=15)
Menu.mainloop()
