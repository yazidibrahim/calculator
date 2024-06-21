from tkinter import *

# Initialize the main window
win = Tk()
win.title("Calculator")
win.geometry('400x450')

#clear
def btn_clear():
    global expression
    expression = ''
    input_string.set(expression)
#button click function
def btn_click(item):
    global expression
    expression = expression + str(item)
    input_string.set(expression)
#equal btn
def btn_equal():
    global expression
    result = str(eval(expression))
    input_string.set(result)



expression = ''
input_string = StringVar()
# Create a frame for the input field
input_Frame = Frame(win, width=45, height=50)
input_Frame.pack(side=TOP, ipady=10)

# Create an entry field and place it in the frame
input_Field = Entry(input_Frame, font=('ariel', 18, 'bold'), width=45, justify=RIGHT, textvariable=input_string)
input_Field.grid(row=0, column=0)  # ipady increases the internal padding of the entry field
input_Field.pack(ipady=10) #increase the height of input field

#button frame
btn_Frame = Frame(win, width=310, height=270)
btn_Frame.pack()
#first row
clear = Button(btn_Frame, text='C', width = 38, height = 3, command=lambda: btn_clear()).grid(row = 0,column= 0, columnspan= 3, padx= 1, pady= 1)
divide = Button(btn_Frame, text='/', width=10, height=3, command=lambda: btn_click('/')).grid(row=0, column=3, padx=1, pady=1)
#second row
seven = Button(btn_Frame, text='7', width=10, height=3, command=lambda: btn_click(7)).grid(row=1, column=0, padx=1, pady=1)
eight = Button(btn_Frame, text='8', width=10, height=3, command=lambda: btn_click(8)).grid(row=1, column=1, padx=1, pady=1)
nine = Button(btn_Frame, text='9', width=10, height=3, command=lambda: btn_click(9)).grid(row=1, column=2, padx=1, pady=1)
multiply = Button(btn_Frame, text='*', width=10, height=3, command=lambda: btn_click('*')).grid(row=1, column=3, padx=1, pady=1)
#thirdrow
four = Button(btn_Frame, text='4', width=10, height=3, command=lambda: btn_click(4)).grid(row=2, column=0, padx=1, pady=1)
five = Button(btn_Frame, text='5', width=10, height=3, command=lambda: btn_click(5)).grid(row=2, column=1, padx=1, pady=1)
six = Button(btn_Frame, text='6', width=10, height=3, command=lambda: btn_click(6)).grid(row=2, column=2, padx=1, pady=1)
minus = Button(btn_Frame, text='-', width=10, height=3, command=lambda: btn_click('-')).grid(row=2, column=3, padx=1, pady=1)
#fourthrow
one = Button(btn_Frame, text='1', width=10, height=3, command=lambda: btn_click(1)).grid(row=3, column=0, padx=1, pady=1)
two = Button(btn_Frame, text='2', width=10, height=3, command=lambda: btn_click(2)).grid(row=3, column=1, padx=1, pady=1)
three = Button(btn_Frame, text='3', width=10, height=3, command=lambda: btn_click(3)).grid(row=3, column=2, padx=1, pady=1)
plus = Button(btn_Frame, text='+', width=10, height=3, command=lambda: btn_click('+')).grid(row=3, column=3, padx=1, pady=1)
#fifthrow
zero = Button(btn_Frame, text='0', width=24, height=3, command=lambda: btn_click(0) ).grid(row=4, column=0,columnspan=2, padx=1, pady=1)
point = Button(btn_Frame, text='.', width=10, height=3, command=lambda: btn_click('.')).grid(row=4, column=2, padx=1, pady=1)
equal = Button(btn_Frame, text='=', width=10, height=3,command=lambda: btn_equal()).grid(row=4, column=3, padx=1, pady=1)



win.mainloop()
