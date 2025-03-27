import pikepdf

password = "0007"  # PDF 암호
input_pdf = "tools/3주차.pdf"
output_pdf = "3주차 (공유).pdf"

pdf = pikepdf.open(input_pdf, password=password)
pdf.save(output_pdf)