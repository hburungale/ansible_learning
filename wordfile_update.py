from docx import Document

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
    output_path = "CTMS_Val1_PIR_new.docx"
    document.save(output_path)
    print(f"\nUpdated Word file saved to: {output_path}")

if __name__ == "__main__":
    # Specify the path to the Word file
    word_file_path = "CTMS_Val1_PIR_new.docx"

    # Specify the replacements as a dictionary
    replacements = {
        "Product_Name": "1",
        "Product_Version": "2",
        # Add more key-value pairs as needed
    }

    # Call the function to replace and print the content
    replace_and_print_word_file_content(word_file_path, replacements)
