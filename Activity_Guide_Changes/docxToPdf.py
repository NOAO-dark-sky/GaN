import sys
import os
import comtypes.client

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
                    doc.SaveAs(out_file, FileFormat=wdFormatPDF)
                    doc.Close()
                    word.Quit()

                    continue
                else:
                    continue
        except:
            continue
