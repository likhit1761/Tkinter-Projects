# Importing Modules
import tkinter
from tkinter.constants import CENTER, DISABLED
import geocoder
import webbrowser  # Not Related to Project


# finding location
def find():
    ip = geocoder.ip(entry_pn.get())
    location_city = str(ip.city)
    location_country = str(ip.country)
    location_str.set(location_city + "," + location_country)


# basic tkinter
tk = tkinter.Tk()
tk.geometry("500x300")
tk.resizable(False, False)
tk.title("IP Address Location Finder")
tk.configure(bg="light sea green")

# Creating Heading
heading = tkinter.Label(text="IP Address Location Finder",
                        font="Monospcae 18 bold",
                        bg="light sea green")
heading.pack()
heading.place(x=100, y=20)

# Creating label for Entry
label_pn = tkinter.Label(text="Enter IP Address :",
                         font="Monospace 13 bold",
                         bg="light sea green")
label_pn.pack()
label_pn.place(x=70, y=65)

# Creating Entry Box
entry_pn = tkinter.Entry(width=30)
entry_pn.pack()
entry_pn.place(x=240, y=70)

# Creating Button
button_pn = tkinter.Button(text="Find !",
                           font="Monospace 12",
                           borderwidth=2,
                           command=find)
button_pn.pack()
button_pn.place(x=210, y=130)

# Creating Location entry
location_str = tkinter.StringVar()
location_str.set("You can type 'me' for this device")

entry_location = tkinter.Entry(textvariable=location_str,
                               font="Monospace 12",
                               width=25,
                               state="disabled")
entry_location.pack()
entry_location.place(x=130, y=200)

loc_lab = tkinter.Label(text="⬆️ Location",
                        font="Monospace 12 bold",
                        bg="light sea green")
loc_lab.pack()
loc_lab.place(x=170, y=230)

tk.mainloop()
