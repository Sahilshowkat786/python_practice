from pypdf import PdfWriter
import os

folder = r"D:\PDFs"

output = os.path.join(folder, "merged.pdf")

writer = PdfWriter()

for file in sorted(os.listdir(folder)):
    if file.lower().endswith(".pdf") and file != "merged.pdf":
        pdf_path = os.path.join(folder, file)
        writer.append(pdf_path)

with open(output, "wb") as f:
    writer.write(f)

print("PDFs merged successfully!")
print("Saved at:", output)