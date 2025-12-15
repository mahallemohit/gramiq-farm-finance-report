# GramIQ Farm Finance PDF Report

## Overview
This project is a backend application built using FastAPI. It accepts farm finance data through a web form and generates a downloadable PDF report containing summaries, charts, tabular data, and a ledger.

## Features
- Farmer & crop details input
- Multiple expense and income entries
- Automatic financial calculations
- Expense distribution chart
- Ledger generation
- Downloadable PDF report

## Tech Stack
- Python
- FastAPI
- Jinja2
- WeasyPrint
- Matplotlib
- HTML & JavaScript

## Project Structure
All application code is organized under the `app/` directory:
- `app/templates/` – HTML templates
- `app/services/` – business logic (calculations, charts, PDF)
- `app/static/` – charts and static assets

## Setup Instructions

```bash
git clone https://github.com/mahallemohit/gramiq-farm-finance-report.git
cd gramiq-farm-finance-report
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
