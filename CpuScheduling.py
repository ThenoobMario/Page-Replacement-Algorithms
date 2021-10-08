from tkinter import *
import pandas as pd
import subprocess
import matplotlib.pyplot as plt

def theory():
    file1 = "python Theory.py"
    # os.system(file1)
    p = subprocess.Popen(file1, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()

# A class for creating Tables in the GUI
class Table:
    def __init__(self, root, total_rows, total_columns, lst):

        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root, width=10, fg='blue',
                                   font=('Centuary Gothic', 16, 'bold'))

                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])

def FCFS(AT, BT):
    # All list of same size where same index represents qualities of one process
    CT = []  # Completion time or the time at which process is finished execution
    TAT = []  # CT - AT
    WT = []  # TAT - BT

    # to sort all the list WRT AT

    # To convert string type AT to int type
    AT = [int(i) for i in AT]
    BT = [int(i) for i in BT]

    # Sorting Values of AT and BT
    inputTable = pd.DataFrame({'AT': AT, 'BT': BT})
    inputTable = inputTable.sort_values(by=['AT'])

    AT = list(inputTable['AT'])
    BT = list(inputTable['BT'])
    PID = inputTable.index  # Gets the index of the table

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
        gnt.broken_barh([(storeThis, BT[i])], (barHeightVar, 2), facecolors='tab:blue')  # here we want startingTime
        # of process (storeThis) + The time taken for the process (BT)

        yticks.append(
            barHeightVar + 1)  # thickness of bars is 2 and base starts at barHeightVar, so +1 will give us middle

        ytickL.append("P{}".format(PID[i] + 1))  # formatting to show P1,P2,P3...

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

    # plt.show()

    # variables for table: Process number-ytickL , AT, BT, CT, TAT , WT in the same order.
    lst = [('PROCESS', 'AT', 'BT', 'CT', 'TAT', 'WT')]

    # Making a dataframe to sort the values based on processes
    outTable = pd.DataFrame({'PROCESS': ytickL, 'AT': AT, 'BT': BT, 'CT': CT,
                             'TAT': TAT, 'WT': WT})

    outTable = outTable.sort_values(by=['PROCESS'])

    # Converting the columns to lists
    PROCESS = list(outTable['PROCESS'])
    AT = list(outTable['AT'])
    BT = list(outTable['BT'])
    CT = list(outTable['CT'])
    TAT = list(outTable['TAT'])
    WT = list(outTable['WT'])

    for i in range(0, len(AT)):
        lst.append([PROCESS[i], AT[i], BT[i],
                    CT[i], TAT[i], WT[i]])  # to add all the values in a table

    # find total number of rows and
    # columns in list
    total_rows = len(lst)
    total_columns = len(lst[0])

    # create root window
    root = Tk()
    t = Table(root, total_rows, total_columns, lst)
    plt.show()
    root.mainloop()


def SJF(AT, BT):
    # all list of same size where same index represents qualities of one process
    CT = []  # Completion time or the time at which process is finished execution
    TAT = []  # CT - AT
    WT = []  # TAT - BT

    # to sort all the list WRT AT

    # To convert string type AT to int type
    AT = [int(i) for i in AT]
    BT = [int(i) for i in BT]

    container = []

    # Sorting Values of AT and BT
    inputTable = pd.DataFrame({'AT': AT, 'BT': BT})
    PID = inputTable.index  # Gets the index of the table

    timeCpu = 0

    yticks = []  # This is to store the bartick values
    ytickL = []  # This is to store the bartick lables

    barHeightVar = 1
    fig, gnt = plt.subplots()

    # Setting labels for x-axis and y-axis
    gnt.set_xlabel('Time')
    gnt.set_ylabel('Processes')
    
    execList = AT

    for i in range(1, len(AT)):
        # to make up for idle CPU time
        while AT[i - 1] > timeCpu:
            timeCpu += 1

        firstCT = BT[i - 1]

        if AT[i - 1] == AT[i]:
            if BT[i - 1] >= BT[i]:
                continue
            else:
                firstCT = BT[i]
        # Calculating CT by adding Current CPU time and BT

        storeThis = timeCpu  # This variable will store the starting time of the i'th process

        timeCpu += BT[i]

        CT.append(timeCpu)

        TAT.append(CT[i] - AT[i])
        WT.append(TAT[i] - BT[i])

        # print(AT[i], BT[i])
        gnt.broken_barh([(storeThis, BT[i])], (barHeightVar, 2), facecolors='tab:blue')  # here we want startingTime
        # of process (storeThis) + The time taken for the process (BT)

        yticks.append(
            barHeightVar + 1)  # thickness of bars is 2 and base starts at barHeightVar, so +1 will give us middle

        ytickL.append("P{}".format(PID[i] + 1))  # formatting to show P1,P2,P3...

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

    lst = [('PROCESS', 'AT', 'BT', 'CT', 'TAT', 'WT')]

    # Making a dataframe to sort the values based on processes
    outTable = pd.DataFrame({'PROCESS': ytickL, 'AT': AT, 'BT': BT, 'CT': CT,
                             'TAT': TAT, 'WT': WT})

    outTable = outTable.sort_values(by=['PROCESS'])
    outTable = outTable.sort_values(by=['AT'])

    # Converting the columns to lists
    PROCESS = list(outTable['PROCESS'])
    AT = list(outTable['AT'])
    BT = list(outTable['BT'])
    CT = list(outTable['CT'])
    TAT = list(outTable['TAT'])
    WT = list(outTable['WT'])

    for i in range(0, len(AT)):
        lst.append([PROCESS[i], AT[i], BT[i],
                    CT[i], TAT[i], WT[i]])  # to add all the values in a table

    # find total number of rows and
    # columns in list
    total_rows = len(lst)
    total_columns = len(lst[0])

    # create root window
    root = Tk()
    t = Table(root, total_rows, total_columns, lst)
    plt.show()
    root.mainloop()

def roundRobin(AT, BT, timeQ = 2):
    # Initialising time
    timeCpu = 0
    readyQ = []
    finalQ = []

    process = []

    AT = [int(i) for i in AT]
    BT = [int(i) for i in BT]

    for i in range(len(AT)):
        process.append({'PID': 'P{}'.format(i + 1), 'AT': AT[i], 'BT': BT[i]})

    # Checkinng if there are processes present
    while len(process) != 0 or len(readyQ) != 0:
        if len(readyQ) == 0:
            # Adding the first process in the ready queue
            readyQ.append(process.pop(0))

            # If Arrival time is greater than current CPU time
            if readyQ[0]['AT'] >= timeCpu:
                timeCpu = readyQ[0]['AT']

        # Getting the active process 
        currProcess = readyQ.pop(0)
        # If Burst Time is less than Time quantum
        if currProcess['BT'] <= timeQ:
            timeCpu += currProcess['BT']
            currProcess['BT'] = 0
        else:
            timeCpu += timeQ
            currProcess['BT'] -= timeQ

        for x in process:
            if x['AT'] <= timeCpu:
                readyQ.append(process.pop(0))

        # Appending all the incomplete processes back to ready queue
        if currProcess['BT'] != 0:
            readyQ.append(currProcess)

        print(readyQ)

def Visualise(option, AT, BT):
    if option == "FCFS":
        FCFS(AT, BT)
    elif option == "SJF":
        SJF(AT, BT)
    elif option == "RR":
        roundRobin(AT, BT, 2)
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
            command=lambda: Visualise(variable.get(), ATList.get().split(" "), BTList.get().split(" "))).pack(pady="25")

L6 = Button(F1, borderwidth="0", text="Compare All Algorithms", bg="#e8e8e8", fg="green", font=("Century Gothic", 18),
            activeforeground="black", activebackground="#bbbfca").pack()
# command=lambda: graph(ATList.get(), BTList.get()))

L7 = Button(F1, borderwidth="0", text="Theory", bg="#e8e8e8", fg="green", font=("Century Gothic", 18),
            activeforeground="black", activebackground="#bbbfca", command=theory).pack(pady="25")

L8 = Button(F1, borderwidth="0", text="Back", bg="#e8e8e8", fg="green", font=("Century Gothic", 18),
            activeforeground="black", activebackground="#bbbfca", command=Menu.destroy).pack()
Menu.mainloop()
