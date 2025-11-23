expenses = [
    ["2025-11-23", "Food", 200, "Snacks"],
    ["2025-11-24", "Transport", 50, "Bus fare"]
]

def delete_expense_by_description(desc):
    for i, e in enumerate(expenses):
        if e[3] == desc:
            del expenses[i]
            print(f"Deleted expense with description: {desc}")
            return
    print("Expense not found.")

# Example usage
delete_expense_by_description("Snacks")
print("Current expenses:", expenses)
