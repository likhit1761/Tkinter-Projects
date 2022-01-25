import tkinter
from PyDictionary import PyDictionary

tk = tkinter.Tk()
tk.title('Tkinter Dictionary')
tk.geometry("800x300")
tk.resizable(False, False)

heading = tkinter.Label(text="Search Word:",
                        font="Monospace 18 bold")
heading.pack()
heading.place(x=310, y=30)

search = tkinter.StringVar()
search.set("Search Here !")

entry1 = tkinter.Entry(textvariable=search,
                       font="Monospace 14")
entry1.pack()
entry1.place(x=280, y=90)

meaning = tkinter.StringVar()
meaning.set("The Definition Will Appear Here!")

meaning_entry = tkinter.Entry(textvariable=meaning,
                              font="Monospace 14",
                              width=70)
meaning_entry.pack()
meaning_entry.place(x=15, y=200)


def main():
    word = entry1.get()
    mean = PyDictionary()
    final = mean.meaning(word)
    mean_present = final['Noun'][0]
    meaning.set(mean_present)


search_btn = tkinter.Button(text="Search!",
                            font="Monospace 12 bold",
                            borderwidth=6,
                            command=main)
search_btn.pack()
search_btn.place(x=350, y=150)

tk.mainloop()
