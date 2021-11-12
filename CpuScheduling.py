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

        yticks.append(barHeightVar + 1)  # thickness of bars is 2 and base starts at barHeightVar, so +1 will give us middle

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
    # Initialising time
    timeCpu = 0
    readyQ = []  # to check and store unfinished processes

    yticks = []  # This is to store the bartick values
    ytickL = []  # This is to store the bartick lables

    barHeightVar = 1
    fig, gnt = plt.subplots()

    # Setting labels for x-axis and y-axis
    gnt.set_xlabel('Time')
    gnt.set_ylabel('Processes')


    PID = [" " for i in AT]

    process = []

    CT = [0 for _ in AT]
    TAT = [0 for _ in AT]
    WT = [0 for _ in AT]

    AT = [int(i) for i in AT]
    BT = [int(i) for i in BT]

    # Making a list of Dictionaries
    for i in range(len(AT)):
        process.append({'PID': 'P{}'.format(i + 1), 'AT': AT[i], 'BT': BT[i]})

    # Checking if there are processes present
    while len(process) != 0 or len(readyQ) != 0:
        if len(readyQ) == 0:
            lenprocess = len(process)
            tempQ = []
            # entering all the processes that have arrived in the readyQ
            for x in range(0, lenprocess):
                if process[0]['AT'] <= timeCpu:
                    tempQ.append(process.pop(0))

            tempQ.sort(key=getBT)  # sorting acc to the burst time
            lengthQ = len(tempQ)
            for i in range(0, lengthQ):
                readyQ.append(tempQ.pop(0))  # adding the sorted queue to readyqueue

            # If Arrival time is greater than current CPU time (in current time no processes have arrived)
            if readyQ[0]['AT'] >= timeCpu:
                timeCpu = readyQ[0]['AT']  # then we make the timeCpu such that the 0th process has arrived

        # Getting the active process
        currProcess = readyQ.pop(0)

        timeCpu += currProcess['BT']

        lenprocess = len(process)
        tempQ = []
        # entering all the processes that have arrived in the readyQ
        for x in range(0, lenprocess):
            if process[0]['AT'] <= timeCpu:
                tempQ.append(process.pop(0))

        tempQ.sort(key=getBT)  # Sorting acc to the burst time
        lengthQ = len(tempQ)
        for i in range(0, lengthQ):
            readyQ.append(tempQ.pop(0))  # Adding the sorted queue to ready queue

        processnum = currProcess["PID"]

        finalNum = int(processnum[-1]) - 1
        CT[finalNum] = timeCpu
        PID[finalNum] = currProcess["PID"]
        TAT[finalNum] = CT[finalNum] - AT[finalNum]
        WT[finalNum] = TAT[finalNum] - BT[finalNum]
        print(readyQ)
        print(CT, TAT, WT)
    lst = [('PROCESS', 'AT', 'BT', 'CT', 'TAT', 'WT')]

    # Making a dataframe to sort the values based on processes
    outTable = pd.DataFrame({'PROCESS': PID, 'AT': AT, 'BT': BT, 'CT': CT,
                             'TAT': TAT, 'WT': WT})   

    PROCESS = list(outTable['PROCESS'])
    AT = list(outTable['AT'])
    BT = list(outTable['BT'])
    CT = list(outTable['CT'])
    TAT = list(outTable['TAT'])
    WT = list(outTable['WT'])

    for i in range(0, len(AT)):
        lst.append([PROCESS[i], AT[i], BT[i],
                    CT[i], TAT[i], WT[i]])  # to add all the values in a table

        # Since SJF is Non-Preemptive, we can use RT and WT interchangeably
        gnt.broken_barh([(WT[i] + AT[i], BT[i])], (barHeightVar, 2), facecolors='tab:blue')

        yticks.append(barHeightVar + 1)

        ytickL.append(PROCESS[i])

        barHeightVar += 3
    
    # Setting Y-axis limits 2 more than the list size
    gnt.set_ylim(0, (len(AT) + 2) * 3)

    # Setting X-axis limits last plus five
    gnt.set_xlim(0, CT[-1] + 5)

    # Setting ticks on y-axis
    gnt.set_yticks(yticks)

    # Labelling tickes of y-axis
    gnt.set_yticklabels(ytickL)
    
    # find total number of rows and
    # columns in list
    total_rows = len(lst)
    total_columns = len(lst[0])

    root = Tk()
    t = Table(root, total_rows, total_columns, lst)
    plt.show()
    root.mainloop()


def getBT(e):
    return e['BT']


def roundRobin(AT, BT, timeQ=2):
    # Initialising time
    timeCpu = 0
    readyQ = []  # to check and store unfinished processes
    processOrder = []

    yticks = []  # This is to store the bartick values
    ytickL = []  # This is to store the bartick lables

    barHeightVar = 1
    barHeightList = []

    # Loop to define the initial y-axis heights of the bars
    for i in range(len(AT)):
        if i == 0:
            barHeightList.append(1) 
        else:
            barHeightList.append(barHeightList[i - 1] + 3)

    fig, gnt = plt.subplots()

    # Setting labels for x-axis and y-axis
    gnt.set_xlabel('Time')
    gnt.set_ylabel('Processes')

    PID = [" " for i in AT]

    process = []

    CT = [0 for _ in AT]
    TAT = [0 for _ in AT]
    WT = [0 for _ in AT]

    AT = [int(i) for i in AT]
    BT = [int(i) for i in BT]

    for i in range(len(AT)):
        process.append({'PID': 'P{}'.format(i + 1), 'AT': AT[i], 'BT': BT[i]})

    # Checking if there are processes present
    while len(process) != 0 or len(readyQ) != 0:
        if len(readyQ) == 0:
            # Adding the first process in the ready queue
            readyQ.append(process.pop(0))

            # If Arrival time is greater than current CPU time (in current time no processes have arrived)
            if readyQ[0]['AT'] >= timeCpu:
                timeCpu = readyQ[0]['AT']

        # Getting the active process 
        currProcess = readyQ.pop(0)
        # If Burst Time is less than Time quantum
        if currProcess['BT'] <= timeQ:
            # Append the Process Name in an order list along with Start and Finish time
            processOrder.append({'Task': currProcess['PID'], 'Start' : timeCpu, 'Finish' : timeCpu + currProcess['BT']})

            timeCpu += currProcess['BT']
            currProcess['BT'] = 0
        else:
            processOrder.append({'Task': currProcess['PID'], 'Start' : timeCpu, 'Finish' : timeCpu + timeQ})

            timeCpu += timeQ
            currProcess['BT'] -= timeQ

        lenprocess = len(process)
        # getting all the arrived processes in the readyQ
        for x in range(0, lenprocess):
            if process[0]['AT'] <= timeCpu:
                readyQ.append(process.pop(0))

        # Appending the incomplete processes back to ready queue
        if currProcess['BT'] != 0:
            readyQ.append(currProcess)

        processnum = currProcess["PID"]

        finalNum = int(processnum[-1]) - 1
        CT[finalNum] = timeCpu
        PID[finalNum] = currProcess["PID"]
        TAT[finalNum] = CT[finalNum] - AT[finalNum]
        WT[finalNum] = TAT[finalNum] - BT[finalNum]

        print(readyQ)
        print(CT, TAT, WT)
    lst = [('PROCESS', 'AT', 'BT', 'CT', 'TAT', 'WT')]

    # Making a dataframe to sort the values based on processes
    outTable = pd.DataFrame({'PROCESS': PID, 'AT': AT, 'BT': BT, 'CT': CT,
                             'TAT': TAT, 'WT': WT})

    PROCESS = list(outTable['PROCESS'])
    AT = list(outTable['AT'])
    BT = list(outTable['BT'])
    CT = list(outTable['CT'])
    TAT = list(outTable['TAT'])
    WT = list(outTable['WT'])

    for i in range(0, len(AT)):
        lst.append([PROCESS[i], AT[i], BT[i],
                    CT[i], TAT[i], WT[i]])  # to add all the values in a table

        yticks.append(barHeightList[i] + 1)

        ytickL.append(PROCESS[i])

    # A loop to display the gantt chart visually 
    for i in range(1, len(processOrder) + 1):
        # Getting the number of the process
        P = processOrder[i - 1]['Task']
        pNo = int(P[-1]) - 1

        # If pNo is same, their height will be the same
        gnt.broken_barh([(processOrder[i - 1]['Start'], processOrder[i - 1]['Finish'] - processOrder[i - 1]['Start'])], 
                        (barHeightList[pNo], 2), facecolors = 'tab:blue')

    # Setting Y-axis limits 2 more than the list size
    gnt.set_ylim(0, (len(AT) + 2) * 3)

    # Setting X-axis limits last plus five
    gnt.set_xlim(0, CT[-1] + 5)

    # Setting ticks on y-axis
    gnt.set_yticks(yticks)

    # Labelling tickes of y-axis
    gnt.set_yticklabels(ytickL)
    
    # find total number of rows and
    # columns in list
    total_rows = len(lst)
    total_columns = len(lst[0])

    root = Tk()
    t = Table(root, total_rows, total_columns, lst)
    plt.show()
    root.mainloop()

def HRRN(AT, BT):
    # Initialising time
    timeCpu = 0
    readyQ = []  # to check and store unfinished processes

    yticks = []  # This is to store the bartick values
    ytickL = []  # This is to store the bartick lables

    barHeightVar = 1
    fig, gnt = plt.subplots()

    # Setting labels for x-axis and y-axis
    gnt.set_xlabel('Time')
    gnt.set_ylabel('Processes')

    PID = [" " for i in AT]

    process = []

    CT = [0 for _ in AT]
    TAT = [0 for _ in AT]
    WT = [0 for _ in AT]

    AT = [int(i) for i in AT]
    BT = [int(i) for i in BT]

    # Making a list of Dictionaries
    for i in range(len(AT)):
        process.append({'PID': 'P{}'.format(i + 1), 'AT': AT[i], 'BT': BT[i]})

    while len(process) != 0 or len(readyQ) != 0:
        if len(readyQ) == 0:
            lenprocess = len(process)
            tempQ = []
            # entering all the processes that have arrived in the readyQ
            for x in range(0, lenprocess):
                if process[0]['AT'] <= timeCpu:
                    tempQ.append(process.pop(0))
            
            lengthQ = len(tempQ)
            for i in range(0, lengthQ):
                readyQ.append(tempQ.pop(0))

            if readyQ[0]['AT'] > timeCpu:
                timeCpu = readyQ[0]['AT']

        currProcess = readyQ.pop(0)

        timeCpu += currProcess['BT']

        lenprocess = len(process)
        tempQ = []
        # entering all the processes that have arrived in the readyQ
        for x in range(0, lenprocess):
            if process[0]['AT'] <= timeCpu:
                tempQ.append(process.pop(0))
        
        HRR = ((timeCpu - readyQ[0]['AT']) + readyQ[0]['BT'])/readyQ[0]['BT']

        for i in range():
            responseRatio = ((timeCpu - readyQ[i]['AT']) + readyQ[i]['BT'])/readyQ[i]['BT']

            if responseRatio > HRR:
                HRR = responseRatio
                currProcess = readyQ.pop(i)

        
    

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
