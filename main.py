
from tkinter import *

window= Tk()
window.title("Mile to Km converter")
window.minsize(400,400)

def miles_to_km():
    miles= float(search_box.get())
    km= miles* 1.609
    result_label.config(text=f"{km}")


#search_box:
search_box= Entry(width= 15)
search_box.grid(row= 1, column=1)

#label
equals_label =Label(text=" is equals to")
equals_label.grid(row=2, column=0)

miles_label =Label(text=" Miles")
miles_label.grid(row=1, column=2)

result_label =Label(text="0")
result_label.grid(row=2, column=1)

km_label =Label(text="km")
km_label.grid(row=2, column=2)

#button:
button= Button(text="Calculate", command=miles_to_km)
button.grid(row=3, column=1)

window.mainloop()
