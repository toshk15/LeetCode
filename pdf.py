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