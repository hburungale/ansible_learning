from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib import colors

def convert_docx_to_pdf(docx_path, pdf_path):
    doc = Document(docx_path)
    pdf_elements = []

    for element in doc.element.body:
        if element.__class__.__name__ == 'Paragraph':
            # Handle paragraphs
            pdf_elements.append(Paragraph(element.text))
        elif element.__class__.__name__ == 'Table':
            # Handle tables
            table_data = []
            for row in element.rows:
                row_data = [cell.text for cell in row.cells]
                table_data.append(row_data)

            table = Table(table_data)
            table.setStyle(TableStyle([
                                       ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                       ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                       ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                      ]))

            pdf_elements.append(table)

    doc = SimpleDocTemplate(pdf_path, pagesize=letter)
    doc.build(pdf_elements)

# Example usage
word_file_path = '/Users/hburungale/Desktop/Hrithik/IR_automation/ansible_learning/CTMS_Val3_HDC_PIR.docx'
pdf_output_path = 'document.pdf'

convert_docx_to_pdf(word_file_path, pdf_output_path)
