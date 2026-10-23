import time
import random

# --- PoC Scenario Setup ---
# Simulate a dataset of products. In a real PoC, this might come from a mock API or database.
products = []
for i in range(100000):
    products.append({
        "id": i,
        "name": f"Product {i}",
        "price": round(random.uniform(10, 1000), 2),
        "in_stock": random.choice([True, False]),
        "category": random.choice(["Electronics", "Books", "Home", "Clothing"])
    })

# Define the core requirement for this PoC: Calculate the total value of all in-stock products.
print("--- Proof of Concept (PoC): In-Stock Product Value Calculation ---")
print("Requirement: Efficiently calculate the total monetary value of all products currently in stock.")
print(f"Dataset size: {len(products)} products.\n")

# --- PoC Approach 1: Imperative Loop ---
# This approach uses a traditional for loop and conditional statements.
print("PoC 1: Imperative Loop Approach")
start_time_1 = time.perf_counter()
total_value_1 = 0
in_stock_count_1 = 0
for product in products:
    if product["in_stock"]:
        total_value_1 += product["price"]
        in_stock_count_1 += 1
end_time_1 = time.perf_counter()
duration_1 = (end_time_1 - start_time_1) * 1000 # Convert to milliseconds

print(f"  Total in-stock products: {in_stock_count_1}")
print(f"  Total value (PoC 1): ${total_value_1:.2f}")
print(f"  Execution time (PoC 1): {duration_1:.4f} ms\n")

# --- PoC Approach 2: Functional with List Comprehension ---
# This approach leverages Python's functional features like list comprehensions and sum().
print("PoC 2: Functional with List Comprehension Approach")
start_time_2 = time.perf_counter()
# First, filter the products that are in stock
in_stock_products_2 = [p for p in products if p["in_stock"]]
# Then, sum their prices
total_value_2 = sum(p["price"] for p in in_stock_products_2)
end_time_2 = time.perf_counter()
duration_2 = (end_time_2 - start_time_2) * 1000 # Convert to milliseconds

print(f"  Total in-stock products: {len(in_stock_products_2)}")
print(f"  Total value (PoC 2): ${total_value_2:.2f}")
print(f"  Execution time (PoC 2): {duration_2:.4f} ms\n")

# --- PoC Evaluation ---
# Compare the results and performance of the different approaches.
print("--- PoC Evaluation ---")
print("Both approaches successfully calculated the total value of in-stock products.")
print(f"PoC 1 (Imperative) execution time: {duration_1:.4f} ms")
print(f"PoC 2 (Functional) execution time: {duration_2:.4f} ms")

if duration_1 < duration_2:
    print(f"Conclusion: PoC 1 (Imperative) was slightly faster by {abs(duration_1 - duration_2):.4f} ms.")
elif duration_2 < duration_1:
    print(f"Conclusion: PoC 2 (Functional) was slightly faster by {abs(duration_1 - duration_2):.4f} ms.")
else:
    print("Conclusion: Both approaches had very similar performance.")

print("\nAdditional PoC Considerations (beyond just performance):")
print("- Readability: PoC 2 (Functional) is often considered more concise and Pythonic for this task.")
print("- Maintainability: Functional approaches can sometimes lead to more predictable and maintainable code.")
print("- Resource Usage: PoC 2 creates an intermediate list, potentially using more memory for very large datasets.")
print("The 'best' choice depends on project priorities (e.g., raw performance vs. code clarity, team familiarity).")