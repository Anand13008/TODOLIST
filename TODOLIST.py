import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        # Creating a frame for the Listbox and Scrollbar
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        #This will be our "Listbox"
        self.todo_listbox = tk.Listbox(frame, width=50, height=10, selectmode=tk.SINGLE)
        self.todo_listbox.pack(side=tk.LEFT)

        #This will be our "Scrollbar"
        self.scrollbar = tk.Scrollbar(frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        #Attaching our scrollbar to Listbox
        self.todo_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.todo_listbox.yview)

        #Creating an "entry" widget for new tasks to be added
        self.task_entry = tk.Entry(self.root, width=52)
        self.task_entry.pack(pady=10)

        #Creating an "Add" Task button to add tasks to list
        self.add_task_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=5)

        #Creating a "Delete" Task button for existing tasks to be deleted
        self.delete_task_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.todo_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)  # Clear the entry box
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        try:
            selected_task_index = self.todo_listbox.curselection()[0]
            self.todo_listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    todo_app = TodoApp(root)
    root.mainloop()