"""
import img2pdf
from PIL import Image # Pillow library for image handling

    # Path to your input image
image_path = "1.png" 
    # Path for the output PDF
pdf_path = "output2.pdf"

try:
        # Open the image using Pillow
    with Image.open(image_path) as img:
            # Convert the image to PDF bytes
        pdf_bytes = img2pdf.convert(img.filename)

            # Write the PDF bytes to a file
        with open(pdf_path, "wb") as f:
                f.write(pdf_bytes)
    print(f"Successfully converted '{image_path}' to '{pdf_path}'")
except FileNotFoundError:
    print(f"Error: Image file not found at '{image_path}'")
except Exception as e:
    print(f"An error occurred: {e}")


"""

from PyPDF2 import PdfReader, PdfWriter
def remove_pdf_pages(input_pdf_path, output_pdf_path, pages_to_remove):
    """
    Removes specified pages from a PDF file and saves the result to a new PDF.

    Args:
        input_pdf_path (str): The path to the input PDF file.
        output_pdf_path (str): The path to save the modified PDF file.
        pages_to_remove (list): A list of page numbers (1-indexed) to remove.
    """
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()

    # Adjust page numbers to 0-indexed for Python list access
    pages_to_remove_0_indexed = [p - 1 for p in pages_to_remove]

    for page_num in range(len(reader.pages)):
        if page_num not in pages_to_remove_0_indexed:
            writer.add_page(reader.pages[page_num])

    with open(output_pdf_path, 'wb') as output_pdf_file:
        writer.write(output_pdf_file)

if __name__ == "__main__":
    input_pdf = "s.pdf"  # Replace with your input PDF file name
    output_pdf = "output_modified.pdf" # Replace with your desired output PDF file name
    pages_to_delete = [1, 3, 4] # Example: Delete pages 2, 4, and 6 (1-indexed)

    try:
        remove_pdf_pages(input_pdf, output_pdf, pages_to_delete)
        print(f"Pages {pages_to_delete} removed from '{input_pdf}' and saved to '{output_pdf}'.")
    except FileNotFoundError:
        print(f"Error: Input PDF file '{input_pdf}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")