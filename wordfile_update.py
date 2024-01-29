from docx import Document
import os
import os

file_path = os.path.abspath('./CTMS_Val1_PIR.docx')

if os.access(file_path, os.R_OK):
    print(f"Your Python code has read permission for the file at {file_path}.")
else:
    print(f"Your Python code does not have read permission for the file at {file_path}.")


def replace_and_print_word_file_content(file_path, replacements):
    document = Document(file_path)

    print("Before Replacement:")
    for table in document.tables:
        for row in table.rows:
            for cell in row.cells:
                print(cell.text)

    # Replace target words with replacement words
    for table in document.tables:
        for row in table.rows:
            for cell in row.cells:
                for target_word, replacement_word in replacements.items():
                    cell.text = cell.text.replace(target_word, replacement_word)

    print("\nAfter Replacement:")
    for table in document.tables:
        for row in table.rows:
            for cell in row.cells:
                print(cell.text)

    # Save the updated Word document
    output_path = file_path
    document.save(output_path)
    print(f"\nUpdated Word file saved to: {output_path}")

if __name__ == "__main__":
    # Specify the path to the Word file
    file_path = os.path.abspath('./CTMS_Val1_PIR.docx')
    word_file_path = file_path

    # Specify the replacements as a dictionary
    replacements = {
        "Product_Name": "1",
        "Product_Version": "2",
        # Add more key-value pairs as needed
    }

    # Call the function to replace and print the content
    replace_and_print_word_file_content(word_file_path, replacements)
