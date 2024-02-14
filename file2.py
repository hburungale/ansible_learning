from docx import Document
import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

def apply_styles(pdf_table, table_index):
    if table_index == 0:
        style = TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('RIGHTPADDING', (0, 0), (-1, -1), -200)

        ])
    elif table_index == 1:
        style = TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ])
    else:
        # Add more conditions for additional tables if needed
        style = TableStyle([])

    pdf_table.setStyle(style)

def count_tables(docx_path):
    doc = Document(docx_path)
    table_count = 0

    # Create a PDF file
    pdfname=os.environ.get('CTMS_URL')
    pdffilename = f"{pdfname}_PIR.pdf"
    pdf = SimpleDocTemplate(pdffilename, pagesize=letter)
    # pdf = SimpleDocTemplate("Distro_PIR.pdf", pagesize=letter)

    pdf_tables = []

    for table_index, table in enumerate(doc.tables):
        table_count += 1
        # print(table)

        # Extract table data
        table_data = []
        for row in table.rows:
            row_data = [cell.text for cell in row.cells]
            table_data.append(row_data)

        # Create a PDF table
        pdf_table = Table(table_data)

        # Apply style based on the table index
        apply_styles(pdf_table, table_index)

        # Add the styled table to the list
        pdf_tables.append(pdf_table)

    # Build the PDF file with all tables
    pdf.build(pdf_tables)

    # return table_count

# Replace 'your_file.docx' with the path to your DOCX file
docx_file_path = 'PIR.docx'
tables_count = count_tables(docx_file_path)

# print(f'The number of tables in the DOCX file is: {tables_count}')
