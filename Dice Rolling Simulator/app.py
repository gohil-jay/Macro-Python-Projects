import random
import tkinter
from PIL import Image, ImageTk

root = tkinter.Tk()
root.geometry('500x500')
root.title('Roll the Dice')

l0 = tkinter.Label(root, text="")
l0.pack()
l1 = tkinter.Label(root, text="Dice Rolling Simulator", fg = "red", bg = "white", font = "Helvetica 16 bold italic")
l1.pack()

dice = ['Dice Rolling Simulator/die1.png', 'Dice Rolling Simulator/die2.png', 'Dice Rolling Simulator/die3.png', 'Dice Rolling Simulator/die4.png', 'Dice Rolling Simulator/die5.png', 'Dice Rolling Simulator/die6.png']
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

label1 = tkinter.Label(root, image=image1)
label1.image = image1
label1.pack( expand=True)

def rolling_dice():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))    
    label1.configure(image=image1)
    label1.image = image1

button = tkinter.Button(root, text='Roll the Dice', fg='red', command=rolling_dice)
button.pack( expand=True)

root.mainloop()
