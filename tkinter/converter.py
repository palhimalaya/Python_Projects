from tkinter import *

screen = Tk()
screen.title("Mile to Km Converter")
screen.config(padx=30, pady=20)


def calculate():
    mile = float(inputs.get())
    km = round(mile * 1.609)
    label_3.config(text=f"{km}")


inputs = Entry(width=15)
inputs.get()
inputs.grid(column=1, row=0)

label_1 = Label(text="Miles")
label_1.grid(column=2, row=0)

label_2 = Label(text="is equal to")
label_2.grid(column=0, row=1)

label_3 = Label(text="0")
label_3.grid(column=1, row=1)

label_4 = Label(text="Km")
label_4.grid(column=2, row=2)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)
screen.mainloop()
