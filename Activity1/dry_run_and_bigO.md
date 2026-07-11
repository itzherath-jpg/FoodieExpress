# Activity 1.3 - Dry Run and Big-O Analysis

## Algorithm 1: Order Sequence Dry Run

### Input: Generate sequence for 6 days

| Day | Formula | Calculation | Output |
|-----|---------|-------------|--------|
| 1 | Base Case | - | 5 |
| 2 | Base Case | - | 8 |
| 3 | O(1) + O(2) | 5 + 8 | 13 |
| 4 | O(2) + O(3) | 8 + 13 | 21 |
| 5 | O(3) + O(4) | 13 + 21 | 34 |
| 6 | O(4) + O(5) | 21 + 34 | 55 |

**Final Output:** [5, 8, 13, 21, 34, 55]

---

## Algorithm 2: Discounted Cost Dry Run

### Example: Calculate cost with discounts

**Input:**
- Base Price: Rs. 100
- Discount Factors: [0.9, 0.8, 0.7]

| Step | Calculation | Result |
|------|-------------|--------|
| Start | total = 100 | 100 |
| Item 1 | 100 × 0.9 | 90 |
| Item 2 | 90 × 0.8 | 72 |
| Item 3 | 72 × 0.7 | 50.4 |

**Final Output:** Rs. 50.4

---

## Big-O Notation Analysis

### What is Big-O?
Big-O notation describes how the runtime or space grows as input size increases. It helps us understand algorithm efficiency.

### Common Big-O Classes:
- O(1) - Constant: Always takes same time
- O(log n) - Logarithmic: Cuts problem in half each time
- O(n) - Linear: Time grows with input size
- O(n²) - Quadratic: Two nested loops
- O(2ⁿ) - Exponential: Very slow

---

## Algorithm 1: Time Complexity

### Analysis:
```
ALGORITHM GenerateOrderSequence(n):
    - Create array: O(1)
    - Set first two values: O(1)
    - FOR loop runs (n-2) times: O(n)
    - Inside loop: addition and assignment: O(1)
    - Total loop: (n-2) × O(1) = O(n)
```

**Time Complexity: O(n) - LINEAR**

### Why?
The loop runs n times, and each operation inside is constant. So it grows linearly with input.

---

## Algorithm 1: Space Complexity

### Analysis:
```
- Array to store n values: O(n)
- Variables (i, temp): O(1)
- Total: O(n)
```

**Space Complexity: O(n) - LINEAR**

### Why?
We need to store all n values in the array.

---

## Algorithm 2: Time Complexity

### Analysis:
```
ALGORITHM CalculateDiscountedCost(price, factors):
    - Set total = price: O(1)
    - FOR loop runs m times (m = number of factors): O(m)
    - Inside loop: multiplication and assignment: O(1)
    - Total loop: m × O(1) = O(m)
```

**Time Complexity: O(m) - LINEAR**

### Why?
The loop runs once for each discount factor, and each operation is constant.

---

## Algorithm 2: Space Complexity

### Analysis:
```
- Variable total: O(1)
- Variable i, factor: O(1)
- Input array (not counted): Already provided
- Total: O(1)
```

**Space Complexity: O(1) - CONSTANT**

### Why?
We only use a few variables, no matter how many discount factors we have.

---

## Efficiency Comparison

### Order Sequence:
- **Iterative:** O(n) time - Good for practical use
- **Recursive:** O(2ⁿ) time - Too slow for n > 30

Iterative is much better.

### Discounted Cost:
- **Our approach:** O(m) time, O(1) space - Optimal
- **No better solution exists** for this problem

---

## Conclusion

Both algorithms:
- ✓ Have acceptable complexity for business use
- ✓ Scale reasonably well
- ✓ Are efficient implementations
- ✓ Follow best practices for the problem type
