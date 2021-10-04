from tkinter import Label, Tk 
import time
w = Tk() 
w.title("Clock") 
w.geometry("390x150") 
w.resizable(1,1)

text_font= ("Times New Roman", 70, 'bold')
background = "#f2e750"
foreground= "#ff6347"
border_width = 25

label = Label(w, font=text_font, bg=background, fg=foreground, bd=border_width) 
label.grid(row=0, column=1)

def clock(): 
   time1 = time.strftime("%H:%M:%S")
   label.config(text=time1) 
   label.after(200, clock)

clock()
w.mainloop()