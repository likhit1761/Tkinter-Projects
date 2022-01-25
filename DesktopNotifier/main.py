import tkinter
from plyer import notification


def notifier():
    msg = note_cont.get()
    title = note_title.get()
    notification.notify(title=title,
                        message=msg,
                        app_icon=None,
                        timeout=10,
                        toast=False)


tk = tkinter.Tk()
tk.geometry("500x400")
tk.title("Python Desktop Notifier")
tk.config(bg="light sea green")

heading = tkinter.Label(text="Python Desktop Notifier", font="Monospace 18 bold", bg="light sea green")
heading.pack()

title_lb = tkinter.Label(text="Enter Notification Title:", font="Monospace 12 bold", bg="light sea green")
title_lb.pack()
title_lb.place(x="50", y=100)

note_title = tkinter.Entry(font="Monospace 12", width=25)
note_title.pack()
note_title.place(x="250", y=100)

cont_lb = tkinter.Label(text="Enter Notification Content:", font="Monospace 12 bold", bg="light sea green")
cont_lb.pack()
cont_lb.place(x="150", y=180)

note_cont = tkinter.Entry(font="Monospace 12", width=50)
note_cont.pack()
note_cont.place(x="20", y=220)

send = tkinter.Button(text="Send Notification", font="Monospace 15 bold", borderwidth=6, command=notifier)
send.pack()
send.place(x="155", y=300)

tk.mainloop()
