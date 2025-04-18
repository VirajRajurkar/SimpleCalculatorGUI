import tkinter as tk
import re
from sympy import sympify # type: ignore

calculation = ""

def addToCalculation(symbol):
    """
    Adds the given symbol (number or operator) to the calculation string
    and updates the text field to display the current calculation.
    """
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_expression(expression):
    """
    Evaluates the given mathematical expression safely using sympy.
    Ensures that only valid characters are allowed in the expression.
    
    Args:
        expression (str): The mathematical expression to evaluate.
    
    Returns:
        str: The result of the evaluation or an error message if invalid.
    """
    # Allow only numbers, operators, and parentheses
    if not re.match(r'^[0-9+\-*/(). ]+$', expression):
        return "Invalid Input"
    try:
        result = sympify(expression)
        return result
    except Exception as e:
        return "Error"

def evaluateCalculation():
    """
    Evaluates the current calculation string and displays the result
    in the text field. Resets the calculation string after evaluation.
    """
    global calculation
    result = evaluate_expression(calculation)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, result)
    calculation = ""


def clearField():
    """
    Clears the current calculation string and the text field. 
    Basically the logic of the clear button.
    """
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")
    pass

# Create the main window
root = tk.Tk()
root.geometry("490x250")
root.title("Simple Calculator with GUI")

# Set the size of the window and the title
text_result = tk.Text(root, height=2, width=30, font=("Arial", 24))
text_result.grid(columnspan=5)

#Button definitions
btn_1 = tk.Button(root, text = "1", command = lambda: addToCalculation(1), width = 10, font = ("Arial", 14))
btn_1.grid(row = 2, column = 1)

btn_2 = tk.Button(root, text = "2", command = lambda: addToCalculation(2), width = 10, font = ("Arial", 14))
btn_2.grid(row = 2, column = 2)

btn_3 = tk.Button(root, text = "3", command = lambda: addToCalculation(3), width = 10, font = ("Arial", 14))
btn_3.grid(row = 2, column = 3)

btn_4 = tk.Button(root, text = "4", command = lambda: addToCalculation(4), width = 10, font = ("Arial", 14))
btn_4.grid(row = 3, column = 1)

btn_5 = tk.Button(root, text = "5", command = lambda: addToCalculation(5), width = 10, font = ("Arial", 14))
btn_5.grid(row = 3, column = 2)

btn_6 = tk.Button(root, text = "6", command = lambda: addToCalculation(6), width = 10, font = ("Arial", 14))
btn_6.grid(row = 3, column = 3)

btn_7 = tk.Button(root, text = "7", command = lambda: addToCalculation(7), width = 10, font = ("Arial", 14))
btn_7.grid(row = 4, column = 1)

btn_8 = tk.Button(root, text = "8", command = lambda: addToCalculation(8), width = 10, font = ("Arial", 14))
btn_8.grid(row = 4, column = 2)

btn_9 = tk.Button(root, text = "9", command = lambda: addToCalculation(9), width = 10, font = ("Arial", 14))
btn_9.grid(row = 4, column = 3)

btn_0 = tk.Button(root, text = "0", command = lambda: addToCalculation(0), width = 10, font = ("Arial", 14))
btn_0.grid(row = 5, column = 2)

btn_clear = tk.Button(root, text = "Clear", command = clearField, width = 20, font = ("Arial", 14))
btn_clear.grid(row = 6, column = 1, columnspan = 2)

btn_equals = tk.Button(root, text = "=", command = evaluateCalculation, width = 20, font = ("Arial", 14))
btn_equals.grid(row = 6, column = 3, columnspan = 2)

btn_plus = tk.Button(root, text = "+", command = lambda: addToCalculation("+"), width = 10, font = ("Arial", 14))
btn_plus.grid(row = 2, column = 4)

btn_minus = tk.Button(root, text = "-", command = lambda: addToCalculation("-"), width = 10, font = ("Arial", 14))
btn_minus.grid(row = 3, column = 4)

btn_times = tk.Button(root, text = "*", command = lambda: addToCalculation("*"), width = 10, font = ("Arial", 14))
btn_times.grid(row = 4, column = 4)

btn_div = tk.Button(root, text = "/", command = lambda: addToCalculation("/"), width = 10, font = ("Arial", 14))
btn_div.grid(row = 5, column = 4)

btn_open_parenthesis = tk.Button(root, text = "(", command = lambda: addToCalculation("("), width = 10, font = ("Arial", 14))
btn_open_parenthesis.grid(row = 5, column = 1)

btn_close_parenthesis = tk.Button(root, text = ")", command = lambda: addToCalculation(")"), width = 10, font = ("Arial", 14))
btn_close_parenthesis.grid(row = 5, column = 3)

# Run the main loop!
root.mainloop()

