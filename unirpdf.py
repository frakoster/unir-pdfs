import os
from PyPDF2 import PdfMerger

def merge_pdfs(input_folder, output_file):
    """
    Merge all PDF files from the specified folder into a single PDF.

    :param input_folder: Path to the folder containing PDF files.
    :param output_file: Path to the output merged PDF file.
    """
    merger = PdfMerger()

    # Get a sorted list of PDF files in the input folder
    pdf_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.pdf')]
    pdf_files.sort()

    if not pdf_files:
        print("No PDF files found in the specified folder.")
        return

    # Add each PDF to the merger
    for pdf in pdf_files:
        pdf_path = os.path.join(input_folder, pdf)
        print(f"Adding: {pdf_path}")
        merger.append(pdf_path)

    # Write the merged PDF to the output file
    try:
        merger.write(output_file)
        print(f"Merged PDF saved as: {output_file}")
    except Exception as e:
        print(f"Error while saving merged PDF: {e}")
    finally:
        merger.close()

if __name__ == "__main__":
    input_folder = input("Enter the path to the folder containing PDF files: ")
    output_file = input("Enter the path for the output merged PDF file: ")
    
    merge_pdfs(input_folder, output_file)
