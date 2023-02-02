import tkinter
from tkinter.font import BOLD

ivory = "#ffe4c0"
pink = "#ffbbbb"
blue = "#bffff0"
green = "#bffff0"

def clicked(digit):
    if digit == "←":
        input_entry.delete(len(input_entry.get())-1) #last index delete
    else:
        input_entry.insert(tkinter.END, digit) 

def del_digit():
    input_entry.delete(0, tkinter.END)
    result_label.config(text="")

def calculate():

    try: 
        result = eval(input_entry.get()) #operation
    except:
        result_label.config(text="Wrong input")
    else:
         result_label.config(text=result)


window = tkinter.Tk()
window.title("Calculator")
window.resizable(False, False)
window.config(padx=10, pady=10, bg=ivory)

digits = [
    ['7','8','9','*'],
    ['4','5','6','/'],
    ['1','2','3','-'],
    ['0','.','←','+']
]

input_entry = tkinter.Entry(window, width=30, font=("Helvetica", 20),
                bg=ivory, justify='right')
input_entry.grid(column=0, row=0, columnspan=4)
input_entry.focus()


result_label = tkinter.Label(window, text="", width=20, font=("Helvetica", 30), bg=ivory)
result_label.grid(column=0, row=1,  columnspan=4, pady=15)

for r in range(4):
    for c in range(4):
        digit = digits[r][c]
        button = tkinter.Button(window, text=digit, width=8, font=("Helvetica", 15), bg=pink, command=lambda x=digit: clicked(x)) #command=lambda x=digit: clicked(x)
        button.grid(row=r+2, column=c, pady=2)

clear_button = tkinter.Button(window, text="C", width=17, font=("Helvetica", 15, BOLD), bg=blue, command=del_digit)
clear_button.grid(column=0, row=6, columnspan=2, pady=5)

cal_button = tkinter.Button(window, text="=", width=17, font=("Helvetica", 15, BOLD), bg=blue, command=calculate)
cal_button.grid(column=2, row=6, columnspan=2, pady=5)

def return_key(event):
    calculate()

window.bind("<Return>", return_key)

window.mainloop()