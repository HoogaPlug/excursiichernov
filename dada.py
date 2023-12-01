from tkinter import*

def add_task():
    task = entry.get()
    if task:
        listbox.insert(END, task)
        entry.delete(0, END)

def mark_as_important():
    selected = listbox.curselection()
    if selected:
        task_index = selected[0]
        task_text = listbox.get(task_index)
        if task_text.startswith('!'):
            task_text = task_text[1:]
        else:
            task_text = '!' + task_text
        listbox.delete(task_index)
        listbox.insert(task_index, task_text)

def filter_important():
    listbox.delete(0, END)
    for task in tasks:
        if task.startswith('!'):
            listbox.insert(END, task)

def filter_all():
    listbox.delete(0, END)
    for task in tasks:
        listbox.insert(END, task)

root = Tk()
root.title("ToDo-лист")

frame = Frame(root)
frame.pack(pady=10)

listbox = Listbox(frame, width=50)
listbox.pack(side=LEFT, fill=Y)

scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry = Entry(root, font=('Arial', 14))
entry.pack(pady=10)

add_button = Button(root, text="Добавить задачу", command=add_task)
add_button.pack(pady=5)

mark_button = Button(root, text="Отметить как важное", command=mark_as_important)
mark_button.pack(pady=5)

filter_important_button = Button(root, text="Показать важные задачи", command=filter_important)
filter_important_button.pack(pady=5)

filter_all_button = Button(root, text="Показать все задачи", command=filter_all)
filter_all_button.pack(pady=5)

tasks = []

root.mainloop()