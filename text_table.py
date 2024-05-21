import os
import pdfplumber
from tabulate import tabulate
import fitz

def extract_content_and_tables(pdf_path):
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    output_txt_path = f"{base_name}.txt"

    contents = []

    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages):
            try:
                # Extract text content from the page
                text = page.extract_text()
                contents.append(text)

                # Extract tables from the page
                extracted_tables = page.extract_tables()
                if extracted_tables:
                    for table in extracted_tables:
                        contents.append(tabulate(table, tablefmt="grid"))
                        contents.append('-' * 50)

            except UnicodeDecodeError as e:
                # Handle the decoding error
                print(f"UnicodeDecodeError on page {page_num + 1}: {str(e)}")

    # Write contents to a text file
    with open(output_txt_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write('\n'.join(contents))

    return output_txt_path  # Return the path to the output text file
