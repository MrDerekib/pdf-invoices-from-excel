import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

#  pandas needs openpyxl as optional package (no need to import)


filepaths = glob.glob("invoices/*xlsx")

for filepath in filepaths:
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    #  Add header and logo of the company
    pdf.image("logo.png", h=10)
    pdf.set_font("Times", size=25, style="B")
    with pdf.local_context(text_mode="STROKE", line_width=1):
        pdf.cell(text="Fake Company INC.")
    pdf.ln()

    pdf.set_font(family="Times", size=12, style="B")
    pdf.cell(w=30, h=5, text="Calle Falsa, 123", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(w=30, h=5, text="08023 Barcelona", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(w=30, h=5, text="Spain", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(20)

    #  Split the filename to extract date an invoice_number
    filename = Path(filepath).stem
    invoice_number, invoice_date = filename.split("-")

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, text=f"Invoice #{invoice_number}", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(w=50, h=8, text=f"Date: {invoice_date}", new_x="LMARGIN", new_y="NEXT")

    # read excel and save to dataframe
    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    #  Add table header with blank spaces.
    columns = list(df.columns)
    columns = [item.replace("_", " ").title() for item in columns]

    pdf.set_font(family="Times", size=10, style="B")
    pdf.set_text_color(105, 105, 105)
    pdf.cell(w=30, h=8, align="C", text=str(columns[0]), border=1)
    pdf.cell(w=80, h=8, align="C", text=str(columns[1]), border=1)
    pdf.cell(w=32, h=8, align="C", text=str(columns[2]), border=1)
    pdf.cell(w=30, h=8, align="C", text=str(columns[3]), border=1)
    pdf.cell(w=20, h=8, align="C", text=str(columns[4]), border=1, new_x="LMARGIN", new_y="NEXT")

    #  Add rows to the table
    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(105, 105, 105)
        pdf.cell(w=30, h=8, align="C", text=str(row["product_id"]), border=1)
        pdf.cell(w=80, h=8, align="C", text=str(row["product_name"]), border=1)
        pdf.cell(w=32, h=8, align="C", text=str(row["amount_purchased"]), border=1)
        pdf.cell(w=30, h=8, align="C", text=str(row["price_per_unit"]), border=1)
        pdf.cell(w=20, h=8, align="C", text=str(row["total_price"]), border=1, new_x="LMARGIN", new_y="NEXT")

    # calculate total_sum
    total_sum = df["total_price"].sum()

    # blank row for total_sum
    pdf.set_font(family="Times", size=10)
    pdf.set_text_color(105, 105, 105)
    pdf.cell(w=30, h=8, border=1)
    pdf.cell(w=80, h=8, border=1)
    pdf.cell(w=32, h=8, border=1)
    pdf.cell(w=30, h=8, border=1)
    pdf.cell(w=20, h=8, align="C", text=str(total_sum), border=1, new_x="LMARGIN", new_y="NEXT")

    # Add a big text outside the table with the total_sum
    pdf.set_font(family="Times", size=16)
    pdf.set_text_color(0, 0, 0)
    pdf.ln()
    pdf.cell(w=200, h=8, align="C", text=f"Total price is {total_sum} Euros (TAX INCLUDED)",
             new_x="LMARGIN", new_y="NEXT")

    pdf.output(f"PDFs/{filename}.pdf")
