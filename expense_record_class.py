from file_io import save_data, load_data

class ExpenseRecord:
    """
    Represents the list of expenses from the landlord.
    """
    def __init__(self, expense_filename='expense_records.txt'):
        """
        Constructs a list for the expense record to hold the 
        information for each expense.

        expense_filename: The filename that contains the expense records
        expense_records: The list of expenses 
        """
        self.expense_filename = expense_filename
        self.expense_records = load_data(self.expense_filename)

    def add_expense(self, date, payee, amount, category):
        """
        Appends a dictionary of data for each expense payment to
        the list and saves it into a txt file.

        date: The date of the payment
        payee: Company or person paid by landlord
        amount: The amount payed by the tenant
        category: The type of expense (mortgage, repairs, utilities, etc.)
        """
        expense = {
            "date": date,
            "payee": payee,
            "amount": amount,
            "category": category
        }
        self.expense_records.append(expense)
        save_data(self.expense_filename, self.expense_records)

    def get_total_expenses(self):
        """
        Calculates the sum of the total expenses in the expense record.
        """
        return sum([record['amount'] for record in self.expense_records])

    def get_total_expenses_by_category(self, category):
        """
        Calculates the sum of the total expenses for a single category
        passed as a parameter.

        category: The category to calculate the sum for
        """

        # Iterate through the expense records, and if the input category matches, add to sum
        return sum(expense['amount'] for expense in self.expense_records if expense['category'] == category)