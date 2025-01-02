import tkinter as tk
from tkinter import messagebox

a={}
c=0
def Add_Task():
    global c
    t=task.get()
    if t.strip():  # Ensure the task is not empty
        c+=1
        a[c] = t  # Store the task with the counter as the key
        messagebox.showinfo("Task Added.","The task has been added")
        print(f"Task {c} added: {t}")
        task.delete(0, tk.END)
    else:
        messagebox.showinfo("Error","Enter Valid task")
        print("Enter valid task") 
        task.delete(0, tk.END)   

def View_Task():
    if a:
        task_list.delete(0, tk.END)
        for i in a:
           task_list.insert(tk.END, f"{i}. {a[i]}") 
    else:
        messagebox.showinfo("Empty List", "The To-Do List is empty.")
        print("To do list is empty🥲.")   

def DeleteAll_Tasks():
    if a:
        a.clear()
        messagebox.showinfo("Success", "All tasks deleted.")
        task_list.delete(0, tk.END)
        global c
        c = 0
    else:
        messagebox.showinfo("Empty List", "The To-Do List is empty.")
        print("To do list is empty🥲.")     

def Delete_Task():
    global a
    global c
    try:
        i=int(delete_task.get().strip())
        if i in a:  # Check if the task exists in the dictionary
            del a[i]  # Delete the task
            messagebox.showinfo("Success", f"The task {i} has been deleted")
            print(f"Task '{i}' has been deleted.")
            a = {new_key: task for new_key, task in enumerate(a.values(), start=1)}
            c=len(a)
            delete_task.delete(0, tk.END)
            View_Task()
        else:
            messagebox.showinfo("Error", "Task not found in the to-do list")
            print("Task not found in the to-do list.")
            delete_task.delete(0, tk.END)
    except Exception as e:
        messagebox.showinfo("Error", f"An error occurred.")
        print("An error occurred:", e)

def Exit():
    root.destroy()
    messagebox.showinfo("Exit", "Hope you enjoyed!")
    print("Exit! Hope you enjoyed!")

root=tk.Tk()
root.title("TODO List")
root.geometry("700x700")

#Heading 
heading = tk.Label(root, text="TODO List", font=("Arial", 24, "bold"), fg="blue")
heading.pack(pady=20)

# Task Input Frame
task_frame = tk.Frame(root)
task_frame.pack(pady=10)

headings = tk.Label(task_frame, text="Enter your task", font=("Arial", 14))
headings.grid(row=0, column=0, padx=5)

task = tk.Entry(task_frame,width=30, font=("Arial", 14))
task.grid(row=0, column=1, padx=5)

#Add Task Button
add_task=tk.Button(task_frame,text="Add Task",command=Add_Task,bg="green", fg="white",font=("Arial", 14))
add_task.grid(row=0, column=2, padx=5)

# Task List Display
list_frame = tk.Frame(root)
list_frame.pack(pady=10)

list_label = tk.Label(list_frame, text="Tasks:", font=("Arial", 16, "bold"))
list_label.pack()

task_list = tk.Listbox(list_frame, width=50, height=10, font=("Arial", 12), selectmode=tk.SINGLE)
task_list.pack(pady=5)

#View Task Button

view_frame = tk.Frame(root)
view_frame.pack(pady=10)

view_task=tk.Button(view_frame,text="View Tasks",command=View_Task,bg="blue", fg="white",font=("Arial", 12))
view_task.grid(row=0,column=0,padx=10)

#Delete All Tasks Button
deleteAll_task=tk.Button(view_frame,text="Delete All Tasks",command=DeleteAll_Tasks,bg="red", fg="white" , font=("Arial", 12))
deleteAll_task.grid(row=0,column=1,padx=10)

#Delete task frame
delete_frame = tk.Frame(root)
delete_frame.pack(pady=10)

#Delete a task heading
del_heading = tk.Label(delete_frame, text="Enter task number to delete", font=("Arial", 14))
del_heading.grid(row=0,column=0,padx=5)

#Delete a task
delete_task = tk.Entry(delete_frame,width = 10, font=("Arial", 14))
delete_task.grid(row=0,column=1,padx=5)

#Delete Tasks Button
del_task=tk.Button(delete_frame,text="Delete Task",command=Delete_Task,bg="red", fg="white" , font=("Arial", 12))
del_task.grid(row=0,column=2,padx=5)

#Exit Button
exit=tk.Button(root,text="Exit",command=Exit,bg="black", fg="white" , font=("Arial", 12))
exit.pack(pady=10)

root.mainloop()