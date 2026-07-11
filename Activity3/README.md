# Activity 3 - Database Design and IDE Implementation

## 3.1 Pseudocode and GUI Implementation

Based on the FoodieExpress scenario, I need to create a system that:
- Takes customer order details
- Calculates costs including delivery and discounts
- Shows the final bill

### Pseudocode for Order Calculation:

```
START
    Read customer name
    Read order type (Regular, Premium, VIP)
    Read number of items
    Read price per item
    Read delivery distance
    
    Calculate food cost = number of items * price per item
    
    If distance > 20 km
        Print error message
    Else
        Calculate delivery charge = distance * 50
        
        If food cost >= 5000
            delivery charge = 0
        End if
        
        Calculate subtotal = food cost + delivery charge
        
        If order type is Premium
            discount = subtotal * 0.10
        Else if order type is VIP
            discount = subtotal * 0.20
        Else
            discount = 0
        End if
        
        Calculate final total = subtotal - discount
        
        Display receipt with all details
    End if
END
```

### Input Validation:
- Customer name should not be empty
- Price and distance should be positive numbers
- Distance should be between 0 and 20 km
- Number of items should be positive integer

### GUI Elements Needed:
- Text field for customer name
- Dropdown for order type
- Text field for number of items
- Text field for price per item
- Text field for delivery distance
- Calculate button
- Display area for receipt/bill

---

## 3.2 Database Design

The FoodieExpress system needs to store three types of information:

### Table 1: CUSTOMER
Stores information about customers

```sql
CREATE TABLE CUSTOMER (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,
    CustomerName VARCHAR(100) NOT NULL,
    CustomerPhone VARCHAR(15) NOT NULL,
    CustomerType VARCHAR(20),
    Email VARCHAR(100)
);
```

**Columns:**
- CustomerID: Unique ID for each customer (Primary Key)
- CustomerName: Name of customer
- CustomerPhone: Phone number for contact
- CustomerType: Whether Regular, Premium, or VIP
- Email: Email address

**Why:** To keep track of all customers and their discount levels

---

### Table 2: ORDER
Stores order information

```sql
CREATE TABLE "ORDER" (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,
    CustomerID INT NOT NULL,
    OrderDate DATE,
    NumberOfItems INT,
    PricePerItem DECIMAL(10, 2),
    FoodCost DECIMAL(10, 2),
    DeliveryDistance DECIMAL(5, 2),
    DeliveryCharge DECIMAL(10, 2),
    Discount DECIMAL(10, 2),
    TotalAmount DECIMAL(10, 2),
    FOREIGN KEY (CustomerID) REFERENCES CUSTOMER(CustomerID)
);
```

**Columns:**
- OrderID: Unique order number
- CustomerID: Which customer placed order (links to CUSTOMER table)
- OrderDate: When order was placed
- NumberOfItems: How many items
- PricePerItem: Cost of each item
- FoodCost: Total food cost
- DeliveryDistance: How far to deliver
- DeliveryCharge: Delivery fee
- Discount: Amount discounted
- TotalAmount: Final bill

**Why:** To keep record of all orders and calculate costs

---

### Table 3: DELIVERY
Stores delivery information

```sql
CREATE TABLE DELIVERY (
    DeliveryID INT PRIMARY KEY AUTO_INCREMENT,
    OrderID INT NOT NULL,
    DeliveryDistance DECIMAL(5, 2),
    DeliveryCharge DECIMAL(10, 2),
    DeliveryStatus VARCHAR(20),
    FOREIGN KEY (OrderID) REFERENCES "ORDER"(OrderID)
);
```

**Columns:**
- DeliveryID: Unique delivery number
- OrderID: Which order to deliver (links to ORDER table)
- DeliveryDistance: How far
- DeliveryCharge: Delivery fee (distance * 50)
- DeliveryStatus: Pending, In Transit, or Delivered

**Why:** To track where deliveries are and manage delivery costs

---

## How Tables Relate

```
CUSTOMER Table
    |
    |-- Has Many Orders
    |
    v
ORDER Table
    |
    |-- Has One Delivery
    |
    v
DELIVERY Table
```

- One customer can have multiple orders
- One order has one delivery
- CustomerID in ORDER table refers to CustomerID in CUSTOMER table (Foreign Key)
- OrderID in DELIVERY table refers to OrderID in ORDER table (Foreign Key)

---

## 3.3 IDE Features Analysis

### What is an IDE?
An IDE is software that helps you write code. It has tools for writing, testing, and fixing code all in one place.

### Main IDE Features:

#### 1. Code Completion
When you start typing, the IDE suggests code completions.

**Example:**
```python
class Order:
    def calc  # IDE suggests: calculate_total, calculate_discount
```

**Advantage:** Helps you write faster and prevents spelling mistakes

#### 2. Debugging Tools
Helps find errors in your code.

**Features:**
- Set breakpoints (pause at specific lines)
- Watch variables (see their values)
- Step through code (run line by line)

**Advantage:** Find bugs quickly instead of guessing

#### 3. UI Design Tools
Drag and drop to create user interfaces visually.

**Advantage:** Don't have to write all the GUI code manually

#### 4. Syntax Highlighting
Colors different parts of code (keywords, strings, comments)

**Advantage:** Easier to read and spot errors

### Comparing IDEs: VS Code vs PyCharm

| Feature | VS Code | PyCharm |
|---------|---------|----------|
| Easy to use | Yes | Yes but more complex |
| Speed | Very fast | Slower (uses more memory) |
| Cost | Free | Free for community edition |
| Debugging | Good | Excellent |
| GUI Designer | No | Yes |
| Code Completion | Good | Excellent |

**For beginners:** VS Code is easier
**For professionals:** PyCharm has more features

### Advantages of Using IDE:

1. **Faster coding** - auto-complete and templates
2. **Find bugs easier** - debugging tools
3. **Better organization** - file explorer and search
4. **Less errors** - real-time error checking
5. **Professional tools** - version control, testing

### Without IDE (Manual Coding):

Without an IDE, you would:
- Write code in basic text editor
- Must remember all syntax yourself
- Find errors by running and checking output
- Use print statements to debug
- Manually manage files
- No auto-complete or suggestions

This takes much longer and is error-prone.

### Conclusion:

Using an IDE like VS Code or PyCharm:
- Saves time
- Reduces errors
- Makes debugging easier
- Essential for professional development

For FoodieExpress project, I recommend **VS Code** (easy to learn) or **PyCharm Community Edition** (more powerful).
