from docx import Document
import os
import os

# file_path = os.path.abspath('./CTMS_Val1_PIR.docx')

# if os.access(file_path, os.R_OK):
#     print(f"Your Python code has read permission for the file at {file_path}.")
# else:
#     print(f"Your Python code does not have read permission for the file at {file_path}.")


def replace_and_print_word_file_content(file_path, replacements):
    
    print(file_path)

    document = Document(file_path)
    for paragraph in document.paragraphs:
        print(paragraph.text)

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
    output_path = "newfile.docx"
    document.save(output_path)
    print(f"\nUpdated Word file saved to: {output_path}")

if __name__ == "__main__":
    # Specify the path to the Word file
    script_directory = os.path.dirname(os.path.abspath(__file__))
    print("script_directory",script_directory)
    # file_path = os.path.join(script_directory, "./app_codes/CTMS_Val1_PIR.docx")
    # print(file_path)
    # file_path1= "./app_codes/CTMS_Val1_PIR.docx"
    # print(file_path1)
    file_path2 = os.path.join(script_directory, "\CTMS_Val1_PIR.docx")
    print(file_path2, "new")
    




    
    word_file_path = file_path2

    # Specify the replacements as a dictionary
    replacements = {
        "Product_Name": "CTMS",
        "Product_Version": "2202",
        
    }

    # Call the function to replace and print the content
    replace_and_print_word_file_content(word_file_path, replacements)
