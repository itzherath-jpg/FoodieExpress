# Activity 1.1 - Define an Algorithm and Outline the Programming Process

## What is an Algorithm?

An algorithm is a step-by-step procedure or set of instructions designed to solve a specific problem or perform a task. It's a logical sequence of actions that, when followed, will produce a desired outcome.

## Characteristics of a Good Algorithm

1. **Clarity** - Easy to understand and follow
2. **Efficiency** - Uses minimal time and resources
3. **Correctness** - Produces accurate results
4. **Finiteness** - Must terminate after a finite number of steps
5. **Generality** - Works for different input values
6. **Effectiveness** - Each step must be doable

---

## Pseudocode Algorithm 1: Order Growth Sequence

### Problem:
Generate a sequence of daily orders where each day depends on the previous two days.
Pattern: 5, 8, 13, 21, 34, 55...
Formula: O(n) = O(n-1) + O(n-2)

### Pseudocode:
```
ALGORITHM GenerateOrderSequence(num_days)
    INPUT: number of days
    OUTPUT: array of order values
    
    IF num_days < 1 THEN
        RETURN empty array
    END IF
    
    CREATE orders array of size num_days
    orders[0] = 5
    orders[1] = 8
    
    FOR i = 2 to num_days - 1 DO
        orders[i] = orders[i-1] + orders[i-2]
        PRINT "Day " + i + ": " + orders[i] + " orders"
    END FOR
    
    RETURN orders
END ALGORITHM
```

---

## Pseudocode Algorithm 2: Calculate Discounted Cost

### Problem:
Calculate total cost by multiplying base price by decreasing discount factors.
Example: 100 × 0.9 × 0.8 × 0.7 = 50.4

### Pseudocode:
```
ALGORITHM CalculateDiscountedCost(basePrice, discountFactors)
    INPUT: base price, array of discount factors
    OUTPUT: final cost after discounts
    
    total = basePrice
    
    FOR i = 0 to length(discountFactors) - 1 DO
        total = total * discountFactors[i]
        PRINT "After item " + i + ": " + total
    END FOR
    
    RETURN total
END ALGORITHM
```

---

## Programming Process: Steps from Writing Code to Execution

### Step 1: Problem Analysis
- Understand what needs to be solved
- Identify inputs and expected outputs
- Define constraints and requirements

### Step 2: Algorithm Design
- Break problem into smaller steps
- Create logical flow
- Consider different approaches

### Step 3: Write Pseudocode
- Write platform-independent logic
- Make it clear and understandable
- Follow logical structure

### Step 4: Implementation
- Translate pseudocode to programming language (Python)
- Write actual code
- Follow syntax rules

### Step 5: Compilation/Interpretation
- Parser reads the code
- Checks for syntax errors
- Converts to machine-readable form

### Step 6: Execution
- Program runs on computer
- Variables are created in memory
- Statements execute in order

### Step 7: Testing
- Run with sample values
- Check if output is correct
- Verify against expected results

### Step 8: Debugging
- Find and fix errors
- Handle edge cases
- Optimize if needed

---

## Challenges During Development

1. **Off-by-One Errors** - Loop starting or ending at wrong position
2. **Incorrect Base Cases** - Not handling starting values properly
3. **Variable Scope Issues** - Variables not accessible where needed
4. **Type Mismatches** - Using wrong data types
5. **Logic Errors** - Algorithm doesn't produce correct output
6. **Memory Issues** - Not enough space for large arrays
7. **Infinite Loops** - Loop condition never becomes false

---

## Programming Process Diagram

```
        START
          |
          v
   Read Requirements
          |
          v
   Design Algorithm
          |
          v
   Write Pseudocode
          |
          v
   Code Implementation
          |
          v
   Syntax Check
          |
          v
     Run Program
          |
          v
    Test with Data
          |
          v
   Bugs Found? --Yes--> Debug & Fix -->
          |                  ^
         No                   |
          |                   |
          v                   |
   Output Correct? --No----->
          |
         Yes
          |
          v
        END
```