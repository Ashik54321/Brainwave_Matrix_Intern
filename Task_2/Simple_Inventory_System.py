import tkinter as tk
from tkinter import messagebox, simpledialog
import datetime

# Sample users (username: password)
users = {"admin": "admin123"}

# Sample product storage
inventory = []

# Login Window
def login_window():
    def check_login():
        username = user_entry.get()
        password = pass_entry.get()
        if users.get(username) == password:
            login.destroy()
            inventory_manager()
        else:
            messagebox.showerror("Error", "Invalid credentials!")

    login = tk.Tk()
    login.title("Login")
    login.geometry("300x150")

    tk.Label(login, text="Username").pack()
    user_entry = tk.Entry(login)
    user_entry.pack()

    tk.Label(login, text="Password").pack()
    pass_entry = tk.Entry(login, show="*")
    pass_entry.pack()

    tk.Button(login, text="Login", command=check_login).pack()
    login.mainloop()

# Inventory GUI
def inventory_manager():
    def add_product():
        name = simpledialog.askstring("Add Product", "Product Name:")
        qty = simpledialog.askinteger("Add Product", "Quantity:")
        price = simpledialog.askfloat("Add Product", "Price:")

        if name and qty is not None and price is not None:
            inventory.append({"name": name, "quantity": qty, "price": price})
            refresh_list()

    def edit_product():
        selected = listbox.curselection()
        if selected:
            index = selected[0]
            product = inventory[index]
            new_qty = simpledialog.askinteger("Edit Product", f"New quantity for {product['name']}:", initialvalue=product['quantity'])
            if new_qty is not None:
                inventory[index]['quantity'] = new_qty
                refresh_list()

    def delete_product():
        selected = listbox.curselection()
        if selected:
            index = selected[0]
            del inventory[index]
            refresh_list()

    def show_low_stock():
        low_stock_items = [p for p in inventory if p['quantity'] < 5]
        if not low_stock_items:
            messagebox.showinfo("Low Stock", "No low stock items.")
            return

        msg = "\n".join([f"{p['name']} (Qty: {p['quantity']})" for p in low_stock_items])
        messagebox.showwarning("Low Stock Items", msg)

    def show_summary():
        total_value = sum(p['quantity'] * p['price'] for p in inventory)
        total_items = sum(p['quantity'] for p in inventory)
        report = f"Total Items: {total_items}\nTotal Inventory Value: ₹{total_value:.2f}\nDate: {datetime.datetime.now().strftime('%Y-%m-%d')}"
        messagebox.showinfo("Inventory Summary", report)

    def refresh_list():
        listbox.delete(0, tk.END)
        for p in inventory:
            listbox.insert(tk.END, f"{p['name']} - Qty: {p['quantity']} - ₹{p['price']:.2f}")

    window = tk.Tk()
    window.title("Inventory Manager")
    window.geometry("400x400")

    listbox = tk.Listbox(window, width=50)
    listbox.pack(pady=10)

    tk.Button(window, text="Add Product", command=add_product).pack(fill='x')
    tk.Button(window, text="Edit Quantity", command=edit_product).pack(fill='x')
    tk.Button(window, text="Delete Product", command=delete_product).pack(fill='x')
    tk.Button(window, text="Low Stock Alert", command=show_low_stock).pack(fill='x')
    tk.Button(window, text="Inventory Summary", command=show_summary).pack(fill='x')

    window.mainloop()

# Run the app
login_window()