from tkinter import *
import pyshorteners

# Create GUI
wd = Tk()
wd.geometry("500x200")
wd.title("URL Shortner")

url = Label(wd, text='Enter URL')
url.grid(column=0, row=1)

url_entry = Entry(wd, width=70)
url_entry.grid(column=1, row=1)

# Shorten URL
def convert_url():
    link = url_entry.get()
    Shortener=pyshorteners.Shortener()
    
    print(link, end =' ')
    short_url = Shortener.tinyurl.short(link)
    print(f'-> {short_url}')
    
    tex = Text(master=wd,height=5 ,width=50)
    tex.grid(column=1, row=5)
    tex.insert(END, short_url)

button = Button(wd, text='Run', width=15, command=convert_url)
button.grid(column=1, row=3)

wd.mainloop()