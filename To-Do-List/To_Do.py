#import Tkinter
import tkinter as tk

#instruction window code
def open_instruction_window():
    instruction_window = tk.Toplevel(root)
    instruction_window.title("Instructions")
    instruction_label = tk.Label(instruction_window, text="---Welcome to the To-Do List Application!---\n\n"
                                                        "Instructions:\n"
                                                        "1. Enter a task in the input field below.\n"
                                                        "2. Click 'Add Task' to add the task to your to-do list.\n"
                                                        "3. Click on a task to mark it as completed (✓) or click on it again to mark it incomplete.\n"
                                                        "4. Enjoy organizing your tasks!")
    instruction_label.pack(padx=20, pady=20)
    close_button = tk.Button(instruction_window, text="Close", command=instruction_window.destroy)
    close_button.pack(pady=10)

#add tasks
def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
#function to toggle the check-mark
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

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create a button to open the instruction window
instruction_button = tk.Button(root, text="Instructions", command=open_instruction_window)
instruction_button.pack(pady=10)

# Create a listbox to display tasks
listbox = tk.Listbox(root, selectmode=tk.SINGLE)
listbox.pack(pady=10)

# Create an entry field to add tasks
entry = tk.Entry(root)
entry.pack(pady=5)

# Create a button to add tasks
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

# Bind the listbox to the toggle_task function
listbox.bind('<ButtonRelease-1>', toggle_task)

# Start the tkinter main loop
root.mainloop()
