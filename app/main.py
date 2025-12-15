from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

from app.schemas import FarmData
from app.services.calculations import calculate_summary
from app.services.charts import generate_expense_chart
from app.services.pdf_generator import generate_pdf

app = FastAPI()

# Static files (CSS, images, charts)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})


@app.post("/generate-pdf")
def generate_report(data: FarmData):
    # 1. Calculate summary
    summary = calculate_summary(
        data.expenses,
        data.incomes,
        data.total_acres
    )

    # 2. Generate expense chart
    chart_path = "app/static/charts/expense_chart.png"
    generate_expense_chart(data.expenses, chart_path)

    # 3. Generate PDF
    filename = f"{data.crop_name}_{data.total_acres}_{data.season}.pdf"
    output_path = os.path.join("reports", filename)

    generate_pdf(data, summary, chart_path, output_path)

    # 4. Return PDF for download
    return FileResponse(
        output_path,
        media_type="application/pdf",
        filename=filename
    )
