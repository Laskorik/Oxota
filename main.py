from tkinter import Tk, PhotoImage, Label, Button

# root
root = Tk()
root.title('Oxota na prishelzya')
root.resizable(False, False)

# background
img = PhotoImage(file='planet.png')

bg = Label(root, image=img)
bg.pack()


# start
root.mainloop()
