from Tkinter import *
import parser

root = Tk()
root.title('Calculator')
#get the user input
i = 0

def get_numbers(num):
	global i
	display.insert(i,num)
	i += 1

def clear_all():
	display.delete(0,END)

def one_by_one():
	entire_string = display.get()
	new_string = entire_string[:-1]
	clear_all()
	display.insert(0,new_string)

def calculate():
	entire_string = display.get()
	try:
		a = parser.expr(entire_string).compile()
		result = eval(a)
		clear_all()
		display.insert(0,result)

	except Exception as e:
		raise e

def get_operation(operator):
	global i
	length = len(operator)
	display.insert(i,operator)
	i += length

#adding the input field
display = Entry(root)
display.grid(row = 1, columnspan = 6, sticky = W + E)

#adding buttons to the calculator

Button(root, text = "1", command = lambda: get_numbers(1)).grid(row = 2, column = 0)
Button(root, text = "2", command = lambda: get_numbers(2)).grid(row = 2, column = 1)
Button(root, text = "3", command = lambda: get_numbers(3)).grid(row = 2, column = 2)

Button(root, text = "4", command = lambda: get_numbers(4)).grid(row = 3, column = 0)
Button(root, text = "5", command = lambda: get_numbers(5)).grid(row = 3, column = 1)
Button(root, text = "6", command = lambda: get_numbers(6)).grid(row = 3, column = 2)

Button(root, text = "7", command = lambda: get_numbers(7)).grid(row = 4, column = 0)
Button(root, text = "8", command = lambda: get_numbers(8)).grid(row = 4, column = 1)
Button(root, text = "9", command = lambda: get_numbers(9)).grid(row = 4, column = 2)

Button(root, text = "AC", command = lambda: clear_all()).grid(row = 5, column =0)
Button(root, text = "/", command = lambda: get_operation("/")).grid(row = 2, column = 3)
Button(root, text = "*", command = lambda: get_operation("*")).grid(row = 3, column = 3)
Button(root, text = "-", command = lambda: get_operation("-")).grid(row = 4, column = 3)
Button(root, text = "+", command = lambda: get_operation("+")).grid(row = 5, column = 3)
Button(root, text = "0", command = lambda: get_numbers(0)).grid(row = 5, column = 1)
Button(root, text = "=", command = lambda: calculate()).grid(row = 5, column = 2)
Button(root, text = "DEL", command = lambda: one_by_one()).grid(row = 2, column = 4)

root.mainloop()