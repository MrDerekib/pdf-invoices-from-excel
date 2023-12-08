import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

#  pandas needs openpyxl as optional package (no need to import)


filepaths = glob.glob("invoices/*xlsx")

print(filepaths)

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    #  print(df)
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    print(filepath)
    filename = Path(filepath).stem
    print(filename)
    invoice_number, invoice_date = filename.split("-")

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, text=f"Invoice #{invoice_number}", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(w=50, h=8, text=f"Date: {invoice_date}")
    pdf.output(f"PDFs/{filename}.pdf")

