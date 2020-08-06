from PyPDF2 import PdfFileWriter, PdfFileReader
    
def order_pages):

    #change pdf page indexes to iterator in Python
    for i in order:
        ordered_list.append(i - 1)

    output_pdf = PdfFileWriter()

    with open(input_file, 'rb') as readfile:
        input_pdf = PdfFileReader(readfile)

        for page in ordered_list:
            output_pdf.addPage(input_pdf.getPage(page))

        with open(output_file, "wb") as writefile:
            output_pdf.write(writefile)
            
#output file order
order = [1, 2, 3, 4, 5]

#empty initial list
ordered_list = []

#input file
original_file = r'C:\input.pdf'

#output file
target_file = r'C:\output.pdf

order_pages()
