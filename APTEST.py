import tkinter as tk
from tkinter import messagebox
class BudgetApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Budget App")
        self.geometry("300x250")

        self.budget = Budget()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Income:").grid(row=0, column=0, padx=10, pady=5)
        self.income_entry = tk.Entry(self)
        self.income_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self, text="Description of Expense:").grid(row=1, column=0, padx=10, pady=5)
        self.description_entry = tk.Entry(self)
        self.description_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self, text="Expense Amount:").grid(row=2, column=0, padx=10, pady=5)
        self.amount_entry = tk.Entry(self)
        self.amount_entry.grid(row=2, column=1, padx=10, pady=5)

        self.add_income_button = tk.Button(self, text="Add Income", command=self.add_income)
        self.add_income_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        self.add_expense_button = tk.Button(self, text="Add Expense", command=self.add_expense)
        self.add_expense_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

        self.print_summary_button = tk.Button(self, text="Print Budget Summary", command=self.print_summary)
        self.print_summary_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

        self.reset_button = tk.Button(self, text="Reset", command=self.reset_data)
        self.reset_button.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

    def add_income(self):
        try:
            income = float(self.income_entry.get())
            if income > 0:
                self.budget.add_income(income)
                messagebox.showinfo("Success", "Income added successfully!")
            else:
                messagebox.showinfo("Failed", "Enter a postive number!")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid income amount.")

    def add_expense(self):
        try:
            expenses = self.parse_expenses()
            if expenses:
                for description, amount in expenses:
                  self.budget.add_expense(description, amount)
                messagebox.showinfo("Success", "Expenses added successfully!")
            else:
                messagebox.showerror("Error", "Please enter valid expenses.")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid expense amounts.")

    def parse_expenses(self):
        description = self.description_entry.get()
        amounts = self.amount_entry.get().split(",")
        expenses = []
        for amount in amounts:
            amount = amount.strip()
            if amount:
                try:
                    amount = float(amount)
                    if amount > 0:
                        expenses.append((description, amount))
                    else:
                        return None
                except ValueError:
                    return None
        return expenses

    def print_summary(self):
        summary = self.budget.get_summary()
        messagebox.showinfo("Budget Summary", summary)

    def reset_data(self):
        self.budget.reset()
        messagebox.showinfo("Success", "Data reset successfully.")

class Budget:
    def __init__(self):
        self.reset()

    def reset(self):
        self.income = 0
        self.expenses = []

    def add_income(self, amount):
        self.income += amount

    def add_expense(self, description, amount):
        self.expenses.append((description, amount))

    def calculate_total_expenses(self):
        return sum(amount for description, amount in self.expenses)

    def calculate_remaining_budget(self):
        return self.income - self.calculate_total_expenses()
    def get_summary(self):
        summary = "Budget Summary:\n"
        summary += f"Income: ${self.income}\n"
        summary += "Expenses:\n"
        for description, amount in self.expenses:
            summary += f"- {description}: ${amount}\n"
        summary += f"Total Expenses: ${self.calculate_total_expenses()}\n"
        summary += f"Remaining Budget: ${self.calculate_remaining_budget()}"
        return summary
        
if __name__ == "__main__":
    app = BudgetApp()
    app.mainloop()
