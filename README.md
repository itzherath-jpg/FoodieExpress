# FoodieExpress - BTEC Higher Nationals Assignment

A complete food delivery order management system built for the BTEC Higher Nationals Computer Science curriculum.

## 📚 Project Overview

FoodieExpress is an assignment project that demonstrates:
- Algorithm design and analysis
- Different programming paradigms
- Database design and implementation
- GUI application development
- Debugging and coding standards

## 📁 Project Structure

```
FoodieExpress/
├── Activity1/              # Algorithms and Programming Process
│   ├── pseudocode.md       # Algorithm pseudocode
│   ├── algorithms.py       # Python implementations
│   └── dry_run_and_bigO.md # Dry run examples and Big-O analysis
│
├── Activity2/              # Programming Paradigms
│   ├── paradigms_explanation.md  # Explanation of 3 paradigms
│   └── code_examples.md          # Procedural, OOP, Event-driven examples
│
├── Activity3/              # Database Design and IDE
│   └── README.md           # Database design and IDE features
│
├── Activity4/              # Full System Build and Debugging
│   ├── README.md           # System requirements and debugging
│   ├── gui_application.py  # Main GUI application
│   ├── test_cases.py       # Test cases
│   └── debugging_guide.md  # Debugging tips
│
└── README.md               # This file
```

## 🎯 Activities Summary

### Activity 1: Algorithms and Programming Process
**What you'll find:**
- Definition of algorithms and good algorithm characteristics
- Pseudocode for two algorithms:
  1. Order growth sequence (Fibonacci-like pattern)
  2. Discounted cost calculation
- Steps from writing code to execution
- Dry run examples with sample values
- Big-O complexity analysis

**Key files:**
- `Activity1/pseudocode.md` - Pseudocode and process diagrams
- `Activity1/algorithms.py` - Working Python code
- `Activity1/dry_run_and_bigO.md` - Detailed analysis

---

### Activity 2: Programming Paradigms
**What you'll find:**
- Explanation of 3 programming paradigms:
  1. **Procedural** - Step-by-step functions
  2. **Object-Oriented (OOP)** - Classes and objects
  3. **Event-Driven** - Responding to user events
- Code examples for each paradigm
- Comparison and advantages/disadvantages
- When to use each paradigm

**Key files:**
- `Activity2/paradigms_explanation.md` - Theory
- `Activity2/code_examples.md` - Working code examples

---

### Activity 3: Database Design and IDE
**What you'll find:**
- Database schema with 3 tables:
  1. **CUSTOMER** - Customer information
  2. **ORDER** - Order details
  3. **DELIVERY** - Delivery tracking
- SQL CREATE TABLE statements
- Table relationships and explanations
- IDE features analysis (Code Completion, Debugging, UI Design)
- IDE comparison (VS Code vs PyCharm)
- Advantages of using an IDE

**Key files:**
- `Activity3/README.md` - Complete explanation

---

### Activity 4: Full System Build, Debugging, and Coding Standards
**What you'll find:**
- Complete FoodieExpress GUI application
- Input validation
- Cost calculations (food, delivery, discounts)
- Database integration
- Debugging guide with common errors
- Coding standards and best practices
- Test cases

**Key files:**
- `Activity4/README.md` - System requirements
- `Activity4/gui_application.py` - Working GUI application
- `Activity4/test_cases.py` - Test cases
- `Activity4/debugging_guide.md` - Debugging help

---

## 🔧 Running the Application

### Prerequisites
- Python 3.7 or higher
- tkinter (comes with Python)
- sqlite3 (comes with Python)

### Installation
```bash
# Clone or download the repository
cd FoodieExpress

# Run the GUI application
python Activity4/gui_application.py
```

### Testing
```bash
# Run test cases
python Activity4/test_cases.py

# Run algorithm demonstrations
python Activity1/algorithms.py
```

---

## 📊 System Specifications

**FoodieExpress Parameters:**
| Parameter | Value |
|-----------|-------|
| Delivery Rate | Rs. 50 per km |
| Maximum Distance | 20 km |
| Free Delivery | Orders above Rs. 5,000 |
| Premium Discount | 10% |
| VIP Discount | 20% |
| Output Format | 2 decimal places |

---

## 💾 Database Structure

### CUSTOMER Table
Stores customer information
```sql
CREATE TABLE CUSTOMER (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(100),
    CustomerType VARCHAR(20),
    CustomerPhone VARCHAR(15)
);
```

### ORDER Table
Stores order details and calculations
```sql
CREATE TABLE "ORDER" (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    NumberOfItems INT,
    PricePerItem DECIMAL(10, 2),
    FoodCost DECIMAL(10, 2),
    DeliveryDistance DECIMAL(5, 2),
    DeliveryCharge DECIMAL(10, 2),
    Discount DECIMAL(10, 2),
    TotalAmount DECIMAL(10, 2)
);
```

### DELIVERY Table
Tracks delivery information
```sql
CREATE TABLE DELIVERY (
    DeliveryID INT PRIMARY KEY,
    OrderID INT,
    DeliveryDistance DECIMAL(5, 2),
    DeliveryCharge DECIMAL(10, 2),
    DeliveryStatus VARCHAR(20)
);
```

---

## 🧪 Testing

### Test Cases Included:

**Test 1: Regular Customer**
- 2 items × Rs. 500 = Rs. 1,000 food
- Distance: 5 km = Rs. 250 delivery
- Total: Rs. 1,250

**Test 2: Premium Customer**
- 3 items × Rs. 400 = Rs. 1,200 food
- Distance: 3 km = Rs. 150 delivery
- Subtotal: Rs. 1,350
- Discount (10%): Rs. 135
- Total: Rs. 1,215

**Test 3: VIP Customer with Free Delivery**
- 15 items × Rs. 500 = Rs. 7,500 food
- Free delivery (food cost > Rs. 5,000)
- Discount (20%): Rs. 1,500
- Total: Rs. 6,000

**Test 4: Input Validation**
- Negative values rejected
- Distance > 20 km rejected
- Empty fields rejected
- Non-numeric input rejected

---

## 🐛 Debugging Tips

Common issues and fixes:

1. **Discount calculated incorrectly**
   - Make sure discount is on subtotal, not just food cost

2. **Free delivery not working**
   - Set `delivery_charge = 0` when food cost >= 5000

3. **Negative values accepted**
   - Add validation: `if value < 0: show error`

4. **Distance validation failing**
   - Check: `if distance > 20 or distance < 0`

See `Activity4/debugging_guide.md` for more details.

---

## 📝 Code Quality

### Good Practices Used:
- Clear variable names
- Input validation
- Error handling
- Comments for complex logic
- Functions organized by purpose
- Database integration
- Follows Python style guidelines

### Example:
```python
def calculate_order(items, price, distance, customer_type):
    """Calculate total order cost"""
    # Validate inputs
    if items <= 0 or price < 0 or distance > 20:
        return None
    
    # Calculate components
    food_cost = items * price
    delivery_charge = distance * 50 if food_cost < 5000 else 0
    subtotal = food_cost + delivery_charge
    
    # Apply discount
    discount = 0
    if customer_type == "Premium":
        discount = subtotal * 0.10
    elif customer_type == "VIP":
        discount = subtotal * 0.20
    
    # Return final total
    return subtotal - discount
```

---

## 📖 Learning Outcomes

After completing this project, you should understand:

✓ Algorithm design and Big-O analysis
✓ Different programming paradigms and their uses
✓ Database design and relationships
✓ GUI application development with Python
✓ Input validation and error handling
✓ Debugging techniques and practices
✓ Coding standards and best practices
✓ How to integrate databases with GUI applications

---

## 👤 Student
itzherath-jpg

## 📅 Date
2026-07-11

## 🎓 Course
BTEC Higher Nationals Computer Science

---

## 📌 Notes

- All code is written in Python for compatibility
- GUI uses tkinter (built-in with Python)
- Database uses SQLite (built-in with Python)
- All requirements from the assignment are covered
- Code is simple and easy to understand
- Well commented for learning purposes

---

## ✅ Assignment Checklist

- [x] Activity 1: Algorithm design and Big-O analysis
- [x] Activity 2: Programming paradigms explanation and examples
- [x] Activity 3: Database design and IDE features analysis
- [x] Activity 4: GUI application with validation and debugging
- [x] Input validation implemented
- [x] Cost calculations with discounts
- [x] Database integration
- [x] Test cases provided
- [x] Debugging guide included
- [x] Code comments and documentation

---

For questions about any activity, check the README.md file in that activity's folder.
