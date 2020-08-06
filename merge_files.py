from PyPDF2 import PdfFileWriter, PdfFileReader

def merge_pdf():

    pdf2merge = [file1, file2]
    pdfWriter = PdfFileWriter()
    # loop through all PDFs
    for filename in pdf2merge:
        # rb for read binary
        pdfFileObj = open(filename, 'rb')
        pdfReader = PdfFileReader(pdfFileObj)
        # Opening each page of the PDF
        for pageNum in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
    # save PDF to file, wb for write binary
    pdfOutput = open(merged_file, 'wb')
    # Outputting the PDF
    pdfWriter.write(pdfOutput)
    # Closing the PDF writer
    pdfOutput.close()
    return('Files merged')

#files to be merged
file1 = r'C:\file1.pdf'
file2 = r'C:\file2.pdf'

#final file
merged_file = r'C:\merged_file.pdf'

merge_pdf()
