import tkinter as tk
import math

#Declaration
root = tk.Tk()
root.title("Calculator")

#Function
l_result = 0
sentence = False
def insertnumber(number):
    global l_result
    global f_result
    if sentence == True:
        l_result = str(l_result) + str(number)
        f_sentence = views.get()
        views.delete(0, tk.END)
        views.insert(0, str(f_sentence) + str(number))
    else:
        f_num = views.get()
        f_result = str(f_num) + str(number)
        views.delete(0, tk.END)
        views.insert(0, str(f_num) + str(number))
def addition():
    global sentence
    global method
    method = "add"
    sentence = True
    f_num = views.get()
    views.delete(0, tk.END)
    views.insert(0, str(f_num) + "+")
def substraction():
    global sentence
    global method
    method = "substract"
    sentence = True
    f_num = views.get()
    views.delete(0, tk.END)
    views.insert(0, str(f_num) + "-")
def multiplication():
    global sentence
    global method
    method = "multiply"
    sentence = True
    f_num = views.get()
    views.delete(0, tk.END)
    views.insert(0, str(f_num) + "x")
def division():
    global sentence
    global method
    method = "divide"
    sentence = True
    f_num = views.get()
    views.delete(0, tk.END)
    views.insert(0, str(f_num) + "/")
def percent():
    global sentence
    global method
    method = "percent"
    sentence = True
    f_num = views.get()
    views.delete(0, tk.END)
    views.insert(0, str(f_num) + "x100%")
def mod():
    global sentence
    global method
    method = "mod"
    sentence = True
    f_num = views.get()
    views.delete(0, tk.END)
    views.insert(0, str(f_num) + "mod")
def factorial():
    global sentence
    global method
    method = "factorial"
    sentence = True
    f_num = views.get()
    views.delete(0, tk.END)
    views.insert(0, str(f_num) + "!")
def comma():
    global sentence
    global method
    method = "comma"
    sentence = True
    f_num = views.get()
    views.delete(0, tk.END)
    views.insert(0, str(float(f_num)))
def plusminus():
    global sentence
    global method
    global f_result
    method = "plusminus"
    sentence = True
    f_num = views.get()
    views.delete(0, tk.END)
    views.insert(0, str(int(f_num) * -1)  )
    f_result = str(int(f_num) * -1)
def equal():
    if method == "add":
        l_sentence = views.get()
        views.delete(0, tk.END)
        views.insert(0,  l_sentence + "=" + str(int(f_result) + int(l_result)))
        record()
    if method == "substract":
        l_sentence = views.get()
        views.delete(0, tk.END)
        views.insert(0,  l_sentence + "=" + str(int(f_result) - int(l_result)))
        record()
    if method == "multiply":
        l_sentence = views.get()
        views.delete(0, tk.END)
        views.insert(0,  l_sentence + "=" + str(int(f_result) * int(l_result)))
        record()
    if method == "divide":
        l_sentence = views.get()
        views.delete(0, tk.END)
        views.insert(0,  l_sentence + "=" + str(int(f_result) / int(l_result)))
        record()
    if method == "percent":
        l_sentence = views.get()
        views.delete(0, tk.END)
        views.insert(0,  l_sentence + "=" + str(int(f_result) / 100))
        record()
    if method == "mod":
        l_sentence = views.get()
        views.delete(0, tk.END)
        views.insert(0,  l_sentence + "=" + str(int(f_result) % int(l_result)))
        record()
    if method == "factorial":
        l_sentence = views.get()
        views.delete(0, tk.END)
        views.insert(0,  l_sentence + "=" + str(math.factorial(int(f_result))))
        record()
def clear():
    global method
    global f_result
    global l_result
    global sentence
    views.delete(0, tk.END)
    method = False
    sentence = False
    f_result = 0
    l_result = 0
def record():
    tk.Label(history, text = views.get()).pack()
#LAYOUT
views = tk.Entry(root, borderwidth = 10)
history = tk.LabelFrame(root, padx = 20)
history_label = tk.Label(root, text = "History", padx = 20)
#Mainbutton
button0 = tk.Button(root, padx = 20, text = 0, command = lambda:insertnumber(0))
button1= tk.Button(root, padx = 20, text = 1, command = lambda:insertnumber(1))
button2 = tk.Button(root, padx = 20, text = 2, command = lambda:insertnumber(2))
button3 = tk.Button(root, padx = 20, text = 3, command = lambda:insertnumber(3))
button4 = tk.Button(root, padx = 20, text = 4, command = lambda:insertnumber(4))
button5 = tk.Button(root, padx = 20, text = 5, command = lambda:insertnumber(5))
button6 = tk.Button(root, padx = 20, text = 6, command = lambda:insertnumber(6))
button7 = tk.Button(root, padx = 20, text = 7, command = lambda:insertnumber(7))
button8 = tk.Button(root, padx = 20, text = 8, command = lambda:insertnumber(8))
button9 = tk.Button(root, padx = 20, text = 9, command = lambda:insertnumber(9))

#Operator
clear = tk.Button(root, padx = 10, text = "Clear", command = clear, bg = "white")
add = tk.Button(root, padx = 19, text = "+", command = addition) 
substract = tk.Button(root, padx = 20, text = "-", command = substraction) 
multiply = tk.Button(root, padx = 20, text = "x", command = multiplication) 
divide = tk.Button(root, padx = 20, text = "/", command = division) 
equal = tk.Button(root, padx = 20, text = "=", command = equal) 
percent = tk.Button(root, padx = 22, text = "%", command = percent) 
mod = tk.Button(root, padx = 14, text = "mod", command = mod) 
factorial = tk.Button(root, padx = 22, text = "n!", command = factorial) 
comma = tk.Button(root, padx = 22, text = ",", command = comma) 
plusminus = tk.Button(root, padx = 18, text = "+/-", command = plusminus) 
out = tk.Button(root, padx = 16, text = "Quit", command = root.destroy, bg= "red", fg = "white")

#Grid System
views.grid(row = 0, column = 1, columnspan = 3)
history_label.grid(row = 0, column = 5)
history.grid(row = 1, column = 5, rowspan = 4)

button0.grid(row = 4, column = 2)

button1.grid(row = 3, column = 1)
button2.grid(row = 3, column = 2)
button3.grid(row = 3, column = 3)

button4.grid(row = 2, column = 1)
button5.grid(row = 2, column = 2)
button6.grid(row = 2, column = 3)

button7.grid(row = 1, column = 1)
button8.grid(row = 1, column = 2)
button9.grid(row = 1, column = 3)

clear.grid(row = 0, column = 4)
add.grid(row = 1, column = 4)
substract.grid(row = 2, column = 4)
multiply.grid(row = 3, column = 4)
divide.grid(row = 4, column = 4)
equal.grid(row = 4, column = 3)

percent.grid(row = 1, column = 0)
mod.grid(row = 2, column = 0)
factorial.grid(row = 3, column = 0)
plusminus.grid(row = 4, column = 0)
comma.grid(row = 4, column = 1)
out.grid(row = 0, column = 0)

#Essentsial Feature
root.mainloop()