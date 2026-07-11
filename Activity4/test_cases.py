# Testing the FoodieExpress Application
# Simple test cases

import sqlite3
from datetime import datetime

def test_calculations():
    """Test different order calculations"""
    
    print("Testing FoodieExpress Order Calculations\n")
    print("=" * 50)
    
    # Test Case 1: Regular customer
    print("\nTest 1: Regular Customer Order")
    items = 2
    price_per_item = 500
    distance = 5
    customer_type = "Regular"
    
    food_cost = items * price_per_item
    delivery_charge = distance * 50
    subtotal = food_cost + delivery_charge
    discount = 0
    total = subtotal - discount
    
    print(f"Items: {items}, Price: Rs. {price_per_item}")
    print(f"Food Cost: Rs. {food_cost}")
    print(f"Delivery (Distance: {distance}km): Rs. {delivery_charge}")
    print(f"Discount: Rs. {discount}")
    print(f"Total: Rs. {total}")
    
    # Test Case 2: Premium customer
    print("\n" + "=" * 50)
    print("\nTest 2: Premium Customer Order (10% discount)")
    items = 3
    price_per_item = 400
    distance = 3
    customer_type = "Premium"
    
    food_cost = items * price_per_item
    delivery_charge = distance * 50
    subtotal = food_cost + delivery_charge
    discount = subtotal * 0.10
    total = subtotal - discount
    
    print(f"Items: {items}, Price: Rs. {price_per_item}")
    print(f"Food Cost: Rs. {food_cost}")
    print(f"Delivery (Distance: {distance}km): Rs. {delivery_charge}")
    print(f"Subtotal: Rs. {subtotal}")
    print(f"Discount (10%): Rs. {discount:.2f}")
    print(f"Total: Rs. {total:.2f}")
    
    # Test Case 3: VIP customer with free delivery
    print("\n" + "=" * 50)
    print("\nTest 3: VIP Customer with Free Delivery (20% discount)")
    items = 15
    price_per_item = 500
    distance = 10
    customer_type = "VIP"
    
    food_cost = items * price_per_item
    if food_cost >= 5000:
        delivery_charge = 0
        free_delivery = "YES"
    else:
        delivery_charge = distance * 50
        free_delivery = "NO"
    
    subtotal = food_cost + delivery_charge
    discount = subtotal * 0.20
    total = subtotal - discount
    
    print(f"Items: {items}, Price: Rs. {price_per_item}")
    print(f"Food Cost: Rs. {food_cost}")
    print(f"Free Delivery Applied: {free_delivery}")
    print(f"Delivery Charge: Rs. {delivery_charge}")
    print(f"Subtotal: Rs. {subtotal}")
    print(f"Discount (20%): Rs. {discount:.2f}")
    print(f"Total: Rs. {total:.2f}")
    
    # Test Case 4: Input validation
    print("\n" + "=" * 50)
    print("\nTest 4: Input Validation Testing")
    
    test_inputs = [
        ("Ahmed Khan", 5, 200, 5, True),  # Valid
        ("Fatima Ali", -2, 300, 5, False),  # Negative items
        ("Hassan", 3, -100, 5, False),  # Negative price
        ("Ali", 2, 200, 25, False),  # Distance > 20
        ("", 3, 200, 5, False),  # Empty name
    ]
    
    for name, items, price, distance, expected_valid in test_inputs:
        valid = True
        if not name:
            valid = False
        if items <= 0:
            valid = False
        if price < 0:
            valid = False
        if distance < 0 or distance > 20:
            valid = False
        
        status = "PASS" if valid == expected_valid else "FAIL"
        print(f"Input: Name='{name}', Items={items}, Price={price}, Distance={distance}")
        print(f"Valid: {valid}, Expected: {expected_valid} - {status}")
    
    print("\n" + "=" * 50)
    print("\nAll tests completed!")

if __name__ == "__main__":
    test_calculations()
