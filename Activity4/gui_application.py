# FoodieExpress GUI Application
# Simple order management system

import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime

# Database setup
db = sqlite3.connect('foodieexpress.db')
cursor = db.cursor()

# Create tables if they don't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    phone TEXT,
    type TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    items INTEGER,
    price_per_item REAL,
    food_cost REAL,
    delivery_distance REAL,
    delivery_charge REAL,
    discount REAL,
    total REAL,
    date TEXT,
    FOREIGN KEY(customer_id) REFERENCES customers(id)
)
''')

db.commit()

# Main GUI Window
class FoodieExpressApp:
    def __init__(self, root):
        self.root = root
        self.root.title("FoodieExpress Order System")
        self.root.geometry("500x600")
        
        # Title
        title = tk.Label(root, text="FoodieExpress", font=("Arial", 18, "bold"))
        title.pack(pady=10)
        
        # Input Frame
        input_frame = tk.Frame(root)
        input_frame.pack(padx=10, pady=10)
        
        # Customer Name
        tk.Label(input_frame, text="Customer Name:").pack(anchor="w")
        self.name_entry = tk.Entry(input_frame, width=30)
        self.name_entry.pack(pady=5)
        
        # Customer Type
        tk.Label(input_frame, text="Customer Type:").pack(anchor="w")
        self.type_var = tk.StringVar(value="Regular")
        tk.Radiobutton(input_frame, text="Regular", variable=self.type_var, value="Regular").pack(anchor="w")
        tk.Radiobutton(input_frame, text="Premium (10% discount)", variable=self.type_var, value="Premium").pack(anchor="w")
        tk.Radiobutton(input_frame, text="VIP (20% discount)", variable=self.type_var, value="VIP").pack(anchor="w")
        
        # Number of Items
        tk.Label(input_frame, text="Number of Items:").pack(anchor="w", pady=(10, 0))
        self.items_entry = tk.Entry(input_frame, width=30)
        self.items_entry.pack(pady=5)
        
        # Price Per Item
        tk.Label(input_frame, text="Price Per Item (Rs):").pack(anchor="w")
        self.price_entry = tk.Entry(input_frame, width=30)
        self.price_entry.pack(pady=5)
        
        # Delivery Distance
        tk.Label(input_frame, text="Delivery Distance (km):").pack(anchor="w")
        self.distance_entry = tk.Entry(input_frame, width=30)
        self.distance_entry.pack(pady=5)
        
        # Calculate Button
        calc_btn = tk.Button(root, text="Calculate Total", command=self.calculate_order, bg="green", fg="white", width=20)
        calc_btn.pack(pady=10)
        
        # Output Frame
        output_frame = tk.Frame(root, relief="sunken", borderwidth=2)
        output_frame.pack(padx=10, pady=10, fill="both", expand=True)
        
        tk.Label(output_frame, text="Bill Details:", font=("Arial", 12, "bold")).pack(anchor="w", padx=5, pady=5)
        
        self.output_text = tk.Text(output_frame, height=12, width=50, font=("Courier", 10))
        self.output_text.pack(padx=5, pady=5, fill="both", expand=True)
        
        # Clear Button
        clear_btn = tk.Button(root, text="Clear", command=self.clear_fields, bg="red", fg="white", width=20)
        clear_btn.pack(pady=5)
    
    def validate_inputs(self):
        """Check if all inputs are valid"""
        name = self.name_entry.get().strip()
        items_str = self.items_entry.get().strip()
        price_str = self.price_entry.get().strip()
        distance_str = self.distance_entry.get().strip()
        
        # Check customer name
        if not name:
            messagebox.showerror("Error", "Please enter customer name")
            return False
        
        # Check number of items
        try:
            items = int(items_str)
            if items <= 0:
                messagebox.showerror("Error", "Number of items must be positive")
                return False
        except ValueError:
            messagebox.showerror("Error", "Please enter valid number of items")
            return False
        
        # Check price per item
        try:
            price = float(price_str)
            if price < 0:
                messagebox.showerror("Error", "Price cannot be negative")
                return False
        except ValueError:
            messagebox.showerror("Error", "Please enter valid price")
            return False
        
        # Check delivery distance
        try:
            distance = float(distance_str)
            if distance < 0:
                messagebox.showerror("Error", "Distance cannot be negative")
                return False
            if distance > 20:
                messagebox.showerror("Error", "Maximum delivery distance is 20 km")
                return False
        except ValueError:
            messagebox.showerror("Error", "Please enter valid distance")
            return False
        
        return True
    
    def calculate_order(self):
        """Calculate order total and display bill"""
        
        # Validate inputs first
        if not self.validate_inputs():
            return
        
        # Get input values
        name = self.name_entry.get().strip()
        items = int(self.items_entry.get())
        price = float(self.price_entry.get())
        distance = float(self.distance_entry.get())
        customer_type = self.type_var.get()
        
        # Calculate food cost
        food_cost = items * price
        
        # Calculate delivery charge
        if food_cost >= 5000:
            delivery_charge = 0  # Free delivery
        else:
            delivery_charge = distance * 50  # Rs 50 per km
        
        # Calculate subtotal
        subtotal = food_cost + delivery_charge
        
        # Calculate discount based on customer type
        if customer_type == "Premium":
            discount = subtotal * 0.10
        elif customer_type == "VIP":
            discount = subtotal * 0.20
        else:
            discount = 0
        
        # Calculate final total
        final_total = subtotal - discount
        
        # Display bill
        bill = f"""
========= FoodieExpress Bill =========
Customer: {name}
Customer Type: {customer_type}

Items: {items}
Price per item: Rs. {price:.2f}
Food Cost: Rs. {food_cost:.2f}

Delivery Distance: {distance} km
Delivery Charge: Rs. {delivery_charge:.2f}

Subtotal: Rs. {subtotal:.2f}
Discount ({customer_type}): Rs. {discount:.2f}

========== FINAL TOTAL ===========
Total Amount: Rs. {final_total:.2f}
=======================================
Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        """
        
        # Show bill in output area
        self.output_text.delete('1.0', tk.END)
        self.output_text.insert('1.0', bill)
        
        # Save to database
        self.save_to_database(name, items, price, distance, food_cost, delivery_charge, discount, final_total, customer_type)
    
    def save_to_database(self, name, items, price, distance, food_cost, delivery_charge, discount, total, customer_type):
        """Save order to database"""
        try:
            # Check if customer exists
            cursor.execute("SELECT id FROM customers WHERE name=?", (name,))
            result = cursor.fetchone()
            
            if result:
                customer_id = result[0]
            else:
                # Add new customer
                cursor.execute("INSERT INTO customers (name, type) VALUES (?, ?)", (name, customer_type))
                customer_id = cursor.lastrowid
            
            # Add order
            cursor.execute("""INSERT INTO orders (customer_id, items, price_per_item, food_cost, delivery_distance, delivery_charge, discount, total, date)
                           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                          (customer_id, items, price, food_cost, distance, delivery_charge, discount, total, datetime.now()))
            
            db.commit()
            messagebox.showinfo("Success", "Order saved to database!")
        except Exception as e:
            messagebox.showerror("Error", f"Could not save order: {str(e)}")
    
    def clear_fields(self):
        """Clear all input fields"""
        self.name_entry.delete(0, tk.END)
        self.items_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.distance_entry.delete(0, tk.END)
        self.type_var.set("Regular")
        self.output_text.delete('1.0', tk.END)

# Run application
if __name__ == "__main__":
    root = tk.Tk()
    app = FoodieExpressApp(root)
    root.mainloop()
