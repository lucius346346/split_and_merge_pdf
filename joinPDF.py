from PyPDF2 import PdfFileReader, PdfFileWriter


def join(files):
    # łączenie pliku
    writer = PdfFileWriter()
    for file in files:
        with open(file, 'rb') as infile:
            reader = PdfFileReader(infile)
            for i in range(reader.getNumPages()):
                writer.addPage(reader.getPage(i))
            with open('newfile.pdf', 'wb') as outfile:
                writer.write(outfile)
