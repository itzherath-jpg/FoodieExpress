# Activity 2.2 - Code Examples and Critical Evaluation

## Procedural Example: Order Cost Calculation

```python
# Procedural Approach - FoodieExpress Order Cost

def calculate_delivery_charge(distance):
    """Calculate delivery charge based on distance"""
    RATE_PER_KM = 50
    return distance * RATE_PER_KM

def apply_discount(price, customer_type):
    """Apply discount based on customer type"""
    if customer_type == "Premium":
        return price * 0.9  # 10% discount
    elif customer_type == "VIP":
        return price * 0.8  # 20% discount
    else:
        return price

def calculate_final_cost(base_price, distance, customer_type):
    """Calculate final order cost"""
    delivery = calculate_delivery_charge(distance)
    subtotal = base_price + delivery
    final_price = apply_discount(subtotal, customer_type)
    return final_price

# Usage
base_price = 500
distance = 5
customer = "Premium"

cost = calculate_final_cost(base_price, distance, customer)
print(f"Final Cost: Rs. {cost}")
```

### Evaluation:
**Strengths:**
- Easy to understand step-by-step
- Simple functions for each task
- Good for beginners

**Weaknesses:**
- Data (price, distance) not linked to functions
- Hard to track related data
- Difficult to extend for multiple customers
- Global functions everywhere

---

## Object-Oriented Example: Order Cost Calculation

```python
# OOP Approach - FoodieExpress Order Cost

class Customer:
    def __init__(self, name, customer_type):
        self.name = name
        self.customer_type = customer_type
    
    def get_discount_rate(self):
        if self.customer_type == "Premium":
            return 0.10
        elif self.customer_type == "VIP":
            return 0.20
        else:
            return 0.0

class Order:
    DELIVERY_RATE = 50  # Rs per km
    
    def __init__(self, base_price, distance, customer):
        self.base_price = base_price
        self.distance = distance
        self.customer = customer
    
    def calculate_delivery_charge(self):
        return self.distance * self.DELIVERY_RATE
    
    def calculate_total(self):
        delivery = self.calculate_delivery_charge()
        subtotal = self.base_price + delivery
        
        discount = subtotal * self.customer.get_discount_rate()
        final_cost = subtotal - discount
        
        return final_cost
    
    def display_receipt(self):
        print(f"Customer: {self.customer.name}")
        print(f"Base Price: Rs. {self.base_price}")
        print(f"Delivery (Distance: {self.distance}km): Rs. {self.calculate_delivery_charge()}")
        print(f"Discount ({self.customer.customer_type}): {self.customer.get_discount_rate() * 100}%")
        print(f"Total: Rs. {self.calculate_total()}")

# Usage
customer1 = Customer("Ahmed", "Premium")
order1 = Order(500, 5, customer1)
order1.display_receipt()

customer2 = Customer("Fatima", "VIP")
order2 = Order(1000, 10, customer2)
order2.display_receipt()
```

### Evaluation:
**Strengths:**
- Data bundled with related methods
- Easy to create multiple orders
- Easy to extend (add new customer types)
- Code reusability
- Better organization

**Weaknesses:**
- More code for simple tasks
- Requires understanding of classes
- Overhead for small programs
- Steeper learning curve

---

## Event-Driven Example: Order GUI

```python
# Event-Driven Approach - FoodieExpress GUI

import tkinter as tk
from tkinter import ttk

class OrderGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("FoodieExpress Order")
        
        # Input fields
        ttk.Label(root, text="Base Price:").pack()
        self.price_entry = ttk.Entry(root)
        self.price_entry.pack()
        
        ttk.Label(root, text="Distance (km):").pack()
        self.distance_entry = ttk.Entry(root)
        self.distance_entry.pack()
        
        ttk.Label(root, text="Customer Type:").pack()
        self.customer_type = ttk.Combobox(root, values=["Regular", "Premium", "VIP"])
        self.customer_type.pack()
        
        # Button to calculate
        self.calculate_button = ttk.Button(root, text="Calculate Cost", command=self.on_calculate)
        self.calculate_button.pack()
        
        # Output label
        self.result_label = ttk.Label(root, text="Total: Rs. 0", font=("Arial", 14))
        self.result_label.pack()
    
    def on_calculate(self):
        """Event handler when Calculate button is clicked"""
        try:
            price = float(self.price_entry.get())
            distance = float(self.distance_entry.get())
            customer_type = self.customer_type.get()
            
            # Calculate
            delivery = distance * 50
            subtotal = price + delivery
            
            if customer_type == "Premium":
                discount = subtotal * 0.10
            elif customer_type == "VIP":
                discount = subtotal * 0.20
            else:
                discount = 0
            
            total = subtotal - discount
            
            self.result_label.config(text=f"Total: Rs. {total:.2f}")
        except ValueError:
            self.result_label.config(text="Please enter valid numbers")

# Usage
if __name__ == "__main__":
    root = tk.Tk()
    gui = OrderGUI(root)
    root.mainloop()
```

### Evaluation:
**Strengths:**
- Responds to user actions (button clicks)
- Interactive and user-friendly
- Program flow controlled by events
- Good for GUI applications

**Weaknesses:**
- Complex program flow
- Harder to understand for beginners
- Difficult to debug
- Mixed concerns (UI and logic)

---

## Critical Comparison

### For FoodieExpress System:

**Which is best?**
- **GUI Application:** Event-Driven + OOP (Best choice)
- **Simple script:** Procedural (Simple)
- **Large system:** OOP (Most flexible)

### Hybrid Approach (Recommended):

Combine all three:
1. **OOP** - Use classes for Order and Customer
2. **Procedural** - Methods contain step-by-step logic
3. **Event-Driven** - GUI buttons trigger calculations

### Code Quality Ranking:

1. **OOP + Event-Driven** - Best for GUI applications
2. **OOP** - Best for business logic
3. **Procedural + Event-Driven** - Acceptable for small GUIs
4. **Pure Procedural** - Only for simple scripts

### Maintainability:

| Paradigm | After 6 months | After 1 year | Adding features |
|----------|---|---|---|
| Procedural | Easy | Getting Hard | Difficult |
| OOP | Easy | Still Easy | Easy |
| Event-Driven | Hard | Very Hard | Difficult |
| Hybrid (OOP + Event) | Easy | Easy | Very Easy |

---

## Conclusion

For the FoodieExpress assignment:
- **Use OOP** for clean code organization
- **Use Event-Driven** for GUI responsiveness
- **Use Procedural logic** inside class methods
- **Combine all three** for best results
