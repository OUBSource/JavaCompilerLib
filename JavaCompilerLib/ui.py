# ui.py
import tkinter as tk
from tkinter import filedialog, messagebox
from .compiler import JavaCompiler

class JavaCompilerUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Java Compiler")

        self.label = tk.Label(root, text="Выберите Java-файл:")
        self.label.pack()

        self.file_entry = tk.Entry(root, width=50)
        self.file_entry.pack()

        self.browse_button = tk.Button(root, text="Обзор", command=self.browse_file)
        self.browse_button.pack()

        self.compile_button = tk.Button(root, text="Компилировать", command=self.compile)
        self.compile_button.pack()

    def browse_file(self):
        filename = filedialog.askopenfilename(filetypes=[("Java Files", "*.java")])
        self.file_entry.insert(0, filename)

    def compile(self):
        java_file = self.file_entry.get()
        if java_file:
            stdout, stderr = JavaCompiler.compile(java_file)
            messagebox.showinfo("Результат", stdout if stdout else stderr)
        else:
            messagebox.showerror("Ошибка", "Выберите Java-файл!")

def main():
    root = tk.Tk()
    app = JavaCompilerUI(root)
    root.mainloop()
