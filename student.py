print("Hello World")
import pickle
from tkinter import *
student = {}
student = pickle.load(open("student.dat","rb"))
root = Tk()
root.title("Student Mangement System")
root.geometry("350x100")
#defineing functions
def add():
    root1 = Tk()
    root1.title("New student")
    root1.geometry("400x100")
    #creating the labels
    name = Label(root1, text = "Enter the name of the student")
    age = Label(root1, text = "Enter the age of the student")
    height = Label(root1, text = "Enter the the height of the student")
    name.grid(row = 0, column = 0)
    age.grid(row=1, column=0)
    height.grid(row=2, column=0)
    #creating the textbox
    name_e = Entry(root1)
    age_e = Entry(root1)
    height_e = Entry(root1)
    name_e.grid(row = 0, column = 1)
    age_e.grid(row=1, column=1)
    height_e.grid(row=2, column=1)
    #defining add_button
    def add_button():
        student[name_e.get()] = [age_e.get(), height_e.get()]
        name_e.delete(0, END)
        age_e.delete(0, END)
        height_e.delete(0, END)
        pickle.dump(student, open("student.dat", "wb"))
    #creating the buttons
    add_b = Button(root1, text = "ADD", command = add_button)
    add_b.grid(row = 3, column = 1)
    root1.mainloop()
# defining show to shwow things
def show():
    a = 0
    root2 = Tk()
    root2.title("Show details")
    root2.geometry("400x400")
    detail_list = Label(root2, text = "name - age - height")
    detail_list.pack()
    for i in student:
        details = Label(root2, text = i+" - "+student[i][0]+" - "+student[i][1])
        details.pack()
    root2.mainloop()
def clear():
    def yes():
        student.clear()
        root3.destroy()
        pickle.dump(student, open("student.dat", "wb"))
    def no():
        root3.destroy()
    root3 = Tk()
    root3.title("Clear records")
    root3.geometry("350x100")
    confrm = Label(root3, text = "Are you sure you want to clear all records")
    confrm.pack()
    confrm_button = Button(root3, text = "YES",command = yes)
    confrm_button.pack()
    non_confem_button = Button(root3, text = "NO", command = no)
    non_confem_button.pack()
#creating startup UI
btn_add = Button(root, text = "Add new student", command = add).pack()
btn_show = Button(root, text = "Show records", command = show).pack()
btn_delete = Button(root, text = "Clear records", command = clear).pack()
root.mainloop()
print(student)
