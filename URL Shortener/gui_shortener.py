import pyshorteners
import tkinter


def shortener():
    short_url = pyshorteners.Shortener()
    short_output = short_url.tinyurl.short(input_link.get())
    output.set(short_output)

    tk.clipboard_clear()
    tk.clipboard_append(short_output)
    copy.config(text="Copied To The Clipboard!")


tk = tkinter.Tk()
tk.geometry("400x300")
tk.resizable(False, False)
tk.title("URL Shortener")
tk.configure(bg="#69afcf")

heading = tkinter.Label(text="URl Shortener", font="Monospace 18 bold", bg="#69afcf", fg="white")
heading.pack()
heading.place(x=110, y=30)

input = tkinter.StringVar()
input.set("Enter URL Here")

input_link = tkinter.Entry(textvariable=input, font="Monospace 15 ", width="30")
input_link.pack()
input_link.place(x=30, y=90)

short_btn = tkinter.Button(text="Generate", font="Monospace 12 ", command=shortener, borderwidth=5)
short_btn.pack()
short_btn.place(x=150, y=140)

output = tkinter.StringVar()
output.set("Short Links")

output_link = tkinter.Entry(textvariable=output, font="Monospace 15 ", width="30")
output_link.pack()
output_link.place(x=30, y=200)

copy = tkinter.Label(text="", font="Monospace 15 bold", bg="#69afcf", fg="sea green")
copy.pack()
copy.place(x=70, y=250)

tk.mainloop()
