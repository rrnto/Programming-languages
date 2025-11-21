import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
import re
import os

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("500x500")
        self.root.config(bg="#f4f4f4")

        # List to store tasks
        self.tasks = []

        # Get the file path for saving tasks
        self.file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tasks.txt")

        # Load tasks from file
        self.load_tasks()

        # Title label
        self.title_label = tk.Label(self.root, text="To-Do List", font=("Helvetica", 24), bg="#f4f4f4", fg="#4CAF50")
        self.title_label.pack(pady=10)

        # Frame for listbox and scrollbar
        self.listbox_frame = tk.Frame(self.root, bg="#f4f4f4")
        self.listbox_frame.pack(pady=10)

        # Scrollbar for the listbox
        self.scrollbar = tk.Scrollbar(self.listbox_frame, orient="vertical")

        # Listbox to display tasks
        self.listbox = tk.Listbox(self.listbox_frame, width=30, height=10, yscrollcommand=self.scrollbar.set, font=("Helvetica", 14), bd=0, selectmode=tk.SINGLE)
        self.listbox.pack(side="left", fill="both")
        self.scrollbar.config(command=self.listbox.yview)
        self.scrollbar.pack(side="right", fill="y")

        # Entry field to add tasks
        self.task_entry = tk.Entry(self.root, font=("Helvetica", 14), bd=2, width=25, fg="#333")
        self.task_entry.pack(pady=10)

        # Entry field for the deadline (e.g., "3 days", "2 weeks")
        self.deadline_entry = tk.Entry(self.root, font=("Helvetica", 14), bd=2, width=25, fg="#333")
        self.deadline_entry.pack(pady=10)
        self.deadline_entry.insert(0, "Deadline (e.g., 3 days, 2 weeks)")

        # Button to add a task
        self.add_button = tk.Button(self.root, text="Add Task", font=("Helvetica", 14), command=self.add_task, bg="#4CAF50", fg="white", relief="flat")
        self.add_button.pack(pady=5)

        # Button to remove selected task
        self.remove_button = tk.Button(self.root, text="Remove Task", font=("Helvetica", 14), command=self.remove_task, bg="#FF6347", fg="white", relief="flat")
        self.remove_button.pack(pady=5)

        # Button to save the tasks to a file
        self.save_button = tk.Button(self.root, text="Save Tasks", font=("Helvetica", 14), command=self.save_tasks, bg="#008CBA", fg="white", relief="flat")
        self.save_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        deadline = self.deadline_entry.get()

        # Parse deadline (e.g., "3 days", "2 weeks")
        deadline_date = self.parse_deadline(deadline)
        if not deadline_date:
            messagebox.showwarning("Invalid Deadline", "Please enter a valid deadline (e.g., '3 days', '2 weeks').")
            return

        if task:
            # Add the task and deadline to the list
            self.tasks.append({"task": task, "deadline": deadline_date, "completed": False})
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
            self.deadline_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task before adding.")

    def remove_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            task = self.listbox.get(selected_task_index)
            task_text = task.split(" | ")[0]  # Get task text to match with list
            self.tasks = [t for t in self.tasks if t["task"] != task_text]  # Remove from tasks list
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to remove.")

    def save_tasks(self):
        """Save tasks to a file"""
        with open(self.file_path, "w") as file:
            for task in self.tasks:
                completed_status = "Completed" if task["completed"] else "Pending"
                file.write(f"{task['task']} | {task['deadline']} | {completed_status}\n")
        messagebox.showinfo("Save", "Tasks saved successfully!")

    def load_tasks(self):
        """Load tasks from a file"""
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                for line in file.readlines():
                    task_text, deadline, completed = line.strip().split(" | ")
                    deadline_date = datetime.strptime(deadline, "%Y-%m-%d")
                    completed_status = completed == "Completed"
                    self.tasks.append({"task": task_text, "deadline": deadline_date, "completed": completed_status})

    def update_listbox(self):
        """Update the listbox with tasks"""
        self.listbox.delete(0, tk.END)  # Clear current list
        for task in self.tasks:
            completed_status = "✔" if task["completed"] else "✘"
            self.listbox.insert(tk.END, f"{task['task']} | {task['deadline'].strftime('%Y-%m-%d')} | {completed_status}")
        self.create_check_buttons()

    def create_check_buttons(self):
        """Create checkboxes for each task to mark as complete"""
        for widget in self.listbox_frame.winfo_children():
            if isinstance(widget, tk.Checkbutton):
                widget.destroy()  # Remove existing check buttons

        for index, task in enumerate(self.tasks):
            var = tk.BooleanVar(value=task["completed"])
            checkbox = tk.Checkbutton(self.listbox_frame, text="Complete", variable=var, command=lambda idx=index, v=var: self.mark_complete(idx, v))
            checkbox.pack()

    def mark_complete(self, index, var):
        """Mark the task as complete/incomplete"""
        self.tasks[index]["completed"] = var.get()
        self.update_listbox()

    def parse_deadline(self, deadline):
        """Parse the deadline string and return the calculated deadline date"""
        # Use regex to check if the deadline is in the format "3 days", "2 weeks"
        match = re.match(r'(\d+)\s*(days?|weeks?)', deadline.lower())
        if not match:
            return None  # Invalid format

        quantity = int(match.group(1))
        unit = match.group(2)

        # Calculate deadline based on the current date
        current_date = datetime.now()

        if "week" in unit:
            deadline_date = current_date + timedelta(weeks=quantity)
        elif "day" in unit:
            deadline_date = current_date + timedelta(days=quantity)

        return deadline_date

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
