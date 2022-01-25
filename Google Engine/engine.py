from tkinter import *
import tkinter as tk
import webbrowser
from PIL import ImageTk, Image
import googlesearch

root = tk.Tk()
root.title("Google Search Engine")
root.geometry("800x500")
root.maxsize(800, 500)
root.minsize(800, 500)
root.iconbitmap('Google.ico')


def callback(url):
    webbrowser.open(url)


def search_query():
    query = text.get("1.0", "end-1c")
    s = googlesearch.search(query, tld="co.in", num=10, stop=1, pause=2)
    for j in s:
        print(webbrowser.open(j))


l1 = Label(root, bg="black", width=500, height=2)
l1.grid(sticky="w")

apps_logo = ImageTk.PhotoImage(Image.open('apps.jpg'))
d = Label(root, image=apps_logo, borderwidth=0)
d.place(x=15, y=11)
apps = Label(root, text="Apps", bg="black", fg="white", cursor="hand2")
apps.place(x=40, y=10)
apps.bind("<Button-1>", lambda e: callback("https://about.google/intl/en/products/?tab=wh"))

d_logo = ImageTk.PhotoImage(Image.open('Google drive.png'))
d = Label(root, image=d_logo, borderwidth=0)
d.place(x=95, y=11)
drive = Label(root, text="Google Drive", bg="black", fg="white", cursor="hand2")
drive.place(x=120, y=10)
drive.bind("<Button-1>", lambda e: callback("https://drive.google.com/"))

yt_logo = ImageTk.PhotoImage(Image.open('youtube.png'))
y = Label(root, image=yt_logo, borderwidth=0)
y.place(x=210, y=12)
yt = Label(root, text="YouTube", bg="black", fg="white", cursor="hand2")
yt.place(x=240, y=10)
yt.bind("<Button-1>", lambda e: callback("https://www.youtube.com/"))

gm_logo = ImageTk.PhotoImage(Image.open('gmail.jpg'))
l2 = Label(root, image=gm_logo, borderwidth=0)
l2.place(x=310, y=12)

gmail = Label(root, text="Gmail", bg="black", fg="white", cursor="hand2")
gmail.place(x=340, y=10)
gmail.bind("<Button-1>", lambda e: callback("https://mail.google.com/mail/"))

g = Label(root, text="Gmail", cursor="hand2")
g.place(x=630, y=50)
g.bind("<Button-1>", lambda e: callback("https://mail.google.com/mail/"))

i = Label(root, text="Images", cursor="hand2")
i.place(x=670, y=50)
i.bind("<Button-1>", lambda e: callback("https://www.google.co.in/imghp?hl=en&tab=wi&ogbl"))

signin = Button(root, text="sign in", font=('roboto', 10, 'bold'), bg="#4583EC", fg="white", cursor="hand2")
signin.place(x=730, y=50)
signin.bind("<Button-1>", lambda e: callback("http://google.com"))

g_logo = ImageTk.PhotoImage(Image.open('google logo.png'))
l2 = Label(root, image=g_logo)
l2.place(x=260, y=190)

text = Text(root, width=90, height=2, relief=RIDGE, font=('roboto', 10, 'bold'), borderwidth=2)
text.place(x=120, y=300)

search = Button(root, text="Google Search", relief=RIDGE, font=('arial', 10), bg="#F3F3F3", fg="#222222",
                cursor="hand2", command=search_query)
search.place(x=280, y=360)

lucky = Button(root, text="i' m Felling Lucky", relief=RIDGE, font=('arial', 10), bg="#F3F3F3", fg="#222222",
               cursor="hand2")
lucky.place(x=400, y=360)
apps.bind("<Button-1>", lambda e: callback("http://google.com"))

offered = Label(root, text="Google offered in:")
offered.place(x=120, y=410)
lang = Label(root, text="हिन्दी বাংলা తెలుగు मराठी தமிழ் ગુજરાતી ಕನ್ನಡ മലയാളം ਪੰਜਾਬੀ", fg="blue")
lang.place(x=230, y=410)

root.mainloop()
