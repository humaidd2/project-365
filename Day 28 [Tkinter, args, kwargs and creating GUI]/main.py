from tkinter import *

window = Tk()
window.title("Miles to KM converter")
window.minsize(width=200, height=200)
'''
Screen text
'''
d_input = Entry(width=10)
d_input.grid(column=1, row=0)

text1 = Label(text="Miles")
text1.grid(column=2, row=0)

text2 = Label(text="is equal to")
text2.grid(column=0, row=1)

km_text = Label(text="0")
km_text.grid(column=1, row=1)

km_sign = Label(text="Km")
km_sign.grid(column=2, row=1)


# Converter calculation function
def calculate():
    miles = int(d_input.get())
    km = (miles * 1.6).__ceil__()
    km_text.config(text=km)


calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)

window.mainloop()
