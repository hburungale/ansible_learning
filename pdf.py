from docx import Document
def count_tables(docx_path):
    doc = Document(docx_path)
    table_count = 0

    for table in doc.tables:
        table_count += 1
        print(table)

    return table_count

# Replace 'your_file.docx' with the path to your DOCX file
docx_file_path = 'CTMS_PIR.docx'
tables_count = count_tables(docx_file_path)

print(f'The number of tables in the DOCX file is: {tables_count}')
