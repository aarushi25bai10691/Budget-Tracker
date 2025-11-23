# Budget Tracker Project 💰

### Submitted by: Aarushi Chauhan | 25BAI10691

## 📖 Project Overview
This is a Python-based command-line application developed as part of a Python programming course. It helps users track and manage their daily expenses by allowing them to add, categorize, and summarize spending. The project demonstrates modular programming, input validation, and basic file handling in Python for budget management.

## ✨ Features
* **Expense Management:** Add expenses with date, category, amount, and description.
* **Data Persistence:** Stores expenses in a plain text file for future use.
* **Summary Reports:** Displays total expenses grouped by category.
* **User-Friendly CLI:** Simple menu-driven interface for easy navigation.
* **Modular Source Code:** Logic separated into multiple maintainable Python files.

## 📂 Project Structure
The project is organized for clarity and maintainability:
* `source_code/`
    * `main.py`: Main script with the application menu.
    * `expense_manager.py`: Handles loading, saving, and adding expenses.
    * `summarizer.py`: Creates summary reports by category.
    * `validator.py`: Validates each entered category.
    * `expenses.txt`: Plain text file storing all expense records (created automatically).
* `statement.md`: Contains the problem statement, project scope, target users, and features.

## 🛠️ Technology Stack
* **Language:** Python 3  
* **Concepts Used:** Modular Programming, Lists, Dictionaries, Exception Handling, File I/O.

## 🚀 Steps to Install & Run
1. Clone the repository:
    ```
    git clone https://github.com/yourusername/budget-tracker.git
    ```
2. Navigate to the source code directory:
    ```
    cd source_code
    ```
3. Run the application:
    ```
    python main.py
    ```
4. Follow the on-screen prompts to add expenses and view summaries.

## ✔️ Instructions for Testing
Test the application by entering these cases using option 1 ("Add Expense"):
1. **Case 1:**  
   - Date: `2025-11-23`, Category: `Food`, Amount: `1500`, Description: `Lunch at cafe`
2. **Case 2:**  
   - Date: `2025-11-22`, Category: `Transport`, Amount: `80`, Description: `Metro ticket`
3. **Case 3:**  
   - Date: `2025-11-21`, Category: `Utilities`, Amount: `900`, Description: `Electricity bill`
4. **Case 4:**  
   - Date: `2025-11-20`, Category: `Entertainment`, Amount: `400`, Description: `Concert ticket`
5. **Case 5:**  
   - Date: `2025-11-19`, Category: `Rent`, Amount: `9000`, Description: `Apartment rent`

Use "View All" to see the complete expense list and "Show Summary" for the categorized report. Invalid input (wrong category or non-numeric amount) will trigger validation errors.

## 📸 Screenshots
*(screenshots are in the /assets` directory to demonstrate input/output examples and summaries.)*

