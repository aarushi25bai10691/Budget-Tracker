# utils.py
def validate_category(category):
    valid_categories = ['Food', 'Rent', 'Entertainment', 'Utilities', 'Transport', 'Other']
    if category not in valid_categories:
        print("Invalid category! Choose from:", valid_categories)
        return False
    return True
