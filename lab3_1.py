import math
import tkinter as tk
from tkinter import ttk

def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("Iteration number")
    label = ttk.Label(popup, text="Number of iterations: " + msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()

def isOdd(n):
    return False if n % 2 == 0 else True

def isNaturalSqr(n):
    return True if math.sqrt(n) - math.floor(math.sqrt(n)) == 0 else False

counter = 0

def getXY(s, n):
    global counter
    counter += 1
    l = math.pow(s, 2) - n
    return isNaturalSqr(l) and (s, int(math.sqrt(l))) or getXY(s + 1, n)

def getAB(x, y):
    return x + y, x - y

print("Insert number:")
N = int(input())
assert (N > 1 and isOdd(N)), "Unexpected value!"

x, y = getXY(abs(math.ceil(math.sqrt(N))), N)
a, b = getAB(x, y)

print("Result:", a, b)
popupmsg(str(counter))
