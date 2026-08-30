from tkcalendar import Calendar, DateEntry
try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk


def example1():
    def print_sel():
        print(cal.selection_get())
        cal.see(datetime.date(year=2016, month=2, day=5))

    top = tk.Toplevel(root)
    top.configure(bg='#ffe6f2')  # Light pink background

    import datetime
    today = datetime.date.today()

    mindate = datetime.date(year=2018, month=1, day=21)
    maxdate = today + datetime.timedelta(days=5)
    print(mindate, maxdate)

    cal = Calendar(top, font="Arial 14", selectmode='day', locale='en_US',
                   mindate=mindate, maxdate=maxdate, disabledforeground='red',
                   cursor="hand1", year=2018, month=2, day=5,
                   background='#ffb6c1',  # Pink background
                   foreground='#6a006a',  # Dark pink text
                   headersbackground='#ff99cc',  # Pink headers
                   headersforeground='#6a006a',  # Dark pink headers text
                   selectbackground='#ff66b2',  # Brighter pink for selected date
                   selectforeground='white')
    cal.pack(fill="both", expand=True)
    
    ttk.Button(top, text="ok", command=print_sel).pack(pady=5)
    ttk.Button(top, text="Back to Menu", command=top.destroy).pack(pady=5)


def example2():
    top = tk.Toplevel(root)
    top.configure(bg='#ffe6f2')  # Light pink background

    cal = Calendar(top, selectmode='none',
                   background='#ffb6c1', foreground='#6a006a',
                   headersbackground='#ff99cc', headersforeground='#6a006a')
    date = cal.datetime.today() + cal.timedelta(days=2)
    cal.calevent_create(date, 'Hello World', 'message')
    cal.calevent_create(date, 'Reminder 2', 'reminder')
    cal.calevent_create(date + cal.timedelta(days=-2), 'Reminder 1', 'reminder')
    cal.calevent_create(date + cal.timedelta(days=3), 'Message', 'message')

    cal.tag_config('reminder', background='#ff9999', foreground='#ff66b2')

    cal.pack(fill="both", expand=True)
    ttk.Label(top, text="Hover over the events.", background='#ffe6f2').pack()

    ttk.Button(top, text="Back to Menu", command=top.destroy).pack(pady=5)


def example3():
    top = tk.Toplevel(root)
    top.configure(bg='#ffe6f2')  # Light pink background

    ttk.Label(top, text='Choose date', background='#ffe6f2').pack(padx=10, pady=10)

    cal = DateEntry(top, width=12, background='darkblue',
                    foreground='white', borderwidth=2, year=2010,
                    selectbackground='#ff66b2',  # Brighter pink for selection
                    selectforeground='white')
    cal.pack(padx=10, pady=10)

    ttk.Button(top, text="Back to Menu", command=top.destroy).pack(pady=5)


root = tk.Tk()
root.configure(bg='#ffe6f2')  # Light pink background

style = ttk.Style()
style.configure('TButton', background='#ff99cc', foreground='#6a006a', font=('Arial', 12, 'bold'))

ttk.Button(root, text='Calendar', command=example1).pack(padx=10, pady=10)
ttk.Button(root, text='Calendar with events', command=example2).pack(padx=10, pady=10)
ttk.Button(root, text='DateEntry', command=example3).pack(padx=10, pady=10)

root.mainloop()
