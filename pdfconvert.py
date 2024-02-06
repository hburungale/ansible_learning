from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

def convert_docx_table_to_pdf(docx_path, pdf_path):
    # Load the DOCX file
    doc = Document(docx_path)

    # Extract table data from the DOCX file
    table_data = []
    for table in doc.tables:
        for row in table.rows:
            row_data = [cell.text for cell in row.cells]
            table_data.append(row_data)

    # Print table_data for debugging
    print("Table Data:")
    for row in table_data:
        print(row)

    if not table_data:
        print("No table data found in the DOCX file.")
        return

    # Create a PDF file
    pdf = SimpleDocTemplate(pdf_path, pagesize=letter)
    
    # Create a table style without grid lines and background color
    style = TableStyle([
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    # ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    # ('LEFTPADDING', (1, 0), (-1, -1), 100),  # Adjust the value as needed
    # ('RIGHTPADDING', (0, 0), (-1, -1), -200),
])


    # Create a table and apply the style
    pdf_table = Table(table_data)
    pdf_table.setStyle(style)

    # Build the PDF file
    pdf.build([pdf_table])

# Example usage
docx_file = "/Users/hburungale/Desktop/Hrithik/IR_automation/ansible_learning/CTMS_PIR.docx"  # Replace with your DOCX file
pdf_file = "PIR1.pdf"     # Replace with the desired PDF output file

convert_docx_table_to_pdf(docx_file, pdf_file)

