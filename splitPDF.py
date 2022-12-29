from PyPDF2 import PdfFileReader, PdfFileWriter


def merge(directory, file_name):
    # rozdzielanie pliku
    with open(directory, 'rb') as infile:
        reader = PdfFileReader(infile)
        number_of_pages = reader.getNumPages()
        for i in range(reader.getNumPages()):
            writer = PdfFileWriter()
            writer.addPage(reader.getPage(i))
            # wypełnia zerami
            with open(file_name + ' ' + str(i + 1).zfill(len(str(number_of_pages))) + '.pdf', 'wb') as outfile:
                writer.write(outfile)
