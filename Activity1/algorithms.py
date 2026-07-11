# Activity 1: Algorithms and Programming Process
# FoodieExpress Order Management System

def generate_order_sequence(num_days):
    """
    Generate order sequence where each day depends on previous two days.
    Pattern: 5, 8, 13, 21, 34, 55...
    Formula: O(n) = O(n-1) + O(n-2)
    """
    
    if num_days <= 0:
        return []
    
    if num_days == 1:
        return [5]
    
    orders = [5, 8]
    
    print("Order Growth Sequence:")
    print(f"Day 1: 5 orders")
    print(f"Day 2: 8 orders")
    
    for i in range(2, num_days):
        next_orders = orders[i-1] + orders[i-2]
        orders.append(next_orders)
        print(f"Day {i+1}: {next_orders} orders")
    
    return orders


def calculate_discounted_cost(base_price, discount_factors):
    """
    Calculate total cost by applying discount factors.
    Example: 100 * 0.9 * 0.8 * 0.7 = 50.4
    """
    
    total_cost = base_price
    
    print(f"\nBase Price: Rs. {base_price}")
    print(f"Discount Factors: {discount_factors}")
    print()
    
    for i, factor in enumerate(discount_factors):
        total_cost = total_cost * factor
        print(f"After Item {i+1}: Rs. {total_cost:.2f}")
    
    return round(total_cost, 2)


if __name__ == "__main__":
    print("=" * 50)
    print("ACTIVITY 1: ALGORITHMS")
    print("=" * 50)
    
    # Test Algorithm 1
    print("\nAlgorithm 1: Order Growth Sequence\n")
    orders = generate_order_sequence(8)
    print(f"\nGenerated Sequence: {orders}\n")
    
    # Test Algorithm 2
    print("\nAlgorithm 2: Discounted Cost Calculation\n")
    
    # Example 1
    print("Example 1:")
    result1 = calculate_discounted_cost(100, [0.9, 0.8, 0.7])
    print(f"Final Total: Rs. {result1}")
    
    print("\n" + "-" * 50)
    
    # Example 2
    print("\nExample 2:")
    result2 = calculate_discounted_cost(500, [0.95, 0.90])
    print(f"Final Total: Rs. {result2}")
