from tkinter import *
import random

root = Tk()
root.title("Dice Simulator")
root.geometry("600x500")

label = Label(root , font = ("Helvintica" , 300 , 'bold'),text='' , fg = 'purple')

def rolldice ():
    dice = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    label.configure(text=f'{random.choice(dice)}')
    label.pack()
button = Button(root, font = ("Helvitica", 25 , 'bold'),text = 'Dice Roll' , command = rolldice, bg = 'blue' , fg = 'white')
button.pack()
root.mainloop()
