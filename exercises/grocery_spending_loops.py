"""
This script demonstrates Python loop and sequence concepts including:
- Iteration with zip()
- Conditional flow control using continue
- Accumulating values for later aggregation
- Identifying entries that exceed a threshold
- Summing selected values from a sequence
"""


# List of grocery stores and corresponding weekly spending amounts
stores = ["Walmart", "Target", "Costco", "Aldi", "Trader Joe's"]
spending = [32, 0, 87, 24, 120]

# Holds only valid spending amounts we actually process
valid_spending = []

# Will store all stores where spending exceeds $100 
over_100_stores = []                         

# Loop through stores and spending together, with a 1-based index
for name, amount in zip(stores, spending):     

    # Skip stores where no money was spent
    if amount == 0:
        continue

    # Record stores where spending exceeds $100                            
    if amount > 100:
        over_100_stores.append((name, amount))                      
        continue                               

    # Record valid spending and print formatted output
    valid_spending.append(amount)
    print(f'{name}: ${amount}')

# Calculate total spending from processed values
total = sum(valid_spending)
print(f'Total spending: ${total}')

# Report stores that exceeded $100
if over_100_stores:
    print('Spending exceeded $100 at:')
    for name, amount in over_100_stores:
        print(f' - {name} (${amount})')
        


