import tkinter as tk
from tkinter import messagebox

class AmazonCloneApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini Amazon")
        self.cart = []
        
        # إنشاء واجهة المستخدم
        self.create_widgets()

    def create_widgets(self):
        # عنوان التطبيق
        self.title_label = tk.Label(self.root, text="Welcome to Mini Amazon", font=("Arial", 24))
        self.title_label.pack(pady=10)
        
        # قائمة المنتجات
        self.products = ["Product 1 - $10", "Product 2 - $20", "Product 3 - $30", "Product 4 - $40"]
        
        self.product_listbox = tk.Listbox(self.root, height=6, width=30)
        for product in self.products:
            self.product_listbox.insert(tk.END, product)
        self.product_listbox.pack(pady=10)
        
        # زر لإضافة المنتج إلى السلة
        self.add_to_cart_button = tk.Button(self.root, text="Add to Cart", command=self.add_to_cart)
        self.add_to_cart_button.pack(pady=5)
        
        # زر لعرض السلة
        self.view_cart_button = tk.Button(self.root, text="View Cart", command=self.view_cart)
        self.view_cart_button.pack(pady=5)
    
    def add_to_cart(self):
        selected_product = self.product_listbox.get(tk.ACTIVE)
        if selected_product:
            self.cart.append(selected_product)
            messagebox.showinfo("Added", f"{selected_product} added to your cart!")
    
    def view_cart(self):
        if self.cart:
            cart_contents = "\n".join(self.cart)
            messagebox.showinfo("Your Cart", f"Items in your cart:\n{cart_contents}")
        else:
            messagebox.showinfo("Your Cart", "Your cart is empty.")

# إنشاء نافذة التطبيق
root = tk.Tk()
app = AmazonCloneApp(root)
root.mainloop()
