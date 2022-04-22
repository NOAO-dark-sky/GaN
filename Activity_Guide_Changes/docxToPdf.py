import sys
import os
#Is needed to install comtypes package
import comtypes.client

#open word document, save as a pdf
def docxtopdf():
    master_direct = os.getcwd()

    for directory in os.listdir(master_direct):
        try:
            for filename in os.listdir(directory):
                if filename.endswith(".docx"):
                    wdFormatPDF = 17

                    in_file = os.path.abspath(filename)
                    out_file1 = os.path.abspath(filename)
                    out_file2 = out_file1[:-4] + 'pdf'
                    word = comtypes.client.CreateObject('Word.Application')
                    doc = word.Documents.Open(in_file)
                    #out_file2 is The PDF file expected as the outcome
                    doc.SaveAs(out_file2, FileFormat=wdFormatPDF)
                    doc.Close()
                    word.Quit()

                    continue
                else:
                    continue
        except:
            continue
