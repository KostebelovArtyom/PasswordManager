import tkinter as tk
from tkinter import ttk, messagebox
from storeman import StoreContol
from DBcm import UseDatabase

dbconfig = {'host':'127.0.0.1',
            'user':'PassMan',
            'password':'qwe123',
            'database':'passmandb'}

class PasswordManagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Менеджер паролей")
        self.root.geometry("600x450")
        
        self.store = StoreContol(dbconfig)
        
        self.create_widgets()
        
        self.load_entries()
    
    def create_widgets(self):
        add_frame = ttk.LabelFrame(self.root, text="Добавить новую запись", padding=10)
        add_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(add_frame, text="Сайт/Ресурс:").grid(row=0, column=0, sticky=tk.W)
        self.link_entry = ttk.Entry(add_frame, width=40)
        self.link_entry.grid(row=0, column=1, padx=5, pady=2)
        
        ttk.Label(add_frame, text="Логин:").grid(row=1, column=0, sticky=tk.W)
        self.login_entry = ttk.Entry(add_frame, width=40)
        self.login_entry.grid(row=1, column=1, padx=5, pady=2)
        
        add_btn = ttk.Button(add_frame, text="Добавить", command=self.add_entry)
        add_btn.grid(row=2, column=1, pady=5, sticky=tk.E)
        
        list_frame = ttk.LabelFrame(self.root, text="Сохранённые пароли", padding=10)
        list_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.tree = ttk.Treeview(list_frame, columns=('link', 'login', 'password'), show='headings')
        self.tree.heading('link', text='Ресурс')
        self.tree.heading('login', text='Логин')
        self.tree.heading('password', text='Пароль')
        
        self.tree.column('link', width=150)
        self.tree.column('login', width=150)
        self.tree.column('password', width=150)
        
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        del_btn = ttk.Button(list_frame, text="Удалить выбранное", command=self.remove_entry)
        del_btn.pack(pady=5, anchor=tk.E)
    
    def load_entries(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        with UseDatabase(dbconfig) as cursor:
            _SQL = """SELECT link, login, password FROM storage"""
            cursor.execute(_SQL)
            rows = cursor.fetchall()
            
            for row in rows:
                self.tree.insert('', tk.END, values=row)
    
    def add_entry(self):
        link = self.link_entry.get()
        login = self.login_entry.get()
        
        if not link or not login:
            messagebox.showwarning("Ошибка", "Поля 'Ресурс' и 'Логин' должны быть заполнены")
            return
        
        try:
            self.store.add_entry(link, login)
            self.load_entries()
            
            self.link_entry.delete(0, tk.END)
            self.login_entry.delete(0, tk.END)
            
            messagebox.showinfo("Успех", "Запись успешно добавлена")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось добавить запись: {e}")
    
    def remove_entry(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Ошибка", "Выберите запись для удаления")
            return
        
        item_data = self.tree.item(selected_item[0])
        entry_id = item_data['values'][0]
        
        try:
            self.store.rem_entry(entry_id)
            self.load_entries()
            messagebox.showinfo("Успех", "Запись успешно удалена")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось удалить запись: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordManagerGUI(root)
    root.mainloop()
