from Tkinter import *
import parser

root = Tk()
root.title('Calculator')
#get the user input

i=0
def get_numbers(num):
	global i
	display.insert(i,num)
	i += 1

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

Button(root, text = "AC").grid(row = 5, column =0)
Button(root, text = "/").grid(row = 2, column = 3)
Button(root, text = "*").grid(row = 3, column = 3)
Button(root, text = "-").grid(row = 4, column = 3)
Button(root, text = "+").grid(row = 5, column = 3)
Button(root, text = "0", command = lambda: get_numbers(0)).grid(row = 5, column = 1)
Button(root, text = "=").grid(row = 5, column = 2)


root.mainloop()