import os

def parse_pdfs(directory_path):
    media_path = []  # List to store file paths of generated text files

    # Loop through all files in the directory
    for file_name in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file_name)

        # Check if the file is a PDF
        if file_name.lower().endswith('.pdf'):
            # Parse and save as text file using the provided function
            output_txt_path = extract_content_and_tables(file_path)

            # Add the path of the generated text file to the list
            media_path.append(output_txt_path)

    return media_path


def collect_textfiles(directory_path):
    media_path = []  # List to store file paths of text files

    # Loop through all files in the directory
    for file_name in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file_name)

        # Check if the file is a text file
        if file_name.lower().endswith('.txt') and os.path.isfile(file_path):
            # Add the path of the text file to the list
            media_path.append(file_path)

    return media_path
