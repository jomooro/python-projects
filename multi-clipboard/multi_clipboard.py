import tkinter as tk
import pyperclip

class MultiClipboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Multi Clipboard")
        self.clipboard_data = []

        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)

        self.create_button("Save", self.save_clipboard)
        self.create_button("Clear", self.clear_clipboard)
        self.create_button("Quit", self.quit_application)

        self.listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        self.listbox.pack(pady=10)
        self.listbox.bind("<Double-Button-1>", self.load_clipboard)

        self.update_listbox()

        self.root.protocol("WM_DELETE_WINDOW", self.quit_application)

    def create_button(self, text, command):
        button = tk.Button(self.root, text=text, command=command)
        button.pack(side=tk.LEFT, padx=5)

    def save_clipboard(self):
        content = self.entry.get()
        if content:
            self.clipboard_data.append(content)
            self.update_listbox()
            self.clear_entry()

    def clear_clipboard(self):
        self.clipboard_data.clear()
        self.update_listbox()
        self.clear_entry()

    def load_clipboard(self, event):
        selected_index = self.listbox.curselection()
        if selected_index:
            content_to_load = self.clipboard_data[selected_index[0]]
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, content_to_load)

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        self.listbox.insert(tk.END, *self.clipboard_data)

    def clear_entry(self):
        self.entry.delete(0, tk.END)

    def quit_application(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MultiClipboardApp(root)
    root.mainloop()
