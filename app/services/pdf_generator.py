from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader
from datetime import datetime
import os


def generate_pdf(data, summary, chart_path, output_path):
    """
    Generates PDF report using HTML template
    """

    # Setup Jinja2 environment
    env = Environment(loader=FileSystemLoader("app/templates"))
    template = env.get_template("report.html")

    # Create ledger (merged income + expense)
    ledger = []

    for expense in data.expenses:
        ledger.append({
            "date": expense.date,
            "particulars": expense.category,
            "type": "Expense",
            "description": expense.description,
            "amount": expense.amount
        })

    for income in data.incomes:
        ledger.append({
            "date": income.date,
            "particulars": income.category,
            "type": "Income",
            "description": income.description,
            "amount": income.amount
        })

    # Sort ledger by date
    ledger.sort(key=lambda x: x["date"])

    # Render HTML
    html_content = template.render(
        data=data,
        summary=summary,
        ledger=ledger,
        chart_path=chart_path,
        generated_on=datetime.now().strftime("%d-%m-%Y %H:%M")
    )

    # Generate PDF
    HTML(
        string=html_content,
        base_url=os.getcwd()
    ).write_pdf(output_path)
