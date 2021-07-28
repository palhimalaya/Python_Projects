import tkinter

window = tkinter.Tk()
window.title("My first GUI")
window.minsize(width=500, height=400)

my_label = tkinter.Label(text="I am a label. ", font=("Arial", 24, "normal"))
my_label.grid(column=0, row=0)


def button_fun():
    my_label.config(text=inputs.get())


button = tkinter.Button(text="Click Me", command=button_fun)
button.grid(column=1, row=1)

button = tkinter.Button(text="New Button", command=button_fun)
button.grid(column=2, row=0)


inputs = tkinter.Entry(width=10)
inputs.grid(column=3,row=2)
window.mainloop()
