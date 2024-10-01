import tkinter as tk
from tkinter import messagebox

# Function to show an error message window
def show_error_window(message):
    messagebox.showerror("Error", message)

# Function to open the instruction window
def open_instruction_window():
    instruction_text = """\
    --- Welcome to the To-Do List Application! ---

    Instructions:
    1. Enter a task in the input field below.
    2. Press 'Enter' or click 'Add Task' to add the task to your to-do list.
    3. Click on a task to mark it as completed (✓) or click on it again
        to mark it incomplete.
    4. Right-click on a task to delete it.
    5. Enjoy organizing your tasks!
    """
    instruction_window = tk.Toplevel(root)
    instruction_window.title("Instructions")
    
    instruction_label = tk.Label(instruction_window, text=instruction_text, justify="left", wraplength=400)
    instruction_label.pack(padx=20, pady=20)
    
    close_button = tk.Button(instruction_window, text="Close", command=instruction_window.destroy)
    close_button.pack(pady=10)

# Function to add tasks
def add_task(event=None):
    task = entry.get().strip()  # Remove leading/trailing whitespace
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        show_error_window("Task cannot be empty.")

# Function to toggle the check-mark
def toggle_task(event):
    selected_task_index = listbox.nearest(event.y)
    if selected_task_index >= 0:
        task = listbox.get(selected_task_index)
        completed = task.startswith("✓ ")
        if completed:
            task = task[2:]  # Remove the "✓ " prefix
        else:
            task = "✓ " + task
        listbox.delete(selected_task_index)
        listbox.insert(selected_task_index, task)

# Function to delete a task
def delete_task(event):
    selected_task_index = listbox.nearest(event.y)
    if selected_task_index >= 0:
        listbox.delete(selected_task_index)

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create a button to open the instruction window
instruction_button = tk.Button(root, text="Instructions", command=open_instruction_window)
instruction_button.pack(pady=10)

# Create a listbox to display tasks with a scrollbar
listbox_frame = tk.Frame(root)
listbox_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

listbox = tk.Listbox(listbox_frame, selectmode=tk.SINGLE, selectbackground="lightblue", selectforeground="black", font=("Arial", 12))
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(listbox_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Create an entry field to add tasks with a placeholder
entry = tk.Entry(root, font=("Arial", 12), justify=tk.LEFT)
entry.insert(0, "Add a task...")
entry.bind("<FocusIn>", lambda event: entry.delete(0, tk.END))  # Clear placeholder when focused
entry.bind("<Return>", add_task)  # Bind the 'Return' key to add_task function
entry.pack(pady=5, padx=20, fill=tk.BOTH, expand=True)

# Create a button to add tasks
add_button = tk.Button(root, text="Add Task", command=add_task, font=("Arial", 12))
add_button.pack(pady=5, padx=20)

# Bind the listbox to the toggle_task function
listbox.bind('<ButtonRelease-1>', toggle_task)
listbox.bind('<Button-3>', delete_task)  # Right-click to delete task

# Start the tkinter main loop
root.mainloop()
