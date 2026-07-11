# Activity 4: Full System Build, Debugging, and Coding Standards

## 4.1 Build the FoodieExpress GUI System

The GUI system allows users to enter order details and calculate the total cost.

### System Requirements:

**Input Section:**
- Customer Name (text field)
- Order Type dropdown (Regular, Premium, VIP)
- Number of Items (number field)
- Price Per Item (number field)
- Delivery Distance (number field)

**Processing:**
- Validate all inputs
- Calculate food cost
- Calculate delivery charge
- Apply discounts
- Calculate final total

**Output Section:**
- Display itemized bill
- Show all calculations
- Display final amount

**Features:**
- Input validation (error messages for invalid data)
- Cost calculations (including delivery and discounts)
- Database integration (save orders to database)
- Delivery category validation (free delivery for orders > Rs. 5000)
- Discount eligibility (Premium 10%, VIP 20%)

---

## 4.2 Debugging Process

Debugging is finding and fixing errors in code.

### Common Errors in FoodieExpress:

#### Error 1: Incorrect Discount Calculation
**Problem:** Discount calculated on food cost instead of total
```python
# WRONG:
discount = food_cost * 0.1

# CORRECT:
discount = (food_cost + delivery_charge) * 0.1
```

**How to debug:**
- Add print statements to see values
- Use debugger to watch variables
- Check calculation step by step

#### Error 2: Delivery Charge Applied Twice
**Problem:** Delivery charge not zeroed when free delivery applies
```python
# WRONG:
if food_cost > 5000:
    free_delivery = True
# But delivery_charge still added

# CORRECT:
if food_cost > 5000:
    delivery_charge = 0
```

**How to debug:**
- Test with orders over Rs. 5000
- Check if delivery charge is included
- Fix the logic

#### Error 3: Input Validation Missing
**Problem:** Negative numbers accepted
```python
# WRONG:
price = float(price_entry.get())

# CORRECT:
price = float(price_entry.get())
if price < 0:
    show_error("Price must be positive")
    return
```

**How to debug:**
- Try entering invalid data
- Check error messages appear
- Verify invalid data rejected

### Debugging Steps:

1. **Identify the problem** - What's wrong?
2. **Reproduce the error** - Make it happen again
3. **Add debugging info** - Print values or use debugger
4. **Find the cause** - Where in code is problem?
5. **Fix the code** - Change the logic
6. **Test the fix** - Make sure it works
7. **Check nothing broke** - Test all features

### Example Debugging Session:

**Issue:** Total amount shows wrong

**Steps:**
1. Enter test data: Price 100, Distance 5, Regular
2. Expected: 100 + (5*50) = 350
3. Actual: 550 (Wrong!)
4. Add print statements:
   ```python
   print(f"Food cost: {food_cost}")
   print(f"Delivery: {delivery_charge}")
   print(f"Total: {total}")
   ```
5. Output shows: Food cost: 500 (should be 100)
6. Find bug: NumberOfItems field has 5
7. Expected only price per item
8. Check calculation: 5 items * 100 = 500 (calculation correct)
9. User error - entered wrong number
10. Test with correct data: Works!

---

## 4.3 Coding Standards

### Good Code Practices:

#### 1. Clear Variable Names
```python
# BAD:
x = y * 50

# GOOD:
delivery_charge = distance * DELIVERY_RATE
```

#### 2. Comments for Complex Logic
```python
# Calculate discount based on order type
if customer_type == "Premium":
    discount = total * 0.10  # 10% for premium
elif customer_type == "VIP":
    discount = total * 0.20  # 20% for VIP
else:
    discount = 0  # No discount for regular
```

#### 3. Use Constants for Fixed Values
```python
# Instead of hardcoding:
DELIVERY_RATE = 50  # Rs per km
FREE_DELIVERY_LIMIT = 5000  # Rs
PREMIUM_DISCOUNT = 0.10
VIP_DISCOUNT = 0.20
```

#### 4. Input Validation
```python
def validate_inputs(name, items, price, distance):
    if not name:
        return False, "Name cannot be empty"
    if items <= 0:
        return False, "Items must be positive"
    if price < 0:
        return False, "Price cannot be negative"
    if distance < 0 or distance > 20:
        return False, "Distance must be 0-20 km"
    return True, "Valid"
```

#### 5. Error Handling
```python
try:
    distance = float(distance_entry.get())
    if distance > 20:
        show_error("Maximum distance is 20 km")
except ValueError:
    show_error("Please enter valid number")
```

#### 6. Function Organization
```python
# Separate concerns into different functions
def calculate_food_cost(items, price):
    return items * price

def calculate_delivery_charge(distance, food_cost):
    if food_cost >= 5000:
        return 0
    return distance * 50

def calculate_discount(total, customer_type):
    # ...
    return discount

def calculate_final_total(food_cost, delivery, discount):
    return food_cost + delivery - discount
```

### Code Style Guidelines:

1. **Indentation:** Use 4 spaces
2. **Line length:** Keep under 80 characters
3. **Naming:** Use lowercase with underscores (food_cost, not foodCost)
4. **Comments:** Explain WHY, not WHAT
5. **Functions:** Keep short and focused
6. **Avoid:** Global variables, hardcoded values

### Example Good Code vs Bad Code:

**BAD:**
```python
def calc(a,b,c,d):
    x = a*b + c*50
    if x >= 5000:
        x = x - x*0.1
    return x
```

**GOOD:**
```python
def calculate_total_cost(items, price_per_item, distance, discount_type):
    """Calculate order total cost"""
    food_cost = items * price_per_item
    delivery_charge = calculate_delivery(distance, food_cost)
    discount = calculate_discount(food_cost + delivery_charge, discount_type)
    total = food_cost + delivery_charge - discount
    return total
```

---

## Summary

### To build the FoodieExpress system:
1. Create GUI with input fields
2. Add calculate button with calculation logic
3. Validate all inputs
4. Display results in clear format
5. Save to database

### To debug:
1. Identify problem
2. Add debug info (print or breakpoint)
3. Find root cause
4. Fix code
5. Test thoroughly

### Good coding practices:
- Clear variable names
- Helpful comments
- Input validation
- Error handling
- Organized functions
- Follow style guidelines
