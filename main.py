import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

#  pandas needs openpyxl as optional package (no need to import)


filepaths = glob.glob("invoices/*xlsx")

print(filepaths)

for filepath in filepaths:
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    print(filepath)
    filename = Path(filepath).stem
    print(filename)
    invoice_number, invoice_date = filename.split("-")

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, text=f"Invoice #{invoice_number}", new_x="LMARGIN", new_y="NEXT")

    pdf.cell(w=50, h=8, text=f"Date: {invoice_date}", new_x="LMARGIN", new_y="NEXT")

    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    #  print(df)

    columns = list(df.columns)
    print(columns[0].replace("_", " "))
    columns = [item.replace("_", " ").title() for item in columns]

    pdf.set_font(family="Times", size=10, style="B")
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, text=str(columns[0]), border=1)
    pdf.cell(w=80, h=8, text=str(columns[1]), border=1)
    pdf.cell(w=32, h=8, text=str(columns[2]), border=1)
    pdf.cell(w=30, h=8, text=str(columns[3]), border=1)
    pdf.cell(w=20, h=8, text=str(columns[4]), border=1, new_x="LMARGIN", new_y="NEXT")

    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, text=str(row["product_id"]), border=1)
        pdf.cell(w=80, h=8, text=str(row["product_name"]), border=1)
        pdf.cell(w=32, h=8, text=str(row["amount_purchased"]), border=1)
        pdf.cell(w=30, h=8, text=str(row["price_per_unit"]), border=1)
        pdf.cell(w=20, h=8, text=str(row["total_price"]), border=1, new_x="LMARGIN", new_y="NEXT")



    pdf.output(f"PDFs/{filename}.pdf")

