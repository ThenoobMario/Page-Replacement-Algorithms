from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt


def FCFS(AT, BT):
    # all list of same size where same index represents qualities of one process
    CT = []  # Completion time or the time at which process is finished execution
    TAT = []  # CT - AT
    WT = []  # TAT - BT

    # To convert string type AT to int type
    AT = [int(i) for i in AT]
    BT = [int(i) for i in BT]

    timeCpu = 0

    yticks = []  # This is to store the bartick values
    ytickL = []  # This is to store the bartick lables

    barHeightVar = 1
    fig, gnt = plt.subplots()

    # Setting labels for x-axis and y-axis
    gnt.set_xlabel('Time')
    gnt.set_ylabel('Processes')

    for i in range(0, len(AT)):
        # to make up for idle CPU time
        while AT[i] > timeCpu:
            timeCpu += 1
        # Calculating CT by adding Current CPU time and BT

        storeThis = timeCpu  # This variable will store the starting time of the i'th process

        timeCpu += BT[i]
        CT.append(timeCpu)

        TAT.append(CT[i] - AT[i])
        WT.append(TAT[i] - BT[i])

        # print(AT[i], BT[i])
        gnt.broken_barh([(storeThis, BT[i])], (barHeightVar, 2), facecolors='tab:blue')   # here we want startingTime
        # of process (storeThis) + The time taken for the process (BT)

        yticks.append(
            barHeightVar + 1)  # thickness of bars is 2 and base starts at barHeightVar, so +1 will give us middle

        ytickL.append("P{}".format(i + 1))  # formatting to show P1,P2,P3...

        barHeightVar += 3  # thickness is 2 and extra 1 for spacing

    print(CT, TAT, WT)

    # Setting Y-axis limits 2 more than the list size
    gnt.set_ylim(0, (len(AT) + 2) * 3)

    # Setting X-axis limits last plus five
    gnt.set_xlim(0, CT[-1] + 5)

    # Setting ticks on y-axis
    gnt.set_yticks(yticks)

    # Labelling tickes of y-axis
    gnt.set_yticklabels(ytickL)
    plt.show()

    # variables for table: Process number-ytickL , AT, BT, CT, TAT , WT in the same order.
    # take the data

    class Table:

        def __init__(self, root):

            # code for creating table
            for i in range(total_rows):
                for j in range(total_columns):
                    self.e = Entry(root, width=10, fg='blue',
                                   font=('Arial', 16, 'bold'))

                    self.e.grid(row=i, column=j)
                    self.e.insert(END, lst[i][j])

    lst = [('PROCESS', 'AT', 'BT', 'CT', 'TAT', 'WT')]

    for i in range(0, len(AT)):
        lst.append([ytickL[i], AT[i], BT[i], CT[i], TAT[i], WT[i]])
        # (ytickL[0], AT[0], BT[0], CT[0], TAT[0], WT[0]),
        # (ytickL[1], AT[1], BT[1], CT[1], TAT[1], WT[1]),
        # (ytickL[2], AT[2], BT[2], CT[2], TAT[2], WT[2])]

    print(lst)

    # find total number of rows and
    # columns in list
    total_rows = len(lst)
    total_columns = len(lst[0])

    # create root window
    root = Tk()
    t = Table(root)
    root.mainloop()
    # variables for table: Process number-ytickL , AT, BT, CT, TAT , WT in the same order.

    # Python program to create a table


# ----------------------------------------------------------------------------------------------------------------------
# Main Page
Menu = Tk()
Menu.title("CPU scheduling Algorithms")
Menu.overrideredirect(False)
# Menu.iconbitmap("icon.ico")
Menu.geometry("800x750+0+0")
Menu.resizable(False, False)

L1 = Label(bg="black", text="CPU scheduling Algorithms", fg="white", font=("Century Gothic", 35), width="900",
           height="1").pack()

F1 = Frame(bg="white").pack()

L2 = Label(F1, text="Choose Algorithm:", font=("Century Gothic", 18)).pack(pady="15")

variable = StringVar()
variable.set("FCFS")  # default value
dropDown = OptionMenu(F1, variable, "FCFS", "SJF", "RR", "HRRN", "SRTF", "LRRN", "Priority")
dropDown.configure(borderwidth="0", width="12", bg="#e8e8e8", fg="green", font=("Century Gothic", 12),
                   activeforeground="black", activebackground="#bbbfca")
dropDown.pack(pady="5")

L3 = Label(F1, text="Enter The Arrival Time List", font=("Century Gothic", 18)).pack(pady="20")

# take input
ATList = Entry(F1, width="15", bg="#e8e8e8", fg="green", font=("Century Gothic", 15), bd="0", justify="center")
ATList.pack()

L4 = Label(F1, text="Enter The Burst Time List ", font=("Century Gothic", 18)).pack(pady="30")

# take input
BTList = Entry(F1, bg="#e8e8e8", fg="green", font=("Century Gothic", 15), bd="0", justify="center")
BTList.pack()

L5 = Button(F1, borderwidth="0", text="Visualise", bg="#e8e8e8", fg="green", font=("Century Gothic", 18),
            activeforeground="black", activebackground="#bbbfca",
            command=lambda: FCFS(ATList.get().split(" "), BTList.get().split(" "))).pack(pady="25")

L6 = Button(F1, borderwidth="0", text="Compare All Algorithms", bg="#e8e8e8", fg="green", font=("Century Gothic", 18),
            activeforeground="black", activebackground="#bbbfca").pack()
# command=lambda: graph(ATList.get(), BTList.get()))

L7 = Button(F1, borderwidth="0", text="Theory", bg="#e8e8e8", fg="green", font=("Century Gothic", 18),
            activeforeground="black", activebackground="#bbbfca").pack(pady="25")

L8 = Button(F1, borderwidth="0", text="Back", bg="#e8e8e8", fg="green", font=("Century Gothic", 18),
            activeforeground="black", activebackground="#bbbfca", command=Menu.destroy).pack()
Menu.mainloop()
