from tkinter import *
import random


def draw(canvas):
    shape_type = random.choice(["square", "circle", "triangle"])
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    if shape_type == "square":
        x1 = random.randint(0, width - 50)
        y1 = random.randint(0, height - 50)
        x2 = x1 + 50
        y2 = y1 + 50
        canvas.create_rectangle(x1, y1, x2, y2, fill="cyan")
    elif shape_type == "circle":
        x = random.randint(25, width - 25)
        y = random.randint(25, height - 25)
        canvas.create_oval(x - 25, y - 25, x + 25, y + 25, fill="black")
    elif shape_type == "triangle":
        x1 = random.randint(0, width - 20)
        y1 = random.randint(0, height - 100)
        x2 = x1 + 50
        y2 = y1 + 50
        x3 = x1 + 50
        y3 = y1 - 50
        canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill="yellow")


def clear(canvas):
    canvas.delete("all")
    draw(canvas)


root = Tk()
root.title("Random Shape Generator")
root.resizable(False,False)
canvas = Canvas(root, width=500, height=500, bg="white")
canvas.pack(side="top")
generate_button = Button(root, text="Create",
                         command=lambda: clear(canvas))
generate_button.pack(side="bottom")

root.mainloop()
