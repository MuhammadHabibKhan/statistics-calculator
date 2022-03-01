# main window
import tkinter as tk
from tkinter import ttk
import math

window = tk.Tk()
window.geometry('1000x600')
window.resizable(False, False)
window.title('Statistics Calculator')

# frames
frame1 = tk.Frame(master=window, width=500, height=600, borderwidth=5, relief='groove', bg='light yellow')
frame2 = tk.Frame(master=window, width=500, height=600, borderwidth=5, relief='groove', bg='light yellow')
tk.Label(master=frame1, text="Select Function to Calculate", bg='light yellow').place(x=10, y=10)

# Combobox
style = ttk.Style()
style.theme_use('alt')
c_var = tk.StringVar()
style.configure("TCombobox", fieldbackground="light green", background="teal")
combo = ttk.Combobox(frame1, style='TCombobox', width=32, textvariable=c_var)
combo['values'] = ('Select', 'Mean', 'Median', 'Mode',
                   'Quartile', 'Deciles', 'Percentile', 'Standard Deviation', 'Variance',
                   'Coefficient Of Variance', 'Range', 'Coefficient Of Range', 'Mean deviation about mean',
                   'Mean deviation about median', 'Coefficient of Mean Deviation about Mean',
                   'Coefficient of Mean Deviation about Median', 'Quartile Deviation',
                   'Coefficient of Quartile Deviation', 'Grouped Range', 'Grouped Mean',
                   'Coefficient of Grouped Range', 'Grouped Median', "Grouped Mode", 'Grouped Standard Deviation',
                   'Grouped Variance', 'Grouped Coefficient of Variation', 'Grouped Quartile',
                   'Grouped Quartile Deviation', 'Coefficient of Grouped Quartile Deviation', 'Grouped Deciles',
                   'Grouped Percentiles', 'Grouped Mean Deviation about Mean',
                   'Coefficient of Grouped Mean Deviation about Mean', 'Grouped Mean Deviation about Median',
                   'Coefficient of Grouped Mean Deviation about Median')
combo['state'] = 'normal'
combo.current(0)
combo.place(x=10, y=35)

# 1st Label
tk.Label(frame1, text="Enter Discrete Data", bg='light yellow').place(x=10, y=70)
# 1st Entry
ent_data_var = tk.IntVar()
ent_data = tk.Entry(frame1, width=33, bg='light grey', state='normal', textvariable=ent_data_var)
ent_data.place(x=10, y=90)
ent_data.focus()

# 2nd Label
tk.Label(frame1, text="Enter Lower Class Boundaries", bg='light yellow').place(x=10, y=120)
# 2nd Entry
ent_LCB_var = tk.IntVar()
ent_LCB = tk.Entry(frame1, width=33, bg='light grey', state='normal', textvariable=ent_LCB_var)
ent_LCB.place(x=10, y=140)

# 3rd Label
tk.Label(frame1, text="Enter Upper Class Boundaries", bg='light yellow').place(x=10, y=170)
# 3rd Entry
ent_UCB_var = tk.IntVar()
ent_UCB = tk.Entry(frame1, width=33, bg='light grey', state='normal', textvariable=ent_UCB_var)
ent_UCB.place(x=10, y=190)

# 4th Label
tk.Label(frame1, text="Enter Frequency", bg='light yellow').place(x=10, y=220)
# 4th Entry
ent_Freq_var = tk.IntVar()
ent_Freq = tk.Entry(frame1, width=33, bg='light grey', state='normal', textvariable=ent_Freq_var)
ent_Freq.place(x=10, y=240)

# model
# n_var = tk.IntVar()
# n_ent = tk.Entry(frame1, bg='light grey', text variable = n_var)
# n_ent.place(x=10, y=350)
# n = n_ent.get()


def clicked():
    # range
    if c_var.get() == 'Range':
        tbox.delete("1.0", tk.END)  # for clearing the already filled output from previous selection
        tbox.insert("1.0", "Given Data:  " + ent_data.get())
        tbox.insert("2.0", "\n")
        tbox.insert("3.0", "\n")
        tbox.insert("3.0", "Range: ")
        while True:
            try:
                x = list(map(float, ent_data.get().split(",")))
                tbox.insert("3.8", max(x)-min(x))
                break
            except ValueError:
                import tkinter.messagebox
                tk.messagebox.showwarning(title='Wrong Format', message='Please use comma separator')
                break

    # coefficient of range
    elif c_var.get() == 'Coefficient Of Range':
        tbox.delete("1.0", tk.END)  # for clearing the already filled output from previous selection
        tbox.insert("1.0", "Given Data:  " + ent_data.get())
        tbox.insert("2.0", "\n")
        tbox.insert("3.0", "\n")
        tbox.insert("3.0", "Coefficient Of Range: ")
        while True:
            try:
                x = list(map(float, ent_data.get().split(",")))
                tbox.insert("3.25", (max(x)-min(x))/(max(x)+min(x)))
                break
            except ValueError:
                import tkinter.messagebox
                tk.messagebox.showwarning(title='Wrong Format', message='Please use comma separator')
                break

    # Standard Deviation
    elif c_var.get() == 'Standard Deviation':
        tbox.delete("1.0", tk.END)
        tbox.insert("1.0", "Given Data:  " + ent_data.get())
        tbox.insert("2.0", "\n")
        tbox.insert("3.0", "\n")
        tbox.insert("3.0", "Standard Deviation: ")
        while True:
            try:
                x = list(map(float, ent_data.get().split(",")))
                n = len(x)
                sum_f = sum(x)
                m = []
                mean = (sum_f/n)
                m.append(mean)
                i = 0
                Y = []
                while i < n:
                    h = [x][0][i]
                    y = (h-mean)**2
                    Y.append(y)
                    i += 1

                sd = math.sqrt(sum(Y)/n)
                tbox.insert("3.30", sd)
                break
            except ValueError:
                import tkinter.messagebox
                tk.messagebox.showwarning(title='Wrong Format', message='Please use comma separator')
                break
                                
    # variance
    elif c_var.get() == 'Variance':
        tbox.delete("1.0", tk.END)
        tbox.insert("1.0", "Given Data:  " + ent_data.get())
        tbox.insert("2.0", "\n")
        tbox.insert("3.0", "\n")
        tbox.insert("3.0", "Variance: ")
        while True:
            try:
                x = list(map(float, ent_data.get().split(",")))
                n = len(x)
                sum_f = sum(x)
                m = []
                mean = (sum_f/n)
                m.append(mean)
                i = 0
                Y = []
                while i < n:
                    h = [x][0][i]
                    y = (h-mean)**2
                    Y.append(y)
                    i += 1

                v = (sum(Y)/n)
                tbox.insert("3.30", v)
                break
            except ValueError:
                import tkinter.messagebox
                tk.messagebox.showwarning(title='Wrong Format', message='Please use comma separator')
                break

    # coefficient of variance
    elif c_var.get() == 'Coefficient Of Variance':
        tbox.delete("1.0", tk.END)
        tbox.insert("1.0", "Given Data:  " + ent_data.get())
        tbox.insert("2.0", "\n")
        tbox.insert("3.0", "\n")
        tbox.insert("3.0", "Coefficient Of Variance: ")
        while True:
            try:
                x = list(map(float, ent_data.get().split(",")))
                n = len(x)
                sum_f = sum(x)
                m = []
                mean = (sum_f/n)
                m.append(mean)
                i = 0
                Y = []
                while i < n:
                    h = [x][0][i]
                    y = (h-mean)**2
                    Y.append(y)
                    i += 1

                sd = math.sqrt((sum(Y)/n))
                cvr = sd/mean
                tbox.insert("3.30", cvr)
                break
            except ValueError:
                import tkinter.messagebox
                tk.messagebox.showwarning(title='Wrong Format', message='Please use comma separator')
                break  

# Mean

    # Mean
    elif c_var.get() == 'Mean':
        tbox.delete("1.0", tk.END) # for clearing the already filled output from previous selection
        tbox.insert("1.0", "Given Data:  " + ent_data.get())
        tbox.insert("2.0", "\n")
        tbox.insert("3.0", "\n")
        tbox.insert("3.0", "Mean: ")
        while True:
            try:
                x = list(map(float, ent_data.get().split(",")))
                s = sum(x)
                n = len(x)
                tbox.insert("3.8", s/n)
                break
            except ValueError:
                import tkinter.messagebox
                tk.messagebox.showwarning(title='Wrong Format', message='Please use comma separator')
                break

    # median
    elif c_var.get() == 'Median':
        tbox.delete("1.0", tk.END) # for clearing the already filled output from previous selection
        tbox.insert("1.0", "Given Data:  " + ent_data.get())
        tbox.insert("2.0", "\n")
        tbox.insert("3.0", "\n")
        tbox.insert("3.0", "Median: ")
        while True:
            try:
                x = list(map(float, ent_data.get().split(",")))

                # implication of selection sort algorithm

                j = 0  # for different ranges so we have to change only one line of code
                n = len(x)  # gives length of the list
                while j < n:  # condition for loop using index as it starts from 0
                    s = x[j] # jth value from the list, which will continue till length of list
                    p = j  # for the last value so it swaps it with itself
                    i = j+1 # i will be the number that comes after j which will be tested if its smaller than jth value
                    # or the previous s and if not then it keeps the loop until it finds one
                    while i < n:  # will execute under the same condition as above
                        if x[i] < s:  # we search for a number less than our starting point e.g we first define 0th
                            # index the smallest then using inequality we look for lesser no.
                            s = x[i]  # the lowest number goes into our s variable for smallest number
                            p = i
                        i += 1
                    x[j], x[p] = x[p], x[j]
                    j += 1
                r = n % 2
                if r > 0:
                    median_index = (n + 1)/2
                    median = x[int(median_index-1)]
                    tbox.insert("3.10", median)
                else:
                    median_index = (n + 1)/2
                    median_floor = int(math.floor(median_index))
                    median = x[(median_floor-1)] + x[median_floor]
                    tbox.insert("3.10", (median/2))
                break
            except ValueError:
                import tkinter.messagebox
                tk.messagebox.showwarning(title='Wrong Format', message='Please use comma separator')
                break

    # mode
    # for uni-modal dataset only
    elif c_var.get() == 'Mode':
        tbox.delete("1.0", tk.END) # for clearing the already filled output from previous selection
        tbox.insert("1.0", "Given Data:  " + ent_data.get())
        tbox.insert("2.0", "\n")
        tbox.insert("3.0", "\n")
        tbox.insert("3.0", "Mode: ")
        while True:
            try:
                x = list(map(float, ent_data.get().split(",")))
                mode = max(x, key=x.count)
                tbox.insert("3.8", mode)
                break
            except ValueError:
                import tkinter.messagebox
                tk.messagebox.showwarning(title='Wrong Format', message='Please use comma separator')
                break

    # mean deviation about mean
    elif c_var.get() == 'Mean deviation about mean':
        tbox.delete("1.0", tk.END) # for clearing the already filled output from previous selection
        tbox.insert("1.0", "Given Data:  " + ent_data.get())
        tbox.insert("2.0", "\n")
        tbox.insert("3.0", "\n")
        tbox.insert("3.0", "Mean deviation about mean: ")
        while True:
            try:
                x = list(map(float, ent_data.get().split(",")))
                s = sum(x)
                n = len(x)
                mean = s/n
                i = 0
                p = []
                while i < n:
                    y = x[i]
                    md_r = abs(y - mean)
                    p.append(md_r)
                    i += 1
                md = sum(p)
                tbox.insert("3.28", md/n)
                break
            except ValueError:
                import tkinter.messagebox
                tk.messagebox.showwarning(title='Wrong Format', message='Please use comma separator')
                break

    # mean deviation about median
    elif c_var.get() == 'Mean deviation about median':
        tbox.delete("1.0", tk.END) # for clearing the already filled output from previous selection
        tbox.insert("1.0", "Given Data:  " + ent_data.get())
        tbox.insert("2.0", "\n")
        tbox.insert("3.0", "\n")
        tbox.insert("3.0", "Mean deviation about median: ")
        while True:
            try:
                x = list(map(float, ent_data.get().split(",")))

                # implication of selection sort algorithm

                j = 0  # for different ranges so we have to change only one line of code
                n = len(x)  # gives length of the list
                while j < n:  # condition for loop using index as it starts from 0
                    s = x[j] # jth value from the list, which will continue till length of list
                    p = j  # for the last value so it swaps it with itself
                    i = j+1 # i will be the number that comes after j which will be tested if its smaller than jth value
                    # or the previous s and if not then it keeps the loop until it finds one
                    while i < n:  # will execute under the same condition as above
                        if x[i] < s:  # we search for a number less than our starting point e.g we first define 0th
                            # index the smallest then using inequality we look for lesser no.
                            s = x[i]  # the lowest number goes into our s variable for smallest number
                            p = i
                        i += 1
                    x[j], x[p] = x[p], x[j]
                    j += 1
                r = n % 2
                if r > 0:
                    median_index = (n + 1)/2
                    median = x[int(median_index-1)]
                    i = 0
                    p = []
                    while i < n:
                        y = x[i]
                        md_r = abs(y - median)
                        p.append(md_r)
                        i += 1
                    md = sum(p)
                    tbox.insert("3.33", md/n)
                else:
                    median_index = (n + 1)/2
                    median_floor = int(math.floor(median_index))
                    median_r = x[(median_floor-1)] + x[median_floor]
                    median = median_r/2
                    i = 0
                    w = []
                    while i < n:
                        y = x[i]
                        md_r = abs(y - median)
                        w.append(md_r)
                        i += 1
                    md = sum(w)
                    tbox.insert("3.33", (md/n))
                break
            except ValueError:
                import tkinter.messagebox
                tk.messagebox.showwarning(title='Wrong Format', message='Please use comma separator')
                break

    # coefficient of mean deviation about mean
    elif c_var.get() == 'Coefficient of Mean Deviation about Mean':
        tbox.delete("1.0", tk.END) # for clearing the already filled output from previous selection
        tbox.insert("1.0", "Given Data:  " + ent_data.get())
        tbox.insert("2.0", "\n")
        tbox.insert("3.0", "\n")
        tbox.insert("3.0", "Coefficient of Mean Deviation about Mean: ")
        while True:
            try:
                x = list(map(float, ent_data.get().split(",")))
                s = sum(x)
                n = len(x)
                mean = s/n
                i = 0
                p = []
                while i < n:
                    y = x[i]
                    md_r = abs(y - mean)
                    p.append(md_r)
                    i += 1
                md = sum(p)/n
                tbox.insert("3.46", md/mean)
                break
            except ValueError:
                import tkinter.messagebox
                tk.messagebox.showwarning(title='Wrong Format', message='Please use comma separator')
                break

    # coefficient of mean deviation about median
    elif c_var.get() == 'Coefficient of Mean Deviation about Median':
        tbox.delete("1.0", tk.END) # for clearing the already filled output from previous selection
        tbox.insert("1.0", "Given Data:  " + ent_data.get())
        tbox.insert("2.0", "\n")
        tbox.insert("3.0", "\n")
        tbox.insert("3.0", "Coefficient of Mean Deviation about Median: ")
        while True:
            try:
                x = list(map(float, ent_data.get().split(",")))

                # implication of selection sort algorithm

                j = 0  # for different ranges so we have to change only one line of code
                n = len(x)  # gives length of the list
                while j < n:  # condition for loop using index as it starts from 0
                    s = x[j]  # jth value from the list, which will continue till length of list
                    p = j  # for the last value so it swaps it with itself
                    i = j+1 # i will be the number that comes after j which will be tested if its smaller than jth value
                    # or the previous s and if not then it keeps the loop until it finds one
                    while i < n:  # will execute under the same condition as above
                        if x[i] < s:  # we search for a number less than our starting point e.g we first define 0th
                            # index the smallest then using inequality we look for lesser no.
                            s = x[i]  # the lowest number goes into our s variable for smallest number
                            p = i
                        i += 1
                    x[j], x[p] = x[p], x[j]
                    j += 1
                r = n % 2
                if r > 0:
                    median_index = (n + 1)/2
                    median = x[int(median_index-1)]
                    i = 0
                    p = []
                    while i < n:
                        y = x[i]
                        md_r = abs(y - median)
                        p.append(md_r)
                        i += 1
                    md = sum(p)/n
                    tbox.insert("3.50", md/median)
                else:
                    median_index = (n + 1)/2
                    median_floor = int(math.floor(median_index))
                    median_r = x[(median_floor-1)] + x[median_floor]
                    median = median_r/2
                    i = 0
                    w = []
                    while i < n:
                        y = x[i]
                        md_r = abs(y - median)
                        w.append(md_r)
                        i += 1
                    md = sum(w)/n
                    tbox.insert("3.50", (md/median))
                break
            except ValueError:
                import tkinter.messagebox
                tk.messagebox.showwarning(title='Wrong Format', message='Please use comma separator')
                break

    # quartile
    elif c_var.get() == 'Quartile':
        tbox.delete("1.0", tk.END) # for clearing the already filled output from previous selection
        tbox.insert("1.0", "Given Data:  " + ent_data.get())
        tbox.insert("2.0", "\n")
        tbox.insert("3.0", "\n")
        tbox.insert("3.0", "Quartile: ")
        while True:
            try:
                x = list(map(float, ent_data.get().split(",")))

                # implication of selection sort algorithm
                j = 0  # for different ranges so we have to change only one line of code
                n = len(x)  # gives length of the list
                while j < n:  # condition for loop using index as it starts from 0
                    s = x[j]  # jth value from the list, which will continue till length of list
                    p = j  # for the last value so it swaps it with itself
                    i = j+1 # i will be the number that comes after j which will be tested if its smaller than jth value
                    # or the previous s and if not then it keeps the loop until it finds one
                    while i < n:  # will execute under the same condition as above
                        if x[i] < s:  # we search for a number less than our starting point e.g we first define 0th
                            # index the smallest then using inequality we look for lesser no.
                            s = x[i]  # the lowest number goes into our s variable for smallest number
                            p = i
                        i += 1
                    x[j], x[p] = x[p], x[j]
                    j += 1
                r = n % 2
                if r > 0:
                    i = 1
                    q = []
                    while i < 4:
                        quartile_f = i*(n+1)/4
                        q_round = round(quartile_f)
                        diff = abs(q_round - quartile_f)
                        if diff == 0:
                            quartile = x[int(quartile_f - 1)]
                            q.append(quartile)
                        else:
                            quartile_floor = math.floor(quartile_f)
                            decimal_value = quartile_f - quartile_floor
                            m1 = x[quartile_floor-1]
                            m2 = x[quartile_floor]
                            quartile = m1 + (decimal_value*(m2-m1))   # interpolation
                            q.append(quartile)
                        i += 1
                    tbox.insert("3.15", 'Q1: ')
                    tbox.insert("3.20", q[0])
                    tbox.insert("4.0", "\n")
                    tbox.insert("4.15", 'Q2: ')
                    tbox.insert("4.20", q[1])
                    tbox.insert("5.0", "\n")
                    tbox.insert("5.15", 'Q3: ')
                    tbox.insert("5.20", q[2])
                else:
                    half = int(n/2)
                    set_left = x[:half]
                    set_right = x[half:]
                    quartile_f = (half+1)/2
                    q_round = round(quartile_f)
                    diff = abs(quartile_f - q_round)
                    if diff == 0:
                        q1 = set_left[int(quartile_f-1)]
                        q3 = set_right[int(quartile_f-1)]
                        tbox.insert("3.15", 'Q1: ')
                        tbox.insert("3.20", q1)
                        tbox.insert("5.0", "\n")
                        tbox.insert("5.15", 'Q3: ')
                        tbox.insert("5.20", q3)
                    else:
                        q1x = set_left[int(math.floor(quartile_f-1))]
                        q3x = set_right[int(math.floor(quartile_f-1))]
                        q11x = set_left[int(math.floor(quartile_f))]
                        q33x = set_right[int(math.floor(quartile_f))]
                        q1 = (q1x+q11x)/2
                        q3 = (q3x+q33x)/2
                        tbox.insert("3.15", 'Q1: ')
                        tbox.insert("3.20", q1)
                        tbox.insert("5.0", "\n")
                        tbox.insert("5.15", 'Q3: ')
                        tbox.insert("5.20", q3)
                    q2_f = (n+1)/2
                    q2_floor = math.floor(q2_f)
                    q2_r1 = x[q2_floor-1]
                    q2_r2 = x[q2_floor]
                    q2 = (q2_r1+q2_r2)/2
                    tbox.insert("4.0", "\n")
                    tbox.insert("4.15", 'Q2: ')
                    tbox.insert("4.20", q2)
                break
            except ValueError:
                import tkinter.messagebox
                tk.messagebox.showwarning(title='Wrong Format', message='Please use comma separator')
                break

    # percentile
    elif c_var.get() == 'Percentile':
        tbox.delete("1.0", tk.END) # for clearing the already filled output from previous selection
        tbox.insert("1.0", "Given Data:  " + ent_data.get())
        tbox.insert("2.0", "\n")
        tbox.insert("3.0", "\n")
        tbox.insert("3.0", "Percentile: ")
        tbox.insert("4.0", "\n")
        while True:
            try:
                x = list(map(float, ent_data.get().split(",")))
                x = sorted(x)
                n = len(x)
                i = 1
                per = []
                while i < 101:
                    k = i/100
                    if k != 1/(n+1):
                        p = ((i*(n-1))/100)+1
                        z = math.floor(p)
                        s = p-z
                        if s == 0:
                            j = x[int(p-1)]
                            per.append(j)
                            # tbox.insert(3.13, per)
                        else:
                            Y = math.floor(p)
                            fraction = p-Y
                            j = x[Y-1]
                            j2 = x[Y]
                            qx1 = fraction*(abs(j2-j))
                            qx = qx1+j
                            per.append(qx)
                            # tbox.insert(3.13, per)
                    else:
                        p = i*(n+1)/100
                        r = k % (1/(n+1))
                        if r == 0:  # if multiple then no interpolation needed
                            j = x[int(p)]
                            per.append(j)
                            # tbox.insert(3.13, j)
                        else:
                            Y = math.floor(p)
                            fraction = p-Y
                            j = x[Y-1]
                            j2 = x[Y]
                            qx1 = fraction*(abs(j2-j))
                            qx = qx1+j
                            per.append(qx)
                            # tbox.insert(3.13, qx)
                    i += 1
                a = 0
                while a < 100:
                    tbox.insert(106.0, str('P'))
                    tbox.insert(106.0, a+1)
                    tbox.insert(106.0, ": ")
                    tbox.insert(106.0, per[a])
                    tbox.insert(106.0, "\n")
                    a += 1
                break
            except ValueError:
                import tkinter.messagebox
                tk.messagebox.showwarning(title='Wrong Format', message='Please use comma separator')
                break

    # Deciles
    elif c_var.get() == 'Deciles':
        tbox.delete("1.0", tk.END) # for clearing the already filled output from previous selection
        tbox.insert("1.0", "Given Data:  " + ent_data.get())
        tbox.insert("2.0", "\n")
        tbox.insert("3.0", "\n")
        tbox.insert("3.0", "Deciles: ")
        tbox.insert("4.0", "\n")
        while True:
            try:
                x = list(map(float, ent_data.get().split(",")))
                x = sorted(x)
                n = len(x)
                i = 1
                per = []
                while i < 10:
                    p = i*((n+1)/10)
                    z = math.floor(p)
                    s = p-z
                    if s == 0:
                        j = x[int(p-1)]
                        per.append(j)
                        # tbox.insert(3.13, per)
                    else:
                        Y = math.floor(p)
                        if Y == 0:
                            fraction = p
                            j2 = x[Y]
                            qx1 = fraction*j2
                            qx = qx1
                            per.append(qx)
                        else:
                            fraction = p-Y
                            j = x[Y-1]
                            if Y == n:
                                qx1 = fraction*(0-j)
                                qx = qx1+j
                                per.append(qx)                                
                            else:
                                j2 = x[Y]
                                qx1 = fraction*(abs(j2-j))
                                qx = qx1+j
                                per.append(qx)
                            # tbox.insert(3.13, per)
                    i += 1
                a = 0
                while a < 9:
                    tbox.insert(20.0, str('D'))
                    tbox.insert(20.0, a+1)
                    tbox.insert(20.0, ": ")
                    tbox.insert(20.0, per[a])
                    tbox.insert(20.0, "\n")
                    a += 1
                break
            except ValueError:
                import tkinter.messagebox
                tk.messagebox.showwarning(title='Wrong Format', message='Please use comma separator')
                break
    
    # Quartile Deviation
    elif c_var.get() == 'Quartile Deviation':
        tbox.delete("1.0", tk.END)  # for clearing the already filled output from previous selection
        tbox.insert("1.0", "Given Data:  " + ent_data.get())
        tbox.insert("2.0", "\n")
        tbox.insert("3.0", "\n")
        tbox.insert("3.0", "Quartile Deviation: ")
        while True:
            try:
                x = list(map(float, ent_data.get().split(",")))

                # implication of selection sort algorithm
                j = 0  # for different ranges so we have to change only one line of code
                n = len(x)  # gives length of the list
                while j < n:  # condition for loop using index as it starts from 0
                    s = x[j]  # jth value from the list, which will continue till length of list
                    p = j  # for the last value so it swaps it with itself
                    i = j+1 # i will be the number that comes after j which will be tested if its smaller than jth value
                    # or the previous s and if not then it keeps the loop until it finds one
                    while i < n:  # will execute under the same condition as above
                        if x[i] < s:  # we search for a number less than our starting point e.g we first define 0th
                            # index the smallest then using inequality we look for lesser no.
                            s = x[i]  # the lowest number goes into our s variable for smallest number
                            p = i
                        i += 1
                    x[j], x[p] = x[p], x[j]
                    j += 1
                r = n % 2
                if r > 0:
                    i = 1
                    q = []
                    while i < 4:
                        quartile_f = i*(n+1)/4
                        q_round = round(quartile_f)
                        diff = abs(q_round - quartile_f)
                        if diff == 0:
                            quartile = x[int(quartile_f - 1)]
                            q.append(quartile)
                        else:
                            quartile_floor = math.floor(quartile_f)
                            decimal_value = quartile_f - quartile_floor
                            m1 = x[quartile_floor-1]
                            m2 = x[quartile_floor]
                            quartile = m1 + (decimal_value*(m2-m1))   # interpolation
                            q.append(quartile)
                        i += 1
                    tbox.insert("3.27", 'QD : ')
                    tbox.insert("3.33", (q[2]-q[0])/2)
                    # tbox.insert("4.0", "\n")
                    # tbox.insert("4.15", 'Q2: ')
                    # tbox.insert("4.20", q[1])
                    # tbox.insert("5.0", "\n")
                    # tbox.insert("5.15", 'Q3: ')
                    # tbox.insert("5.20", q[2])
                else:
                    half = int(n/2)
                    set_left = x[:half]
                    set_right = x[half:]
                    quartile_f = (half+1)/2
                    q_round = round(quartile_f)
                    diff = abs(quartile_f - q_round)
                    if diff == 0:
                        q1 = set_left[int(quartile_f-1)]
                        q3 = set_right[int(quartile_f-1)]
                        tbox.insert("3.27", 'QD : ')
                        tbox.insert("3.33", (q3-q1)/2)
                        # tbox.insert("5.0", "\n")
                        # tbox.insert("5.15", 'Q3: ')
                        # tbox.insert("5.20", q3)
                    else:
                        q1x = set_left[int(math.floor(quartile_f-1))]
                        q3x = set_right[int(math.floor(quartile_f-1))]
                        q11x = set_left[int(math.floor(quartile_f))]
                        q33x = set_right[int(math.floor(quartile_f))]
                        q1 = (q1x+q11x)/2
                        q3 = (q3x+q33x)/2
                        tbox.insert("3.27", 'QD : ')
                        tbox.insert("3.33", (q3-q1)/2)
                        # tbox.insert("5.0", "\n")
                        # tbox.insert("5.15", 'Q3: ')
                        # tbox.insert("5.20", q3)
                    # q2_f = (n+1)/2
                    # q2_floor = math.floor(q2_f)
                    # q2_r1 = x[q2_floor-1]
                    # q2_r2 = x[q2_floor]
                    # q2 = (q2_r1+q2_r2)/2
                    # tbox.insert("4.0", "\n")
                    # tbox.insert("4.15", 'Q2: ')
                    # tbox.insert("4.20", q2)
                break
            except ValueError:
                import tkinter.messagebox
                tk.messagebox.showwarning(title='Wrong Format', message='Please use comma separator')
                break

    # Coefficient of Quartile Deviation
    elif c_var.get() == 'Coefficient of Quartile Deviation':
        tbox.delete("1.0", tk.END)  # for clearing the already filled output from previous selection
        tbox.insert("1.0", "Given Data:  " + ent_data.get())
        tbox.insert("2.0", "\n")
        tbox.insert("3.0", "\n")
        tbox.insert("3.0", "Coefficient of Quartile Deviation: ")
        while True:
            try:
                x = list(map(float, ent_data.get().split(",")))

                # implication of selection sort algorithm
                j = 0  # for different ranges so we have to change only one line of code
                n = len(x)  # gives length of the list
                while j < n:  # condition for loop using index as it starts from 0
                    s = x[j]  # jth value from the list, which will continue till length of list
                    p = j  # for the last value so it swaps it with itself
                    i = j+1 # i will be the number that comes after j which will be tested if its smaller than jth value
                    # or the previous s and if not then it keeps the loop until it finds one
                    while i < n:  # will execute under the same condition as above
                        if x[i] < s:  # we search for a number less than our starting point e.g we first define 0th
                            # index the smallest then using inequality we look for lesser no.
                            s = x[i]  # the lowest number goes into our s variable for smallest number
                            p = i
                        i += 1
                    x[j], x[p] = x[p], x[j]
                    j += 1
                r = n % 2
                if r > 0:
                    i = 1
                    q = []
                    while i < 4:
                        quartile_f = i*(n+1)/4
                        q_round = round(quartile_f)
                        diff = abs(q_round - quartile_f)
                        if diff == 0:
                            quartile = x[int(quartile_f - 1)]
                            q.append(quartile)
                        else:
                            quartile_floor = math.floor(quartile_f)
                            decimal_value = quartile_f - quartile_floor
                            m1 = x[quartile_floor-1]
                            m2 = x[quartile_floor]
                            quartile = m1 + (decimal_value*(m2-m1))   # interpolation
                            q.append(quartile)
                        i += 1
                    tbox.insert("3.43", 'QD : ')
                    tbox.insert("3.48", (q[2]-q[0])/(q[2]+q[0]))
                    # tbox.insert("4.0", "\n")
                    # tbox.insert("4.15", 'Q2: ')
                    # tbox.insert("4.20", q[1])
                    # tbox.insert("5.0", "\n")
                    # tbox.insert("5.15", 'Q3: ')
                    # tbox.insert("5.20", q[2])
                else:
                    half = int(n/2)
                    set_left = x[:half]
                    set_right = x[half:]
                    quartile_f = (half+1)/2
                    q_round = round(quartile_f)
                    diff = abs(quartile_f - q_round)
                    if diff == 0:
                        q1 = set_left[int(quartile_f-1)]
                        q3 = set_right[int(quartile_f-1)]
                        tbox.insert("3.43", 'QD : ')
                        tbox.insert("3.48", (q3-q1)/(q3+q1))
                        # tbox.insert("5.0", "\n")
                        # tbox.insert("5.15", 'Q3: ')
                        # tbox.insert("5.20", q3)
                    else:
                        q1x = set_left[int(math.floor(quartile_f-1))]
                        q3x = set_right[int(math.floor(quartile_f-1))]
                        q11x = set_left[int(math.floor(quartile_f))]
                        q33x = set_right[int(math.floor(quartile_f))]
                        q1 = (q1x+q11x)/2
                        q3 = (q3x+q33x)/2
                        tbox.insert("3.43", 'QD : ')
                        tbox.insert("3.48", (q3-q1)/(q3+q1))
                        # tbox.insert("5.0", "\n")
                        # tbox.insert("5.15", 'Q3: ')
                        # tbox.insert("5.20", q3)
                    # q2_f = (n+1)/2
                    # q2_floor = math.floor(q2_f)
                    # q2_r1 = x[q2_floor-1]
                    # q2_r2 = x[q2_floor]
                    # q2 = (q2_r1+q2_r2)/2
                    # tbox.insert("4.0", "\n")
                    # tbox.insert("4.15", 'Q2: ')
                    # tbox.insert("4.20", q2)
                break
            except ValueError:
                import tkinter.messagebox
                tk.messagebox.showwarning(title='Wrong Format', message='Please use comma separator')
                break

    # Grouped Range
    elif c_var.get() == 'Grouped Range':
        tbox.delete("1.0", tk.END) # for clearing the already filled output from previous selection
        tbox.insert("1.0", "Lower Class Boundaries:  " + ent_LCB.get())
        tbox.insert("2.0", "\n")
        tbox.insert("2.0", "Upper Class Boundaries:  " + ent_UCB.get())
        tbox.insert("3.0", "\n")
        tbox.insert("3.0", "\n")
        tbox.insert("4.0", "Grouped Range: ")
        while True:
            try:
                u = list(map(float, ent_UCB.get().split(",")))
                l = list(map(float, ent_LCB.get().split(",")))
                a = u[0]
                b = l[1]
                if a == b:
                    ma = max(u)
                    mi = min(l)
                    r = ma-mi
                    tbox.insert("4.18", r)
                else:
                    ma = max(u)
                    mi = min(l)
                    m1 = ma-0.5
                    m2 = mi-0.5
                    if m2 < 0:
                        r = m1-mi
                        tbox.insert("4.18", r)
                    else:
                        r = m1-m2
                        tbox.insert("4.18", r)
                break
            except ValueError:
                import tkinter.messagebox
                tk.messagebox.showwarning(title='Wrong Format', message='Please use comma separator')
                break

    # Grouped Mean
    elif c_var.get() == 'Grouped Mean':
        tbox.delete("1.0", tk.END)  # for clearing the already filled output from previous selection
        tbox.insert("1.0", "Lower Class Boundaries:  " + ent_LCB.get())
        tbox.insert("2.0", "\n")
        tbox.insert("2.0", "Upper Class Boundaries:  " + ent_UCB.get())
        tbox.insert("3.0", "\n")
        tbox.insert("3.0", "Frequency:  " + ent_Freq.get())
        tbox.insert("4.0", "\n")
        tbox.insert("5.0", "\n")
        tbox.insert("5.0", "Grouped Mean: ")
        while True:
            try:
                u = list(map(float, ent_UCB.get().split(",")))
                l = list(map(float, ent_LCB.get().split(",")))
                f = list(map(float, ent_Freq.get().split(",")))
                n = len(l)
                i = 0
                X = []
                while i < n:
                    a = u[i]
                    b = l[i]
                    x = (a+b)/2
                    fx = f[i]*x
                    X.append(fx)
                    i += 1
                sum_f = sum(f)
                sum_fx = sum(X)
                mean = sum_fx/sum_f
                tbox.insert("5.18", mean)
                break
            except ValueError:
                import tkinter.messagebox
                tk.messagebox.showwarning(title='Wrong Format', message='Please use comma separator')
                break

    # Coefficient of Grouped Range
    elif c_var.get() == 'Coefficient of Grouped Range':
        tbox.delete("1.0", tk.END) # for clearing the already filled output from previous selection
        tbox.insert("1.0", "Lower Class Boundaries:  " + ent_LCB.get())
        tbox.insert("2.0", "\n")
        tbox.insert("2.0", "Upper Class Boundaries:  " + ent_UCB.get())
        tbox.insert("3.0", "\n")
        tbox.insert("3.0", "\n")
        tbox.insert("4.0", "Coefficient of Grouped Range: ")
        while True:
            try:
                u = list(map(float, ent_UCB.get().split(",")))
                l = list(map(float, ent_LCB.get().split(",")))
                a = u[0]
                b = l[1]
                if a == b:
                    ma = max(u)
                    mi = min(l)
                    r = (ma-mi)/(ma+mi)
                    tbox.insert("4.33", r)
                else:
                    ma = max(u)
                    mi = min(l)
                    m1 = ma-0.5
                    m2 = mi-0.5
                    if m2 < 0:
                        r = (m1-mi)/(m1+mi)
                        tbox.insert("4.33", r)
                    else:
                        r = (m1-m2)/(m1+m2)
                        tbox.insert("4.33", r) 
                break
            except ValueError:
                import tkinter.messagebox
                tk.messagebox.showwarning(title='Wrong Format', message='Please use comma separator')
                break

    # Grouped Median
    elif c_var.get() == 'Grouped Median':
        tbox.delete("1.0", tk.END)  # for clearing the already filled output from previous selection
        tbox.insert("1.0", "Lower Class Boundaries:  " + ent_LCB.get())
        tbox.insert("2.0", "\n")
        tbox.insert("2.0", "Upper Class Boundaries:  " + ent_UCB.get())
        tbox.insert("3.0", "\n")
        tbox.insert("3.0", "Frequency:  " + ent_Freq.get())
        tbox.insert("4.0", "\n")
        tbox.insert("5.0", "\n")
        tbox.insert("5.0", "Grouped Median: ")
        while True:
            try:
                u = list(map(float, ent_UCB.get().split(",")))
                l = list(map(float, ent_LCB.get().split(",")))
                f = list(map(float, ent_Freq.get().split(",")))
                n = len(l)
                sum_f = sum(f)
                r = sum_f/2
                D = []
                i = 0
                cf = []
                while i < n:    # cumulative less than frequency
                    if i == 0:
                        c = f[i]
                        cf.append(c)
                    else:
                        c2 = f[i]
                        c = cf[i-1]+c2
                        cf.append(c)              
                    dif = cf[i]-r
                    D.append(dif)
                    i += 1
                mi = D.index(min([i for i in D if i > 0]))
                freq = f[int(mi)]
                cfp = cf[int(mi-1)]  
                k = l[int(mi)]
                x = u[0]
                y = l[1]
                if x == y:
                    h = u[0]-l[0]
                    median = k+(h/freq)*((sum_f/2)-cfp)
                else:
                    h = (u[0]-l[0])+1
                    median = (k-0.5)+(h/freq)*((sum_f/2)-cfp)
                tbox.insert("5.18", median)
                break
            except ValueError:
                import tkinter.messagebox
                tk.messagebox.showwarning(title='Wrong Format', message='Please use comma separator')
                break

    # Grouped Mode
    elif c_var.get() == 'Grouped Mode':
        tbox.delete("1.0", tk.END)  # for clearing the already filled output from previous selection
        tbox.insert("1.0", "Lower Class Boundaries:  " + ent_LCB.get())
        tbox.insert("2.0", "\n")
        tbox.insert("2.0", "Upper Class Boundaries:  " + ent_UCB.get())
        tbox.insert("3.0", "\n")
        tbox.insert("3.0", "Frequency:  " + ent_Freq.get())
        tbox.insert("4.0", "\n")
        tbox.insert("5.0", "\n")
        tbox.insert("5.0", "Grouped Mode: ")
        while True:
            try:
                u = list(map(float, ent_UCB.get().split(",")))
                l = list(map(float, ent_LCB.get().split(",")))
                f = list(map(float, ent_Freq.get().split(",")))
                fm = max(f)  # modal frequency
                j = f.index(fm)
                if fm != 0:
                    f1 = f[j-1]  # frequency of group preceding modal group
                    f2 = f[j+1]  # Frequency of group following modal group
                else:
                    f1 = 0
                    f2 = f[j+1]
                k = l[j]  # lower class limit of modal group
                x = u[0]
                y = l[1]
                if x == y:
                    h = u[0]-l[0]
                    mode = k + ((fm-f1)/(2*fm-f1-f2))*h
                else:
                    h = (u[0]-l[0])+1
                    mode = (k-0.5)+((fm-f1)/(2*fm-f1-f2))*h
                tbox.insert("5.18", mode)
                break
            except ValueError:
                import tkinter.messagebox
                tk.messagebox.showwarning(title='Wrong Format', message='Please use comma separator')
                break

    # Grouped Standard Deviation
    elif c_var.get() == 'Grouped Standard Deviation':
        tbox.delete("1.0", tk.END)  # for clearing the already filled output from previous selection
        tbox.insert("1.0", "Lower Class Boundaries:  " + ent_LCB.get())
        tbox.insert("2.0", "\n")
        tbox.insert("2.0", "Upper Class Boundaries:  " + ent_UCB.get())
        tbox.insert("3.0", "\n")
        tbox.insert("3.0", "Frequency:  " + ent_Freq.get())
        tbox.insert("4.0", "\n")
        tbox.insert("5.0", "\n")
        tbox.insert("5.0", "Grouped Standard Deviation: ")
        while True:
            try:
                u = list(map(float, ent_UCB.get().split(",")))
                l = list(map(float, ent_LCB.get().split(",")))
                f = list(map(float, ent_Freq.get().split(",")))
                n = len(l)
                i = 0
                X = []
                m = []
                while i < n:
                    a = u[i]
                    b = l[i]
                    x = (a+b)/2
                    m.append(x)
                    fx = f[i]*x
                    X.append(fx)
                    i += 1
                sum_f = sum(f)
                sum_fx = sum(X)
                mean = sum_fx/sum_f
                s = []
                i = 0
                while i < n:
                    sd = f[i]*((m[i]-mean)**2)
                    s.append(sd)
                    i += 1
                sd1 = math.sqrt(sum(s)/sum_f)
                tbox.insert("5.32", sd1)
                break
            except ValueError:
                import tkinter.messagebox
                tk.messagebox.showwarning(title='Wrong Format', message='Please use comma separator')
                break

    # Grouped Variance
    elif c_var.get() == 'Grouped Variance':
        tbox.delete("1.0", tk.END)  # for clearing the already filled output from previous selection
        tbox.insert("1.0", "Lower Class Boundaries:  " + ent_LCB.get())
        tbox.insert("2.0", "\n")
        tbox.insert("2.0", "Upper Class Boundaries:  " + ent_UCB.get())
        tbox.insert("3.0", "\n")
        tbox.insert("3.0", "Frequency:  " + ent_Freq.get())
        tbox.insert("4.0", "\n")
        tbox.insert("5.0", "\n")
        tbox.insert("5.0", "Grouped Variance: ")
        while True:
            try:
                u = list(map(float, ent_UCB.get().split(",")))
                l = list(map(float, ent_LCB.get().split(",")))
                f = list(map(float, ent_Freq.get().split(",")))
                n = len(l)
                i = 0
                X = []
                m = []
                while i < n:
                    a = u[i]
                    b = l[i]
                    x = (a+b)/2
                    m.append(x)
                    fx = f[i]*x
                    X.append(fx)
                    i += 1
                sum_f = sum(f)
                sum_fx = sum(X)
                mean = sum_fx/sum_f
                s = []
                i = 0
                while i < n:
                    sd = f[i]*((m[i]-mean)**2)
                    s.append(sd)
                    i += 1
                sd1 = sum(s)/sum_f
                tbox.insert("5.22", sd1)
                break
            except ValueError:
                import tkinter.messagebox
                tk.messagebox.showwarning(title='Wrong Format', message='Please use comma separator')
                break    

    # Grouped Coefficient of Variation
    elif c_var.get() == 'Grouped Coefficient of Variation':
        tbox.delete("1.0", tk.END)  # for clearing the already filled output from previous selection
        tbox.insert("1.0", "Lower Class Boundaries:  " + ent_LCB.get())
        tbox.insert("2.0", "\n")
        tbox.insert("2.0", "Upper Class Boundaries:  " + ent_UCB.get())
        tbox.insert("3.0", "\n")
        tbox.insert("3.0", "Frequency:  " + ent_Freq.get())
        tbox.insert("4.0", "\n")
        tbox.insert("5.0", "\n")
        tbox.insert("5.0", "Grouped Coefficient of Variation: ")
        while True:
            try:
                u = list(map(float, ent_UCB.get().split(",")))
                l = list(map(float, ent_LCB.get().split(",")))
                f = list(map(float, ent_Freq.get().split(",")))
                n = len(l)
                i = 0
                X = []
                m = []
                while i < n:
                    a = u[i]
                    b = l[i]
                    x = (a+b)/2
                    m.append(x)
                    fx = f[i]*x
                    X.append(fx)
                    i += 1
                sum_f = sum(f)
                sum_fx = sum(X)
                mean = sum_fx/sum_f
                s = []
                i = 0
                while i < n:
                    sd = f[i]*((m[i]-mean)**2)
                    s.append(sd)
                    i += 1
                sd1 = math.sqrt(sum(s)/sum_f)
                tbox.insert("5.47", sd1/mean)
                break
            except ValueError:
                import tkinter.messagebox
                tk.messagebox.showwarning(title='Wrong Format', message='Please use comma separator')
                break

    # Grouped Quartile
    elif c_var.get() == 'Grouped Quartile':
        tbox.delete("1.0", tk.END)  # for clearing the already filled output from previous selection
        tbox.insert("1.0", "Lower Class Boundaries:  " + ent_LCB.get())
        tbox.insert("2.0", "\n")
        tbox.insert("2.0", "Upper Class Boundaries:  " + ent_UCB.get())
        tbox.insert("3.0", "\n")
        tbox.insert("3.0", "Frequency:  " + ent_Freq.get())
        tbox.insert("4.0", "\n")
        tbox.insert("5.0", "\n")
        tbox.insert("5.0", "Grouped Quartile: ")
        tbox.insert("6.0", "\n")
        while True:
            try:
                j = 1
                q = []
                while j < 4:
                    u = list(map(float, ent_UCB.get().split(",")))
                    l = list(map(float, ent_LCB.get().split(",")))
                    f = list(map(float, ent_Freq.get().split(",")))
                    n = len(l)
                    sum_f = sum(f)
                    g = []
                    e = j*(sum_f/4)
                    g.append(e)
                    i = 0
                    cf = []
                    d = []
                    while i < n:    # cumulative less than frequency
                        if i == 0:
                            c = f[i]
                            cf.append(c)
                        else:
                            c2 = f[i]
                            c = cf[i-1]+c2
                            cf.append(c)
                        dif = cf[i]-e
                        d.append(dif)
                        i += 1
                    mi = d.index(min([i for i in d if i > 0]))
                    if mi == 0:
                        cfp = 0
                    else:
                        cfp = cf[int(mi-1)]
                    freq = f[int(mi)]
                    k = l[int(mi)]
                    x = u[0]
                    y = l[1]
                    if x == y:
                        h = u[0]-l[0]
                        median = k+(h/freq)*(e-cfp)
                    else:
                        h = (u[0]-l[0])+1
                        median = (k-0.5)+(h/freq)*(e-cfp)
                    q.append(median)
                    j += 1
                tbox.insert("6.0", 'Q1 :')
                tbox.insert("6.5", q[0])
                tbox.insert("7.0", "\n")
                tbox.insert("7.0", 'Q2 :')
                tbox.insert("7.5", q[1])
                tbox.insert("8.0", "\n")
                tbox.insert("8.0", 'Q3 :')
                tbox.insert("8.5", q[2])
                break
            except ValueError:
                import tkinter.messagebox
                tk.messagebox.showwarning(title='Wrong Format', message='Please use comma separator')
                break

    # Grouped Quartile Deviation
    elif c_var.get() == 'Grouped Quartile Deviation':
        tbox.delete("1.0", tk.END)  # for clearing the already filled output from previous selection
        tbox.insert("1.0", "Lower Class Boundaries:  " + ent_LCB.get())
        tbox.insert("2.0", "\n")
        tbox.insert("2.0", "Upper Class Boundaries:  " + ent_UCB.get())
        tbox.insert("3.0", "\n")
        tbox.insert("3.0", "Frequency:  " + ent_Freq.get())
        tbox.insert("4.0", "\n")
        tbox.insert("5.0", "\n")
        tbox.insert("5.0", "Grouped Quartile Deviation: ")
        while True:
            try:
                j = 1
                q = []
                while j < 4:
                    u = list(map(float, ent_UCB.get().split(",")))
                    l = list(map(float, ent_LCB.get().split(",")))
                    f = list(map(float, ent_Freq.get().split(",")))
                    n = len(l)
                    sum_f = sum(f)
                    g = []
                    e = j*(sum_f/4)
                    g.append(e)
                    i = 0
                    cf = []
                    d = []
                    while i < n:    # cumulative less than frequency
                        if i == 0:
                            c = f[i]
                            cf.append(c)
                        else:
                            c2 = f[i]
                            c = cf[i-1]+c2
                            cf.append(c)
                        dif = cf[i]-e
                        d.append(dif)
                        i += 1
                    mi = d.index(min([i for i in d if i > 0]))
                    if mi == 0:
                        cfp = 0
                    else:
                        cfp = cf[int(mi-1)]
                    freq = f[int(mi)]
                    k = l[int(mi)]
                    x = u[0]
                    y = l[1]
                    if x == y:
                        h = u[0]-l[0]
                        median = k+(h/freq)*(e-cfp)
                    else:
                        h = (u[0]-l[0])+1
                        median = (k-0.5)+(h/freq)*(e-cfp)
                    q.append(median)
                    j += 1
                tbox.insert("5.29", (q[2]-q[0])/2)
                break
            except ValueError:
                import tkinter.messagebox
                tk.messagebox.showwarning(title='Wrong Format', message='Please use comma separator')
                break

    # Coefficient of Grouped Quartile Deviation
    elif c_var.get() == 'Coefficient of Grouped Quartile Deviation':
        tbox.delete("1.0", tk.END)  # for clearing the already filled output from previous selection
        tbox.insert("1.0", "Lower Class Boundaries:  " + ent_LCB.get())
        tbox.insert("2.0", "\n")
        tbox.insert("2.0", "Upper Class Boundaries:  " + ent_UCB.get())
        tbox.insert("3.0", "\n")
        tbox.insert("3.0", "Frequency:  " + ent_Freq.get())
        tbox.insert("4.0", "\n")
        tbox.insert("5.0", "\n")
        tbox.insert("5.0", "Coefficient of Grouped Quartile Deviation: ")
        while True:
            try:
                j = 1
                q = []
                while j < 4:
                    u = list(map(float, ent_UCB.get().split(",")))
                    l = list(map(float, ent_LCB.get().split(",")))
                    f = list(map(float, ent_Freq.get().split(",")))
                    n = len(l)
                    sum_f = sum(f)
                    g = []
                    e = j*(sum_f/4)
                    g.append(e)
                    i = 0
                    cf = []
                    d = []
                    while i < n:    # cumulative less than frequency
                        if i == 0:
                            c = f[i]
                            cf.append(c)
                        else:
                            c2 = f[i]
                            c = cf[i-1]+c2
                            cf.append(c)
                        dif = cf[i]-e
                        d.append(dif)
                        i += 1
                    mi = d.index(min([i for i in d if i > 0]))
                    if mi == 0:
                        cfp = 0
                    else:
                        cfp = cf[int(mi-1)]
                    freq = f[int(mi)]
                    k = l[int(mi)]
                    x = u[0]
                    y = l[1]
                    if x == y:
                        h = u[0]-l[0]
                        median = k+(h/freq)*(e-cfp)
                    else:
                        h = (u[0]-l[0])+1
                        median = (k-0.5)+(h/freq)*(e-cfp)
                    q.append(median)
                    j += 1
                tbox.insert("5.44", (q[2]-q[0])/(q[2]+q[0]))
                break
            except ValueError:
                import tkinter.messagebox
                tk.messagebox.showwarning(title='Wrong Format', message='Please use comma separator')
                break

    # Grouped Deciles
    elif c_var.get() == 'Grouped Deciles':
        tbox.delete("1.0", tk.END)  # for clearing the already filled output from previous selection
        tbox.insert("1.0", "Lower Class Boundaries:  " + ent_LCB.get())
        tbox.insert("2.0", "\n")
        tbox.insert("2.0", "Upper Class Boundaries:  " + ent_UCB.get())
        tbox.insert("3.0", "\n")
        tbox.insert("3.0", "Frequency:  " + ent_Freq.get())
        tbox.insert("4.0", "\n")
        tbox.insert("5.0", "\n")
        tbox.insert("5.0", "Grouped Deciles: ")
        tbox.insert("6.0", "\n")
        while True:
            try:
                j = 1
                q = []
                while j < 10:
                    u = list(map(float, ent_UCB.get().split(",")))
                    l = list(map(float, ent_LCB.get().split(",")))
                    f = list(map(float, ent_Freq.get().split(",")))
                    n = len(l)
                    sum_f = sum(f)
                    g = []
                    e = j*(sum_f/10)
                    g.append(e)
                    i = 0
                    cf = []
                    d = []
                    while i < n:    # cumulative less than frequency
                        if i == 0:
                            c = f[i]
                            cf.append(c)
                        else:
                            c2 = f[i]
                            c = cf[i-1]+c2
                            cf.append(c)
                        dif = cf[i]-e
                        d.append(dif)
                        i += 1
                    mi = d.index(min([i for i in d if i > 0]))
                    if mi == 0:
                        cfp = 0
                    else:
                        cfp = cf[int(mi-1)]
                    freq = f[int(mi)]
                    k = l[int(mi)]
                    x = u[0]
                    y = l[1]
                    if x == y:
                        h = u[0]-l[0]
                        median = k+(h/freq)*(e-cfp)
                    else:
                        h = (u[0]-l[0])+1
                        median = (k-0.5)+(h/freq)*(e-cfp)
                    q.append(median)
                    j += 1
                a = 0
                while a < 9:
                    tbox.insert(20.0, str('D'))
                    tbox.insert(20.0, a+1)
                    tbox.insert(20.0, ": ")
                    tbox.insert(20.0, q[a])
                    tbox.insert(20.0, "\n")
                    a += 1
                break
            except ValueError:
                import tkinter.messagebox
                tk.messagebox.showwarning(title='Wrong Format', message='Please use comma separator')
                break

    # Grouped Percentiles
    elif c_var.get() == 'Grouped Percentiles':
        tbox.delete("1.0", tk.END)  # for clearing the already filled output from previous selection
        tbox.insert("1.0", "Lower Class Boundaries:  " + ent_LCB.get())
        tbox.insert("2.0", "\n")
        tbox.insert("2.0", "Upper Class Boundaries:  " + ent_UCB.get())
        tbox.insert("3.0", "\n")
        tbox.insert("3.0", "Frequency:  " + ent_Freq.get())
        tbox.insert("4.0", "\n")
        tbox.insert("5.0", "\n")
        tbox.insert("5.0", "Grouped Percentiles: ")
        tbox.insert("6.0", "\n")
        while True:
            try:
                j = 1
                q = []
                while j < 100:
                    u = list(map(float, ent_UCB.get().split(",")))
                    l = list(map(float, ent_LCB.get().split(",")))
                    f = list(map(float, ent_Freq.get().split(",")))
                    n = len(l)
                    sum_f = sum(f)
                    g = []
                    e = j*(sum_f/100)
                    g.append(e)
                    i = 0
                    cf = []
                    d = []
                    while i < n:    # cumulative less than frequency
                        if i == 0:
                            c = f[i]
                            cf.append(c)
                        else:
                            c2 = f[i]
                            c = cf[i-1]+c2
                            cf.append(c)
                        dif = cf[i]-e
                        d.append(dif)
                        i += 1
                    mi = d.index(min([i for i in d if i > 0]))
                    if mi == 0:
                        cfp = 0
                    else:
                        cfp = cf[int(mi-1)]
                    freq = f[int(mi)]
                    k = l[int(mi)]
                    x = u[0]
                    y = l[1]
                    if x == y:
                        h = u[0]-l[0]
                        median = k+(h/freq)*(e-cfp)
                    else:
                        h = (u[0]-l[0])+1
                        median = (k-0.5)+(h/freq)*(e-cfp)
                    q.append(median)
                    j += 1
                a = 0
                while a < 99:
                    tbox.insert(106.0, str('P'))
                    tbox.insert(106.0, a+1)
                    tbox.insert(106.0, ": ")
                    tbox.insert(106.0, q[a])
                    tbox.insert(106.0, "\n")
                    a += 1
                break
            except ValueError:
                import tkinter.messagebox
                tk.messagebox.showwarning(title='Wrong Format', message='Please use comma separator')
                break

    # Grouped mean deviation about mean
    elif c_var.get() == 'Grouped Mean Deviation about Mean':
        tbox.delete("1.0", tk.END)  # for clearing the already filled output from previous selection
        tbox.insert("1.0", "Lower Class Boundaries:  " + ent_LCB.get())
        tbox.insert("2.0", "\n")
        tbox.insert("2.0", "Upper Class Boundaries:  " + ent_UCB.get())
        tbox.insert("3.0", "\n")
        tbox.insert("3.0", "Frequency:  " + ent_Freq.get())
        tbox.insert("4.0", "\n")
        tbox.insert("5.0", "\n")
        tbox.insert("5.0", "Grouped Mean Deviation about Mean: ")
        while True:
            try:
                u = list(map(float, ent_UCB.get().split(",")))
                l = list(map(float, ent_LCB.get().split(",")))
                f = list(map(float, ent_Freq.get().split(",")))
                n = len(l)
                i = 0
                X = []
                while i < n:
                    a = u[i]
                    b = l[i]
                    x = (a+b)/2
                    fx = f[i]*x
                    X.append(fx)
                    i += 1
                sum_f = sum(f)
                sum_fx = sum(X)
                mean = sum_fx/sum_f
                i = 0
                p = []
                while i < n:
                    x1 = l[i]
                    y = u[i]
                    z = (x1+y)/2
                    f1 = f[i]
                    md_r = f1*(abs(z-mean))
                    p.append(md_r)
                    i += 1
                md = sum(p)
                tbox.insert("5.35", md/sum_f)
                break
            except ValueError:
                import tkinter.messagebox
                tk.messagebox.showwarning(title='Wrong Format', message='Please use comma separator')
                break

    # Coefficient of Grouped Mean Deviation about Mean
    elif c_var.get() == 'Coefficient of Grouped Mean Deviation about Mean':
        tbox.delete("1.0", tk.END)  # for clearing the already filled output from previous selection
        tbox.insert("1.0", "Lower Class Boundaries:  " + ent_LCB.get())
        tbox.insert("2.0", "\n")
        tbox.insert("2.0", "Upper Class Boundaries:  " + ent_UCB.get())
        tbox.insert("3.0", "\n")
        tbox.insert("3.0", "Frequency:  " + ent_Freq.get())
        tbox.insert("4.0", "\n")
        tbox.insert("5.0", "\n")
        tbox.insert("5.0", "Coefficient of Grouped Mean Deviation about Mean: ")
        while True:
            try:
                u = list(map(float, ent_UCB.get().split(",")))
                l = list(map(float, ent_LCB.get().split(",")))
                f = list(map(float, ent_Freq.get().split(",")))
                n = len(l)
                i = 0
                X = []
                while i < n:
                    a = u[i]
                    b = l[i]
                    x = (a+b)/2
                    fx = f[i]*x
                    X.append(fx)
                    i += 1
                sum_f = sum(f)
                sum_fx = sum(X)
                mean = sum_fx/sum_f
                i = 0
                p = []
                while i < n:
                    x1 = l[i]
                    y = u[i]
                    z = (x1+y)/2
                    f1 = f[i]
                    md_r = f1*(abs(z-mean))
                    p.append(md_r)
                    i += 1
                md = sum(p)/sum_f
                tbox.insert("5.50", md/mean)    
                break
            except ValueError:
                import tkinter.messagebox
                tk.messagebox.showwarning(title='Wrong Format', message='Please use comma separator')
                break

    # Grouped Mean Deviation about Median
    elif c_var.get() == 'Grouped Mean Deviation about Median':
        tbox.delete("1.0", tk.END)  # for clearing the already filled output from previous selection
        tbox.insert("1.0", "Lower Class Boundaries:  " + ent_LCB.get())
        tbox.insert("2.0", "\n")
        tbox.insert("2.0", "Upper Class Boundaries:  " + ent_UCB.get())
        tbox.insert("3.0", "\n")
        tbox.insert("3.0", "Frequency:  " + ent_Freq.get())
        tbox.insert("4.0", "\n")
        tbox.insert("5.0", "\n")
        tbox.insert("5.0", "Grouped Mean Deviation about Median: ")
        while True:
            try:
                u = list(map(float, ent_UCB.get().split(",")))
                l = list(map(float, ent_LCB.get().split(",")))
                f = list(map(float, ent_Freq.get().split(",")))
                n = len(l)
                sum_f = sum(f)
                r = sum_f/2
                D = []
                i = 0
                cf = []
                while i < n:    # cumulative less than frequency
                    if i == 0:
                        c = f[i]
                        cf.append(c)
                    else:
                        c2 = f[i]
                        c = cf[i-1]+c2
                        cf.append(c)
                    dif = cf[i]-r
                    D.append(dif)
                    i += 1
                mi = D.index(min([i for i in D if i > 0]))
                freq = f[int(mi)]
                cfp = cf[int(mi-1)]
                k = l[int(mi)]
                x = u[0]
                y = l[1]
                if x == y:
                    h = u[0]-l[0]
                    median = k+(h/freq)*((sum_f/2)-cfp)
                else:
                    h = (u[0]-l[0])+1
                    median = (k-0.5)+(h/freq)*((sum_f/2)-cfp)
                i = 0
                w = []
                while i < n:
                    x = u[i]
                    y = l[i]
                    f1 = f[i]
                    z = (x+y)/2
                    md_r = f1*(abs(z-median))
                    w.append(md_r)
                    i += 1
                md = sum(w)
                tbox.insert("5.38", (md/sum_f))
                break
            except ValueError:
                import tkinter.messagebox
                tk.messagebox.showwarning(title='Wrong Format', message='Please use comma separator')
                break    




    # Coefficient of Grouped Mean Deviation about Median
    elif c_var.get() == 'Coefficient of Grouped Mean Deviation about Median':
        tbox.delete("1.0", tk.END)  # for clearing the already filled output from previous selection
        tbox.insert("1.0", "Lower Class Boundaries:  " + ent_LCB.get())
        tbox.insert("2.0", "\n")
        tbox.insert("2.0", "Upper Class Boundaries:  " + ent_UCB.get())
        tbox.insert("3.0", "\n")
        tbox.insert("3.0", "Frequency:  " + ent_Freq.get())
        tbox.insert("4.0", "\n")
        tbox.insert("5.0", "\n")
        tbox.insert("5.0", "Coefficient of Grouped Mean Deviation about Median: ")
        while True:
            try:
                u = list(map(float, ent_UCB.get().split(",")))
                l = list(map(float, ent_LCB.get().split(",")))
                f = list(map(float, ent_Freq.get().split(",")))
                n = len(l)
                sum_f = sum(f)
                r = sum_f/2
                D = []
                i = 0
                cf = []
                while i < n:    # cumulative less than frequency
                    if i == 0:
                        c = f[i]
                        cf.append(c)
                    else:
                        c2 = f[i]
                        c = cf[i-1]+c2
                        cf.append(c)
                    dif = cf[i]-r
                    D.append(dif)
                    i += 1
                mi = D.index(min([i for i in D if i > 0]))
                freq = f[int(mi)]
                cfp = cf[int(mi-1)]
                k = l[int(mi)]
                x = u[0]
                y = l[1]
                if x == y:
                    h = u[0]-l[0]
                    median = k+(h/freq)*((sum_f/2)-cfp)
                else:
                    h = (u[0]-l[0])+1
                    median = (k-0.5)+(h/freq)*((sum_f/2)-cfp)
                i = 0
                w = []
                while i < n:
                    x = u[i]
                    y = l[i]
                    f1 = f[i]
                    z = (x+y)/2
                    md_r = f1*(abs(z-median))
                    w.append(md_r)
                    i += 1
                md = sum(w)/sum_f
                tbox.insert("5.53", (md/median))
                break
            except ValueError:
                import tkinter.messagebox
                tk.messagebox.showwarning(title='Wrong Format', message='Please use comma separator')
                break

    else:
        import tkinter.messagebox
        tk.messagebox.showwarning(title='Wrong Selection', message='Please Select a Valid Function')


# reset button
def clicked1():
    ent_data.delete("0", tk.END)
    ent_LCB.delete("0", tk.END)
    ent_UCB.delete("0", tk.END)
    ent_Freq.delete("0", tk.END)
    tbox.delete("1.0", tk.END)
    combo.current(0)


# buttons
style = ttk.Style()
style.configure("TButton", foreground="black", background="light grey", borderwidth=5, relief='raised')
bt = ttk.Button(frame1, text="Evaluate", style='TButton', command=clicked)
bt.place(x=160, y=290)
bt1 = ttk.Button(frame1, text="Reset", style='TButton', command=clicked1)
bt1.place(x=20, y=290)

# 2nd Frame
# Result Label
tk.Label(frame2, text="Result:", bg='light yellow').place(x=10, y=10)
# Result text box
tbox = tk.Text(frame2, borderwidth=5, relief='sunken', width=50, height=20, bg='light grey', state='normal', font=("Arial",14))
tbox.place(x=30, y=60)

tk.Label(frame1, text="======================================================", bg='light yellow').place(x=0, y=380)

tk.Label(frame1, text='xxxxxxxxxxx  Welcome To Statistics Calculator  xxxxxxxxxxxxx', bg='light yellow').place(x=10, y=400)
tk.Label(frame1, text='*) Select/Type the desired function in the drop-down menu to calculate', bg='light yellow').place(x=10, y=430)
tk.Label(frame1, text='*) Use discrete field for ungrouped and L,U,F for grouped functions', bg='light yellow').place(x=10, y=455)
tk.Label(frame1, text='*) Enter the data separated by comma (e.g. 2,4,6,8) ', bg='light yellow').place(x=10, y=480)
tk.Label(frame1, text='*) Press the Evaluate Button to calculate the result', bg='light yellow').place(x=10, y=505)
tk.Label(frame1, text='*) Press the Reset Button to clear all the fields', bg='light yellow').place(x=10, y=530)
frame1.pack(side='left')
frame2.pack(side='right')

window.mainloop()
