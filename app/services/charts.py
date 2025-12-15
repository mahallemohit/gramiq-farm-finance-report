import matplotlib.pyplot as plt


def generate_expense_chart(expenses, output_path):
    """
    Generates a pie chart for expense distribution
    and saves it as an image.
    """

    category_totals = {}

    for expense in expenses:
        category_totals[expense.category] = (
            category_totals.get(expense.category, 0) + expense.amount
        )

    # If no expenses, do not generate chart
    if not category_totals:
        return None

    plt.figure(figsize=(5, 5))
    plt.pie(
        category_totals.values(),
        labels=category_totals.keys(),
        autopct="%1.1f%%",
        startangle=140
    )
    plt.title("Expense Distribution")

    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

    return output_path
