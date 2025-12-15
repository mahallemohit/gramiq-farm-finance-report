def calculate_summary(expenses, incomes, total_acres):
    """
    Calculates finance summary for the farm report
    """

    total_expense = sum(e.amount for e in expenses)
    total_income = sum(i.amount for i in incomes)

    profit_or_loss = total_income - total_expense

    cost_per_acre = 0
    if total_acres > 0:
        cost_per_acre = total_expense / total_acres

    return {
        "total_income": round(total_income, 2),
        "total_expense": round(total_expense, 2),
        "profit_or_loss": round(profit_or_loss, 2),
        "cost_per_acre": round(cost_per_acre, 2)
    }
