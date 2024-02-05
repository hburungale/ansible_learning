from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

def convert_docx_tables_to_pdf(docx_path, pdf_path):
    # Load the DOCX file
    doc = Document(docx_path)

    # Extract table data from the DOCX file
    table_data_list = []
    for table_num, table in enumerate(doc.tables):
        table_data = []
        for row in table.rows:
            row_data = [cell.text for cell in row.cells]
            table_data.append(row_data)
        table_data_list.append(table_data)

    # Create a PDF file
    pdf = SimpleDocTemplate(pdf_path, pagesize=letter)

    # Define different styles for each table
    table_styles = [
        TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('RIGHTPADDING', (0, 0), (-1, -1), -50),
        ]),
        TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Times-Roman'),
            ('RIGHTPADDING', (0, 0), (-1, -1), -100),
        ]),
        # Add more styles for additional tables as needed
    ]

    # Iterate through tables and apply styles
    for table_num, table_data in enumerate(table_data_list):
        # Check if a corresponding style is defined
        if table_num < len(table_styles):
            style = table_styles[table_num]
        else:
            # Use a default style if no specific style is defined
            style = TableStyle([
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (-1, 0), 'Arial'),  # Change to the default font
                ('RIGHTPADDING', (0, 0), (-1, -1), -50),
            ])

        # Create a table and apply the style
        pdf_table = Table(table_data)
        pdf_table.setStyle(style)

        # Build the PDF file with the current table
        pdf.build([pdf_table])

# Example usage
docx_file = "CTMS_PIR.docx"  # Replace with your DOCX file
pdf_file = "output.pdf"  # Replace with the desired PDF output file

convert_docx_tables_to_pdf(docx_file, pdf_file)
