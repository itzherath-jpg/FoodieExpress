# Debugging Guide for FoodieExpress Application

## Common Issues and How to Fix Them

### Issue 1: Discount calculated on food cost instead of total

**Problem Code:**
```python
discount = food_cost * 0.10
```

**Why it's wrong:**
Discount should be on the total (food + delivery), not just food.

**Correct Code:**
```python
subtotal = food_cost + delivery_charge
discount = subtotal * 0.10
```

**How to debug:**
- Order: 2 items × Rs 500 = Rs 1000 food
- Delivery: 5 km × Rs 50 = Rs 250
- Subtotal: Rs 1250
- Premium discount should be: Rs 1250 × 0.10 = Rs 125
- If you see Rs 100, it means discount was on food cost only

---

### Issue 2: Free delivery not working

**Problem Code:**
```python
if food_cost > 5000:
    print("Free delivery")
# But delivery_charge still calculated
```

**Why it's wrong:**
You need to actually set delivery_charge to 0.

**Correct Code:**
```python
if food_cost >= 5000:
    delivery_charge = 0
else:
    delivery_charge = distance * 50
```

**How to debug:**
- Order: Rs 5500 food + Rs 300 km distance
- With bug: Shows Rs 5500 + Rs 300 = Rs 5800 (wrong)
- Fixed: Shows Rs 5500 + Rs 0 = Rs 5500 (correct)

---

### Issue 3: Negative numbers accepted

**Problem Code:**
```python
price = float(price_entry.get())
food_cost = items * price
```

**Why it's wrong:**
No validation of input values.

**Correct Code:**
```python
try:
    price = float(price_entry.get())
    if price < 0:
        messagebox.showerror("Error", "Price cannot be negative")
        return
except ValueError:
    messagebox.showerror("Error", "Please enter valid number")
    return
```

**How to debug:**
- Try entering: price = -100
- With bug: Accepts it and shows negative total
- Fixed: Shows error message

---

### Issue 4: Distance validation

**Problem Code:**
```python
if distance > 20:
    print("Too far")
# But still calculates
```

**Correct Code:**
```python
if distance < 0 or distance > 20:
    messagebox.showerror("Error", "Distance must be 0-20 km")
    return
```

---

## Debugging Methods

### Method 1: Print Statements

Add prints to see what values are being used:

```python
food_cost = items * price
print(f"Items: {items}, Price: {price}")
print(f"Food Cost: {food_cost}")

delivery_charge = distance * 50
print(f"Distance: {distance}, Delivery: {delivery_charge}")

subtotal = food_cost + delivery_charge
print(f"Subtotal: {subtotal}")
```

### Method 2: Test with Known Values

Use simple numbers to verify calculations:

```python
# Test: 2 items × Rs 100 = Rs 200 food
# 2 km × Rs 50 = Rs 100 delivery
# Subtotal = Rs 300
# Premium (10%) = Rs 30 discount
# Total = Rs 270

items = 2
price = 100
distance = 2
customer_type = "Premium"

# Run and check if total is 270
```

### Method 3: Step Through Code

Mentally execute code line by line:

```
Line 1: items = 3
Line 2: price = 500
Line 3: food_cost = 3 * 500 = 1500 ✓
Line 4: distance = 5
Line 5: delivery_charge = 5 * 50 = 250 ✓
Line 6: subtotal = 1500 + 250 = 1750 ✓
Line 7: discount = 1750 * 0.10 = 175 ✓
Line 8: total = 1750 - 175 = 1575 ✓
```

---

## Testing Checklist

- [ ] Regular customer order calculates correctly
- [ ] Premium customer gets 10% discount
- [ ] VIP customer gets 20% discount
- [ ] Free delivery works for orders > Rs 5000
- [ ] Distance validation works (0-20 km)
- [ ] Negative numbers rejected
- [ ] Empty fields show error
- [ ] Non-numeric input shows error
- [ ] Discount calculated on subtotal, not just food
- [ ] Database saves orders
- [ ] Bill displays correctly
- [ ] Clear button resets all fields

---

## Quick Bug Fixes

| Bug | Quick Fix |
|-----|----------|
| Discount wrong | Change to `subtotal * rate` not `food_cost * rate` |
| Free delivery not working | Set `delivery_charge = 0` in if statement |
| Accepts negative numbers | Add validation: `if price < 0: return` |
| Distance check fails | Use `and` not `or`: `if distance < 0 or distance > 20` |
| Database error | Make sure SQLite is installed |
| GUI not showing | Check `root.mainloop()` at end |
